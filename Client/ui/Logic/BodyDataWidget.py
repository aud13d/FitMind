import json
from datetime import datetime

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QButtonGroup

from Client.services.server_bodydata import BodyDataService
from Client.ui.Components.NetworkErrorTipLabel import NetworkErrorTipLabel
from Client.ui.Components.RecordListDialog import RecordListDialog
from Client.ui.Designer.ui_BodyData import Ui_Widget_BodyData
from Client.ui.Components.bodyFrame import BodyFrame
from Client.services.user_session import UserSession

class BodyDataWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.ui = Ui_Widget_BodyData()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.setup_Unit_button_group()
        self.setup_Show_button_group()
        self.ui.stackedWidget.setCurrentIndex(0) # self.ui.page_body_data
        self.body_frame = BodyFrame(self.ui.page_body_data)

        self.unit_weight = "kg" if self.ui.button_body_kg.isChecked() else "g"
        self.unit_percentage = "%"
        self.unit_length = "cm"

        # 网络错误提示初始化（悬浮小标签，默认隐藏）
        self.network_error_tip = NetworkErrorTipLabel(self)
        self.network_error_tip.hide()

        # 初始化用户ID
        self.user_id = UserSession.get_user_id()

        self.bind()

    def bind(self):
        self.ui.button_body_data.clicked.connect(self.move_to_body_data)
        self.ui.button_body_graph.clicked.connect(self.move_to_body_graph)

        self.ui.label_body_current_weight.clicked.connect(self.set_current_weight)
        self.ui.label_body_target_weight.clicked.connect(self.on_click_target_weight)
        self.ui.label_body_body_fat.clicked.connect(self.on_click_body_fat)


    def move_to_body_data(self):
        """切换到数据界面"""
        self.ui.stackedWidget.setCurrentIndex(0)

    def move_to_body_graph(self):
        """切换到图表界面"""
        self.ui.stackedWidget.setCurrentIndex(1)

    def setup_Unit_button_group(self):
        """设置单位转换"""
        self.unit_group = QButtonGroup(self)
        self.unit_group.setExclusive(True)
        self.unit_group.addButton(self.ui.button_body_kg, 0)
        self.unit_group.addButton(self.ui.button_body_g, 1)
        self.ui.button_body_kg.setChecked(True)

    def setup_Show_button_group(self):
        """设置显示转换"""
        self.show_group = QButtonGroup(self)
        self.show_group.setExclusive(True)
        self.show_group.addButton(self.ui.button_body_data, 0)
        self.show_group.addButton(self.ui.button_body_graph, 1)
        self.ui.button_body_data.setChecked(True)

    def set_current_weight(self):
        """设置当前体重"""
        self.dialog = RecordListDialog(parent=self, input_title="weight",unit=self.unit_weight,date_text=datetime.today().strftime("%Y-%m-%d"))
        self.dialog.setModal(True)
        self.dialog.save_current_weight_signal.connect(self.save_current_weight)

        self.dialog.exec()

    def save_current_weight(self, current_weight):
        """保存当前体重，调用发送网络请求"""
        user_id = self.user_id
        current_weight = current_weight

        if not current_weight:
            self.show_tip("Please enter a weight",success=False)
            return

        response = BodyDataService.request_current_weight_save(user_id,current_weight)

        if response is None:
            self.show_tip("Network error, please try again",success=False)
            return

        try:
            data = response.json()
        except ValueError:
            self.show_tip("Invalid server response.", success=False)

        if response.status_code == 200:
            message = data.get("message","Current Weight saved!")
            self.show_tip(message,success=True)
            print("Successfully!",message)

        else:
            message = data.get("message","Failed to save Current Weight.")
            self.show_tip(message,success=False)
            print("Failed!",message)


    def show_tip(self, message, success=True):
        """用NetworkErrorTipLabel显示提示，自动处理消息类型和样式"""
        # 如果是列表或者字典，转成字符串显示，防止setText报错
        if not isinstance(message, str):
            if isinstance(message, list) or isinstance(message, dict):
                message = json.dumps(message, ensure_ascii=False, indent=2)
            else:
                message = str(message)

        if success:
            self.network_error_tip.setStyleSheet("color: white; background-color: rgba(0, 128, 0, 180);")
        else:
            self.network_error_tip.setStyleSheet("color: white; background-color: rgba(255, 0, 0, 180);")

        self.network_error_tip.show_message(message)


    def on_click_target_weight(self):
        print("点击了目标体重～")

    def on_click_body_fat(self):
        print("点击了体脂率～")


