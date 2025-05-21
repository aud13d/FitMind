import json

from PySide6.QtCore import QDate, QLocale, Qt
from PySide6.QtWidgets import (QDialog, QCalendarWidget,
                               QVBoxLayout, QDialogButtonBox, QApplication,  QDateEdit)

from Client.services.server_rest import RestService
from Client.services.user_session import UserSession
from Client.ui.Components.NetworkErrorTipLabel import NetworkErrorTipLabel
from Client.ui.Designer.ui_NewRest import Ui_Dialog_NewRest


class NewRestDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog_NewRest()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        if parent:
            self.setGeometry(parent.geometry())

        # 初始化设置
        self.init_date()
        self.init_color_buttons()

        # 用户ID
        self.user_id = UserSession.get_user_id()

        # 网络错误提示初始化（悬浮小标签，默认隐藏）
        self.network_error_tip = NetworkErrorTipLabel(self)
        self.network_error_tip.hide()

        self.bind()


    def bind(self):
        self.connect_reason_buttons()
        self.ui.button_date_setting.clicked.connect(self.show_calendar_dialog)
        self.ui.button_return.clicked.connect(self.reject)
        self.ui.button_save.clicked.connect(self.save_rest)

    def save_rest(self):
        """保存休息"""
        user_id = self.user_id
        title = self.ui.lineEdit_rest_title.text()
        date_text = self.ui.button_date_setting.text()

        # 使用 QLocale 英文解析按钮上的日期文本（如 "May 21, 2025"）
        locale = QLocale(QLocale.English)
        qdate = locale.toDate(date_text, "MMM d, yyyy")

        if not qdate.isValid():
            qdate = QDate.currentDate()  # fallback，避免出错

        # 转换为 ISO 格式字符串："2025-05-21"
        date = qdate.toString(Qt.ISODate)

        color = self.get_selected_color()

        if not title:
            title = "Rest Day"

        response = RestService.request_rest_save(user_id, title, date, color)

        if response is None:
            self.show_tip("Network Error,please try again!", success=False)
            return

        try:
            data = response.json()
        except ValueError:
            self.show_tip("Invalid server response.", success=False)
            return

        if response.status_code == 200:
            message = data.get("message", "Rest saved!")
            self.show_tip(message, success=True)
            print("Successfully!", message)
            self.close()
        else:
            message = data.get("detail", "Rest save failed.")
            self.show_tip(message, success=False)
            print("Failed:", message)

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


    def init_date(self):
        """初始化日期显示"""
        locale = QLocale(QLocale.English)
        current_date = locale.toString(QDate.currentDate(), "MMM d, yyyy")
        self.ui.button_date_setting.setText(current_date)

    def connect_reason_buttons(self):
        """连接原因按钮到文本框"""
        reason_buttons = [
            self.ui.button_choice_1,  # Rest Day
            self.ui.button_choice_2,  # Busy
            self.ui.button_choice_3,  # Fall Ill
            self.ui.button_choice_4  # Be Injured
        ]
        for btn in reason_buttons:
            btn.clicked.connect(lambda _, b=btn: self.ui.lineEdit_rest_title.setText(b.text()))

    def show_calendar_dialog(self):
        """显示自定义日历对话框"""
        dialog = QDialog(self)
        dialog.setWindowTitle("Select Date")
        dialog.setFixedSize(340, 340)

        # 创建日历组件
        calendar = QCalendarWidget(dialog)
        calendar.setLocale(QLocale(QLocale.English))  # 英文显示
        calendar.setGridVisible(True)

        # 解析当前日期
        locale = QLocale(QLocale.English)
        current_text = self.ui.button_date_setting.text()
        current_date = locale.toDate(current_text, "MMM d, yyyy")

        # 无效日期处理
        if not current_date.isValid():
            current_date = QDate.currentDate()

        calendar.setSelectedDate(current_date)

        # 创建按钮组
        btn_box = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel,
            dialog
        )
        btn_box.accepted.connect(dialog.accept)
        btn_box.rejected.connect(dialog.reject)

        # 设置布局
        layout = QVBoxLayout(dialog)
        layout.addWidget(calendar)
        layout.addWidget(btn_box)

        if dialog.exec() == QDialog.DialogCode.Accepted:
            selected_date = calendar.selectedDate()
            formatted_date = locale.toString(selected_date, "MMM d, yyyy")
            self.ui.button_date_setting.setText(formatted_date)

    def init_color_buttons(self):
        """初始化颜色选择按钮"""
        self.color_buttons = [
            self.ui.button_rest_setred,  # Red
            self.ui.button_rest_setroange,  # Orange
            self.ui.button_rest_setgreen,  # Green
            self.ui.button_rest_setblue,  # Blue
            self.ui.button_rest_setpurple  # Purple
        ]

        # 颜色映射表
        self.color_map = {
            self.ui.button_rest_setred: "#FF0000",
            self.ui.button_rest_setroange: "#FFA500",
            self.ui.button_rest_setgreen: "#90EE90",
            self.ui.button_rest_setblue: "#87CEEB",
            self.ui.button_rest_setpurple: "#DDA0DD"
        }

        # 设置按钮样式和属性
        for btn in self.color_buttons:
            btn.setStyleSheet(f"""
                QPushButton {{
                    background-color: {self.color_map[btn]};
                    border: none;
                    min-width: 45px;
                    max-width: 45px;
                    min-height: 45px;
                    max-height: 45px;
                }}
                QPushButton[selected="true"] {{
                    border: 2px solid black;
                    margin: 0px;
                }}
            """)
            btn.setProperty("selected", False)
            btn.clicked.connect(self.update_color_selection)

    def update_color_selection(self):
        """更新颜色选择状态"""
        sender = self.sender()

        # 重置所有按钮状态
        for btn in self.color_buttons:
            btn.setProperty("selected", False)
            btn.style().unpolish(btn)
            btn.style().polish(btn)

        # 设置当前选中状态
        sender.setProperty("selected", True)
        sender.style().unpolish(sender)
        sender.style().polish(sender)



    def get_selected_color(self):
        """获取当前选中颜色"""
        for btn in self.color_buttons:
            if btn.property("selected"):
                return self.color_map[btn]
        return "#FFFFFF"
