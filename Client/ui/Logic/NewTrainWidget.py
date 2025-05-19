from PySide6.QtCore import Qt, Signal, QTime, QTimer, QDateTime

from Client.ui.Components.ActionFrame import ActionFrame
from Client.ui.Designer.ui_NewTrain import Ui_Widget_NewTrain
from PySide6.QtWidgets import QWidget, QVBoxLayout
from Client.ui.Components.MaskWidget import MaskWidget
from Client.ui.Components.AcationSettingFrame import ActionSettingFrame
from Client.ui.Logic.AddActionDialog import AddActionDialog
from Client.ui.Logic.CancelTrainingDialog import CancelTrainingDialog
from Client.ui.Logic.FinishTrainingDialog import FinishTrainingDialog
from Client.services.server_train import TrainService
from Client.ui.Components.NetworkErrorTipLabel import NetworkErrorTipLabel
from Client.services.user_session import UserSession

class NewTrainWidget(QWidget):
    minimized_signal = Signal()  # 发送最小化信号给 MainInterfaceWindow

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget_NewTrain()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.timer = QTimer(self)  # 创建定时器
        self.time = QTime(0, 0)  # 计时初始时间设为00:00
        self.timer_running = False
        self.start_datetime = None
        self.end_datetime = None

        # 初始化动作列表
        self.layout_actions = QVBoxLayout(self.ui.scrollAreaWidgetContents)
        self.layout_actions.setAlignment(Qt.AlignTop)
        self.layout_actions.setSpacing(10)
        self.layout_actions.setContentsMargins(10, 10, 10, 0)
        self.dialog = None

        # 初始化计划状态
        self.has_planned_exercise = False  # 默认没有计划运动

        # 网络错误提示初始化（悬浮小标签，默认隐藏）
        self.network_error_tip = NetworkErrorTipLabel(self)
        self.network_error_tip.hide()

        # 用户ID
        self.user_id = UserSession.get_user_id()

        self.bind()

    def bind(self):
        self.ui.button_newtrain_minimize.clicked.connect(self.minisize_window)
        self.ui.button_newtrain_add_action.clicked.connect(self.open_addaction_dialog)

        self.ui.button_newtrain_start.clicked.connect(self.start_timer)
        self.timer.timeout.connect(self.update_time) # 每秒更新时间
        self.ui.button_newtrain_finish.clicked.connect(self.finish_training)

    def minisize_window(self):
        """最小化窗口并发送信号"""
        self.hide()
        self.minimized_signal.emit()  # 通知 MainInterfaceWindow

    def start_timer(self):
        """开始计时"""
        self.timer.start(1000)
        self.timer_running = True
        self.start_datetime = QDateTime.currentDateTime()
        self.ui.button_newtrain_start.setEnabled(False)
        self.ui.button_newtrain_start.setVisible(False)
        self.ui.label_newtrain_time.setStyleSheet("color: blue;font: 700 18pt '微软雅黑';")

    def update_time(self):
        """更新时间"""
        self.time = self.time.addSecs(1)
        self.ui.label_newtrain_time.setText(self.time.toString("mm:ss"))

    def stop_timer(self):
        """停止计时并记录当前时间"""
        if not self.timer_running:
            return

        self.timer.stop()
        current_time = self.time.toString("mm:ss")
        print(f"计时结束，当前时间是: {current_time}")
        self.timer_running = False
        self.ui.button_newtrain_start.setEnabled(True)
        self.ui.button_newtrain_start.setVisible(True)

        self.ui.label_newtrain_time.setStyleSheet("color: black;font: 700 18pt '微软雅黑';")

    def finish_training(self):
        """完成训练"""
        if self.has_planned_exercise:  # 判断是否有运动计划
            self.open_FinishTraining()
        else:
            self.open_CancelTraining()

    def open_FinishTraining(self):
        """完成训练：完成"""
        # 创建遮罩层
        self.mask = MaskWidget(self)
        self.mask.show()

        # 创建并显示对话框
        self.dialog= FinishTrainingDialog(self)

        self.dialog.training_finished_signal.connect(self.handle_train_finish)
        self.dialog.setModal(True)
        self.dialog.show()
        self.dialog.raise_()
        self.dialog.exec_()

        # 关闭遮罩层
        self.mask.close()

    def calculate_training_times(self):
        """计算训练时长、结束时间和格式化时间字符串"""
        duration = self.time.hour() * 60 + self.time.minute() + self.time.second() / 60.0
        end_datetime = self.start_datetime.addSecs(
            self.time.hour() * 3600 + self.time.minute() * 60 + self.time.second()
        )
        start_date_str = self.start_datetime.toString("yyyy-MM-dd HH:mm:ss") if self.start_datetime else ""
        end_date_str = end_datetime.toString("yyyy-MM-dd HH:mm:ss") if end_datetime else ""
        return duration, end_datetime, start_date_str, end_date_str

    def handle_train_finish(self):
        """完成训练后调用接口的整个流程"""
        user_id = self.user_id
        name = self.ui.lineEdit_newtrain_trainging_title.text()

        duration, self.end_datetime, start_date, end_date = self.calculate_training_times()

        actions = self.get_action_data()
        if not actions:
            self.show_tip("Please add at least one action!", success=False)
            return

        response = TrainService.request_train_finish(user_id, name, duration, start_date, end_date, actions)

        if response is None:
            self.show_tip("Network error, please try again!", success=False)
            return

        try:
            data = response.json()
        except ValueError:
            self.show_tip("Invalid server response.", success=False)
            return

        if response.status_code == 200:
            message = data.get("message", "Training completed!")
            self.show_tip(message, success=True)
            print("Successfully!", message)
        else:
            message = data.get("detail", "Training submission failed.")
            self.show_tip(message, success=False)
            print("Failed:", message)

    def show_tip(self, message, success=True):
        """用NetworkErrorTipLabel显示提示，自动处理消息类型和样式"""
        # 如果是列表或者字典，转成字符串显示，防止setText报错
        if not isinstance(message, str):
            if isinstance(message, list) or isinstance(message, dict):
                import json
                message = json.dumps(message, ensure_ascii=False, indent=2)
            else:
                message = str(message)

        if success:
            self.network_error_tip.setStyleSheet("color: white; background-color: rgba(0, 128, 0, 180);")
        else:
            self.network_error_tip.setStyleSheet("color: white; background-color: rgba(255, 0, 0, 180);")

        self.network_error_tip.show_message(message)

    def get_action_data(self):
        """遍历 layout 中所有 ActionFrame，提取动作信息"""
        actions = []
        for i in range(self.layout_actions.count()):
            item = self.layout_actions.itemAt(i).widget()
            if isinstance(item, ActionFrame):
                action_info = {
                    "name": item.name,
                    "sets": item.sets,
                    "reps": item.reps,
                    "rest_time": item.rest_time,
                    "order": i + 1, # 按照添加顺序排序
                    "note": item.note,
                }
                actions.append(action_info)
        return actions

    def open_CancelTraining(self):
        """完成训练：取消"""
        # 创建遮罩层
        self.mask = MaskWidget(self)
        self.mask.show()

        # 创建并显示对话框
        self.dialog= CancelTrainingDialog(self)
        self.dialog.setModal(True)
        self.dialog.show()
        self.dialog.raise_()
        self.dialog.exec_()

        # 关闭遮罩层
        self.mask.close()

    def open_addaction_dialog(self):
        """弹出添加动作界面，宽度一致，底部对齐"""
        self.dialog = AddActionDialog(self)
        self.dialog.addaction_signal.connect(self.add_action_frame)
        self.dialog.setModal(True)
        self.dialog.exec_()

    def add_action_frame(self, action_name, action_icon):
        """添加动作"""
        action_frame = ActionFrame(action_name, action_icon)
        action_frame.setFixedSize(335, 55)

        self.layout_actions.addWidget(action_frame)

        self.last_action_frame = action_frame
        self.has_planned_exercise = True












