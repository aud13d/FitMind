from PySide6.QtCore import QDate, QLocale, Qt
from PySide6.QtWidgets import (QDialog, QCalendarWidget,
                               QVBoxLayout, QDialogButtonBox, QApplication,  QDateEdit)
from Client.ui.Designer.ui_NewRest import Ui_Dialog_add_action


class NewRestDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog_add_action()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        if parent:
            self.setGeometry(parent.geometry())

        # 初始化设置
        self.init_date()
        self.connect_reason_buttons()
        self.ui.pushButton_8.clicked.connect(self.show_calendar_dialog)
        self.init_color_buttons()
        self.ui.pushButton.clicked.connect(self.reject)
        self.ui.pushButton_2.clicked.connect(self.accept)

    def init_date(self):
        """初始化日期显示"""
        locale = QLocale(QLocale.English)
        current_date = locale.toString(QDate.currentDate(), "MMM d, yyyy")
        self.ui.pushButton_8.setText(current_date)

    def connect_reason_buttons(self):
        """连接原因按钮到文本框"""
        reason_buttons = [
            self.ui.pushButton_9,  # Rest Day
            self.ui.pushButton_10,  # Busy
            self.ui.pushButton_12,  # Fall Ill
            self.ui.pushButton_11  # Be Injured
        ]
        for btn in reason_buttons:
            btn.clicked.connect(lambda _, b=btn: self.ui.lineEdit.setText(b.text()))

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
        current_text = self.ui.pushButton_8.text()
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
            self.ui.pushButton_8.setText(formatted_date)

    def init_color_buttons(self):
        """初始化颜色选择按钮"""
        self.color_buttons = [
            self.ui.pushButton_4,  # Red
            self.ui.pushButton_5,  # Orange
            self.ui.pushButton_6,  # Green
            self.ui.pushButton_7,  # Blue
            self.ui.pushButton_3  # Purple
        ]

        # 颜色映射表
        self.color_map = {
            self.ui.pushButton_4: "#FF0000",
            self.ui.pushButton_5: "#FFA500",
            self.ui.pushButton_6: "#90EE90",
            self.ui.pushButton_7: "#87CEEB",
            self.ui.pushButton_3: "#DDA0DD"
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

    def get_rest_data(self):
        """获取最终数据"""
        return {
            "title": self.ui.lineEdit.text(),
            "date": self.ui.pushButton_8.text(),
            "color": self.get_selected_color(),
            "reason": self.ui.lineEdit.text()
        }

    def get_selected_color(self):
        """获取当前选中颜色"""
        for btn in self.color_buttons:
            if btn.property("selected"):
                return self.color_map[btn]
        return "#FFFFFF"
