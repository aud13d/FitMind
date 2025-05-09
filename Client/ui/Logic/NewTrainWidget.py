from PySide6.QtCore import Qt, Signal, QTime, QTimer

from Client.ui.Components.ActionFrame import ActionFrame
from Client.ui.Designer.ui_NewTrain import Ui_Widget_NewTrain
from PySide6.QtWidgets import QWidget, QVBoxLayout
from Client.ui.Components.MaskWidget import MaskWidget
from Client.ui.Logic.AddActionDialog import AddActionDialog
from Client.ui.Logic.CancelTrainingDialog import CancelTrainingDialog
from Client.ui.Logic.FinishTrainingDialog import FinishTrainingDialog

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

        # 初始化动作列表
        self.layout_actions = QVBoxLayout(self.ui.scrollAreaWidgetContents)
        self.layout_actions.setAlignment(Qt.AlignTop)
        self.layout_actions.setSpacing(10)
        self.layout_actions.setContentsMargins(10, 10, 10, 0)
        self.dialog = None

        # 初始化计划状态
        self.has_planned_exercise = False  # 默认没有计划运动

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
        self.dialog.setModal(True)
        self.dialog.show()
        self.dialog.raise_()
        self.dialog.exec_()

        # 关闭遮罩层
        self.mask.close()

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

    def add_action_frame(self, action_name,action_icon):
        """添加动作"""
        action_frame = ActionFrame(action_name,action_icon)
        if action_frame:
            action_frame.setFixedSize(335,55)
            self.layout_actions.addWidget(action_frame)

            # 设置有计划运动
            self.has_planned_exercise = True  # 添加了运动动作，设定为有计划








