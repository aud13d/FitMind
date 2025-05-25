import json
from datetime import datetime
import re

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QButtonGroup

from Client.services.server_bodydata import BodyDataService
from Client.cache.user_bodydata import UserBodyData
from Client.ui.Components.NetworkErrorTipLabel import NetworkErrorTipLabel
from Client.ui.Components.RecordListDialog import RecordListDialog
from Client.ui.Designer.ui_BodyData import Ui_Widget_BodyData
from Client.ui.Components.BodyFrame import BodyFrame
from Client.cache.user_session import UserSession

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

        # 初始化单位
        self.unit_weight = UserBodyData.Unit_weight
        self.unit_percentage = "%"
        self.unit_length = "cm"

        # 初始化体重数据
        self.Init_weight_label_value()

        # 网络错误提示初始化（悬浮小标签，默认隐藏）
        self.network_error_tip = NetworkErrorTipLabel(self)
        self.network_error_tip.hide()

        # 初始化用户ID
        self.user_id = UserSession.get_user_id()

        # 载入用户数据
        self.load_initial_body_data()

        self.recover_weight_unit()

        self.bind()

    def bind(self):
        # 界面切换
        self.ui.button_body_data.clicked.connect(self.move_to_body_data)
        self.ui.button_body_graph.clicked.connect(self.move_to_body_graph)

        # 体重数据点击事件
        self.ui.label_body_current_weight.clicked.connect(self.set_current_weight)
        self.ui.label_body_target_weight.clicked.connect(self.set_target_weight)
        self.ui.label_body_body_fat.clicked.connect(self.set_current_body_fat_rate)

        # 单位切换
        self.ui.button_body_kg.clicked.connect(self.on_unit_button_clicked)
        self.ui.button_body_g.clicked.connect(self.on_unit_button_clicked)

        # 显示切换
        self.body_frame.body_part_clicked.connect(self.on_body_part_clicked)

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

    def setup_Show_button_group(self):
        """设置显示转换"""
        self.show_group = QButtonGroup(self)
        self.show_group.setExclusive(True)
        self.show_group.addButton(self.ui.button_body_data, 0)
        self.show_group.addButton(self.ui.button_body_graph, 1)
        self.ui.button_body_data.setChecked(True)

    def Init_weight_label_value(self):
        """初始化体重相关的标签值"""
        def init_label(label, title, unit):
            label.setTextFormat(Qt.RichText)
            label.setTextInteractionFlags(Qt.NoTextInteraction)

            # 提取已有文本中的日期，若无则使用今天
            current_text = label.text()
            match = re.search(r'\d{4}-\d{2}-\d{2}', current_text)
            date_str = match.group(0) if match else datetime.today().strftime("%Y-%m-%d")

            value_html = '<span style="color:#007BFF; font:bold 24px "微软雅黑";">0</span>'
            unit_html = f'<span style="color:#868686;"> {unit}</span>'
            full_text = f"{title}<br>{date_str}<br><br>{value_html} {unit_html}"
            label.setText(full_text)

        init_label(self.ui.label_body_current_weight,"Current Weight", UserBodyData.Unit_weight)
        init_label(self.ui.label_body_target_weight,"Target Weight", UserBodyData.Unit_weight)
        init_label(self.ui.label_body_body_fat,"Current Fat Rate", self.unit_percentage)
        self.ui.button_body_kg.setText(UserBodyData.UNIT_KG)
        self.ui.button_body_g.setText(UserBodyData.UNIT_JIN)

    def load_initial_body_data(self):
        """载入已有的体重、目标体重和体脂率数据并更新显示"""
        # 如果缓存中已有数据，则直接用缓存更新界面
        if UserBodyData.current_weight is not None or \
                UserBodyData.target_weight is not None or \
                UserBodyData.body_fat_rate is not None:
            self.update_labels_from_user_data()
            return

        # 否则，请求服务器数据
        user_id = self.user_id
        response = BodyDataService.request_get_latest_body_data(user_id)

        if response is None:
            self.show_tip("Network error when loading data", success=False)
            return

        try:
            data = response.json()
        except ValueError:
            self.show_tip("Invalid server response", success=False)
            return

        if response.status_code != 200:
            self.show_tip(data.get("message", "Failed to load body data."), success=False)
            return

        # 写入 UserBodyData 缓存
        UserBodyData.update(data)

        # 更新界面显示
        self.update_labels_from_user_data()

    def recover_weight_unit(self):
        """恢复体重单位"""
        if UserBodyData.Unit_weight == UserBodyData.UNIT_KG:
            self.ui.button_body_kg.setChecked(True)
        elif UserBodyData.Unit_weight == UserBodyData.UNIT_JIN:
            self.ui.button_body_g.setChecked(True)

    def on_unit_button_clicked(self):
        if self.ui.button_body_kg.isChecked():
            UserBodyData.Unit_weight = UserBodyData.UNIT_KG
        elif self.ui.button_body_g.isChecked():
            UserBodyData.Unit_weight = UserBodyData.UNIT_JIN
        self.update_labels_from_user_data()
        # 更新按钮文本
        self.ui.button_body_kg.setText(UserBodyData.UNIT_KG)
        self.ui.button_body_g.setText(UserBodyData.UNIT_JIN)

    def convert_weight(self, value: float):
        if value is None:
            return None
        if UserBodyData.Unit_weight == UserBodyData.UNIT_KG:
            return value
        elif UserBodyData.Unit_weight == UserBodyData.UNIT_JIN:
            return value * 2
        return value

    def convert_to_kg(self, value: float):
        if UserBodyData.Unit_weight == UserBodyData.UNIT_JIN:
            return value / 2
        return value

    def update_labels_from_user_data(self):
        """根据缓存数据更新界面"""
        current_weight = self.convert_weight(UserBodyData.current_weight)
        target_weight = self.convert_weight(UserBodyData.target_weight)

        if current_weight is not None:
            self.update_current_weight_label_value(current_weight)
        if target_weight is not None:
            self.update_target_weight_label_value(target_weight)
        if UserBodyData.body_fat_rate is not None:
            self.update_current_body_fat_rate_label_value(UserBodyData.body_fat_rate)

        if hasattr(self, "body_frame"):
            circ_data = UserBodyData.circumferences or {}
            for part, info in circ_data.items():
                if info and info.get("value") is not None:
                    self.body_frame.update_label_value_by_part_name(part, info["value"])

    def set_current_weight(self):
        """设置当前体重"""
        self.dialog = RecordListDialog(parent=self, input_title="weight",unit=UserBodyData.Unit_weight,date_text=datetime.today().strftime("%Y-%m-%d"))
        self.dialog.setModal(True)
        self.dialog.save_current_weight_signal.connect(self.save_current_weight)

        self.dialog.exec()

    def save_current_weight(self, current_weight):
        """保存当前体重，调用发送网络请求"""
        user_id = self.user_id

        if not current_weight:
            self.show_tip("Please enter a weight",success=False)
            return

        # 转换为 Kg
        current_weight_kg = self.convert_to_kg(current_weight)

        response = BodyDataService.request_current_weight_save(user_id, current_weight_kg)

        if response is None:
            self.show_tip("Network error, please try again",success=False)
            return

        try:
            data = response.json()
        except ValueError:
            self.show_tip("Invalid server response.", success=False)

        if response.status_code == 200:
            message = data.get("message","Current Weight saved!")
            self.update_current_weight_label_value(current_weight)
            UserBodyData.update(current_weight=current_weight_kg)       #把更新的数据填入缓冲
            self.show_tip(message,success=True)
            print("Successfully!",message)

        else:
            message = data.get("message","Failed to save Current Weight.")
            self.show_tip(message,success=False)
            print("Failed!",message)

    def update_current_weight_label_value(self, current_weight,date=None):
        """更新体重标签的值"""
        if not date:
            date = datetime.today().strftime("%Y-%m-%d")

        value_html = f'<span style="color:#007BFF; font:bold 24px "微软雅黑";">{current_weight}</span>'
        unit_html = f'<span style="color:#868686;"> {UserBodyData.Unit_weight}</span>'
        full_text = f"Current weight<br>{date}<br><br>{value_html} {unit_html}"

        label = self.ui.label_body_current_weight
        label.setTextFormat(Qt.RichText)  # 启用富文本模式
        label.setTextInteractionFlags(Qt.NoTextInteraction)  # 防止鼠标选中文本
        label.setText(full_text)

    def set_target_weight(self):
        """设置目标体重"""
        self.dialog = RecordListDialog(parent=self, input_title="target weight",unit=UserBodyData.Unit_weight,date_text=datetime.today().strftime("%Y-%m-%d"))
        self.dialog.setModal(True)
        self.dialog.save_target_weight_signal.connect(self.save_target_weight)

        self.dialog.exec()

    def save_target_weight(self, target_weight):
        """保存目标体重，调用发送网络请求"""
        user_id = self.user_id
        if not target_weight:
            self.show_tip("Please enter a target weight",success=False)
            return

        # 转换为 Kg
        target_weight_kg = self.convert_to_kg(target_weight)

        response = BodyDataService.request_target_weight_save(user_id, target_weight_kg)
        if response is None:
            self.show_tip("Network error, please try again",success=False)
            return
        try:
            data = response.json()
        except ValueError:
            self.show_tip("Invalid server response.", success=False)
        if response.status_code == 200:
            message = data.get("message","Target Weight saved!")
            self.update_target_weight_label_value(target_weight)
            UserBodyData.update(target_weight=target_weight_kg)  # 把更新的数据填入缓冲
            self.show_tip(message,success=True)
            print("Successfully!",message)
        else:
            message = data.get("message","Failed to save Target Weight.")
            self.show_tip(message,success=False)
            print("Failed!",message)

    def update_target_weight_label_value(self, target_weight):
        """更新目标体重标签的值"""
        date = datetime.today().strftime("%Y-%m-%d")
        value_html = f'<span style="color:#007BFF; font:bold 24px "微软雅黑";">{target_weight}</span>'
        unit_html = f'<span style="color:#868686;"> {UserBodyData.Unit_weight}</span>'
        full_text = f"Target weight<br>{date}<br><br>{value_html} {unit_html}"
        label = self.ui.label_body_target_weight
        label.setTextFormat(Qt.RichText)  # 启用富文本模式
        label.setTextInteractionFlags(Qt.NoTextInteraction)  # 防止鼠标选中文本
        label.setText(full_text)

    def set_current_body_fat_rate(self):
        """保存体脂率，调用发送网络请求"""
        self.dialog = RecordListDialog(parent=self, input_title="body fat",unit=self.unit_percentage,date_text=datetime.today().strftime("%Y-%m-%d"))
        self.dialog.setModal(True)
        self.dialog.save_current_body_fat_rate_signal.connect(self.save_current_body_fat_rate)

        self.dialog.exec()

    def save_current_body_fat_rate(self, current_body_fat_rate):
        """保存体脂率，调用发送网络请求"""
        user_id = self.user_id

        if not current_body_fat_rate:
            self.show_tip("Please enter a body fat rate",success=False)
            return
        response = BodyDataService.request_current_body_fat_rate_save(user_id,current_body_fat_rate)
        if response is None:
            self.show_tip("Network error, please try again",success=False)
            return
        try:
            data = response.json()
        except ValueError:
            self.show_tip("Invalid server response.", success=False)
        if response.status_code == 200:
            message = data.get("message","Current Body Fat Rate saved!")
            self.update_current_body_fat_rate_label_value(current_body_fat_rate)
            UserBodyData.update(current_body_fat_rate=current_body_fat_rate)  # 把更新的数据填入缓冲
            self.show_tip(message,success=True)
            print("Successfully!",message)
        else:
            message = data.get("message","Failed to save Current Body Fat Rate.")
            self.show_tip(message,success=False)
            print("Failed!",message)

    def update_current_body_fat_rate_label_value(self, current_body_fat_rate,date=None):
        if not date:
            date = datetime.today().strftime("%Y-%m-%d")
        value_html = f'<span style="color:#007BFF; font:bold 24px "微软雅黑";">{current_body_fat_rate}</span>'
        unit_html = '<span style="color:#868686;"> %</span>'
        full_text = f"Body Fat<br>{date}<br><br>{value_html} {unit_html}"
        label = self.ui.label_body_body_fat
        label.setTextFormat(Qt.RichText)  # 启用富文本模式
        label.setTextInteractionFlags(Qt.NoTextInteraction)  # 防止鼠标选中文本
        label.setText(full_text)

    def on_body_part_clicked(self, part: str):
        """响应身体部位点击事件"""
        self.dialog = RecordListDialog(
            parent=self,
            input_title=part,
            unit=self.unit_length,
            date_text=datetime.today().strftime("%Y-%m-%d")
        )

        self.dialog.save_current_circumference_signal.connect(self.save_current_circumference)
        self.dialog.exec()

    def save_current_circumference(self, part: str, value: float):
        """通用方法：保存任意身体部位围度"""
        user_id = self.user_id
        if not value:
            self.show_tip(f"Please enter a {part} circumference", success=False)
            return

        # 调用通用的保存方法
        response = BodyDataService.request_current_circumference_save(user_id, part, value)
        if response is None:
            self.show_tip("Network error, please try again", success=False)
            return

        try:
            data = response.json()
        except ValueError:
            self.show_tip("Invalid server response.", success=False)
            return

        if response.status_code == 200:
            message = data.get("message", f"{part.capitalize()} circumference saved!")
            UserBodyData.update(data)  # 把更新的数据填入缓冲
            self.show_tip(message, success=True)
            self.body_frame.update_label_value_by_part_name(part, value)  # 提醒BodyFrame更新UI
            print("Successfully!", message)
        else:
            message = data.get("message", f"Failed to save {part} circumference.")
            self.show_tip(message, success=False)
            print("Failed!", message)

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
