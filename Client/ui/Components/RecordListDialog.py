"""""记录列表弹窗"""""
import sys
from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (
    QApplication, QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QListWidget, QFrame, QSizePolicy, QListWidgetItem, QWidget
)
from datetime import datetime, date
from Client.ui.Components.ClickableLabel import ClickableLabel


class RecordListDialog(QDialog):
    save_current_weight_signal = Signal(float)
    save_target_weight_signal  = Signal(float)
    save_current_body_fat_rate_signal = Signal(float)

    get_current_weight_signal = Signal()
    get_target_weight_signal = Signal()
    get_current_body_fat_rate_signal = Signal()

    get_weight_history_signal = Signal()
    get_body_fat_rate_history_signal = Signal()

    delete_weight_history_signal = Signal(date)
    delete_body_fat_rate_history_signal = Signal(date)


    def __init__(self, parent=None,input_title="", unit="", date_text=None):
        super().__init__(parent)

        if date_text is None:
            date_text = datetime.today().strftime("%Y-%m-%d")

        if parent:
            self.setFixedSize(parent.size())
            global_pos = parent.mapToGlobal(parent.rect().topLeft())
            self.move(global_pos)

        self.current_date = date_text  # 记录当前日期成员变量
        self.input_title = input_title  # 保存标题，方便更新显示

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setFixedSize(362, 700)

        # 主体白色背景容器 Frame（代替原窗口）
        self.bg_frame = QFrame(self)
        self.bg_frame.setStyleSheet("""
            QFrame {
                background-color: white;
                border-radius: 12px;
                font:"微软雅黑";
            }
        """)
        self.bg_frame.setObjectName("bg_frame")

        # 背景容器布局
        self.bg_layout = QVBoxLayout(self.bg_frame)
        self.bg_layout.setContentsMargins(20, 20, 20, 20)
        self.bg_layout.setSpacing(12)

        # 标题
        title_label = QLabel("Record list")
        title_label.setStyleSheet("font-size: 18px; font-weight: bold;")
        self.bg_layout.addWidget(title_label)

        # 记录列表
        self.record_list = QListWidget()
        self.record_list.setFocusPolicy(Qt.NoFocus)
        self.record_list.setSelectionMode(QListWidget.NoSelection)
        self.record_list.setStyleSheet("""
            QListWidget::item {
                background-color: transparent;
                border: none;
            }
            QListWidget::item:hover {
                background-color: transparent;
            }
            QListWidget::item:selected {
                background-color: transparent;
            }
        """)
        self.bg_layout.addWidget(self.record_list)

        # 输入区
        input_container = QFrame()
        input_container.setStyleSheet("""
            QFrame {
                background-color: white;
                border-radius: 8px;
                border: none;
            }
        """)
        input_container_layout = QHBoxLayout(input_container)
        input_container_layout.setContentsMargins(12, 6, 12, 6)
        input_container_layout.setSpacing(8)

        # 左侧：可点击整体日期显示
        self.date_display_label = ClickableLabel()
        self.update_date_display(self.input_title, self.current_date)
        self.date_display_label.setTextFormat(Qt.RichText)
        self.date_display_label.setCursor(Qt.PointingHandCursor)
        input_container_layout.addWidget(self.date_display_label, stretch=2)

        # 右侧：输入框 + 单位
        percent_input_layout = QHBoxLayout()
        self.percent_input = QLineEdit()
        self.percent_input.setEnabled(False)
        self.percent_input.setStyleSheet("""
            QLineEdit {
                border: none;
                font: 700 16pt "微软雅黑";
                color:blue;
            }
        """)
        self.percent_input.setAlignment(Qt.AlignRight)
        self.percent_label = QLabel(unit)
        self.percent_label.setStyleSheet("font-size: 16px;")
        percent_input_layout.addWidget(self.percent_input)
        percent_input_layout.addWidget(self.percent_label)
        percent_input_layout.setContentsMargins(0, 0, 0, 0)

        percent_frame = QFrame()
        percent_frame.setLayout(percent_input_layout)
        input_container_layout.addWidget(percent_frame, stretch=1)

        self.bg_layout.addWidget(input_container)

        # 数字键盘样式
        button_style = """
            QPushButton {
                background-color: transparent;
                font-size: 20px;
                border-radius: 8px;
                padding: 10px;
                border:none;
            }
            QPushButton:hover {
                background-color: #f2f2f2;
            }
        """

        # 数字键盘布局
        num_button_rows = [
            ["1", "2", "3", "Left"],
            ["4", "5", "6", "Right"],
            ["7", "8", "9", "Ready"],
            [".", "0", "Back", ""]
        ]
        for row in num_button_rows:
            h_layout = QHBoxLayout()
            for button_text in row:
                button = QPushButton(button_text)
                button.setStyleSheet(button_style)
                button.setMinimumHeight(48)
                button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
                button.setCursor(Qt.PointingHandCursor)
                if button_text.isdigit() or button_text == ".":
                    button.clicked.connect(lambda _, text=button_text: self.on_number_click(text))
                elif button_text == "Back":
                    button.clicked.connect(self.on_backspace_click)
                elif button_text == "Ready":
                    button.clicked.connect(self.on_complete_click)
                elif button_text == "":
                    button.setEnabled(False)
                h_layout.addWidget(button)
            self.bg_layout.addLayout(h_layout)

        self.bind()

    def bind(self):
        self.date_display_label.clicked.connect(self.on_date_click)

    def update_date_display(self, input_title, date_text):
        self.date_display_label.setText(
            f'{input_title} &nbsp;&nbsp;<span style="font-size:12px; color:#999999;">{date_text}</span>'
        )

    def add_record(self, date, percent):
        unit = self.percent_label.text()

        # 遍历已有项，检查是否有相同日期，更新文本
        for i in range(self.record_list.count()):
            item = self.record_list.item(i)
            widget = self.record_list.itemWidget(item)
            if widget:
                label = widget.findChild(QLabel)
                if label:
                    # 这里直接用 label.text() 但因格式复杂，不用改动
                    if date in label.text():
                        label.setText(
                            f'<span style="color: #999999; font-size: 13px;">{date}</span> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'
                            f'<span style="color: #000000; font-size: 15px; font-weight: bold;">{percent}{unit}</span>'
                        )
                        return  # 找到就更新后返回

        # 新建item
        item_widget = QWidget()
        layout = QHBoxLayout(item_widget)
        layout.setContentsMargins(8, 4, 8, 4)
        layout.setSpacing(36)

        left_label = QLabel()
        left_label.setTextFormat(Qt.RichText)
        left_label.setText(
            f'<span style="color: #999999; font-size: 13px;">{date}</span> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'
            f'<span style="color: #000000; font-size: 15px; font-weight: bold;">{percent}{unit}</span>'
        )

        delete_button = QPushButton("Delete")
        delete_button.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                font:700 14px "微软雅黑";
                border: none;
            }
        """)

        layout.addWidget(left_label)
        layout.addStretch()
        layout.addWidget(delete_button)

        item = QListWidgetItem()
        item.setSizeHint(item_widget.sizeHint())
        self.record_list.addItem(item)
        self.record_list.setItemWidget(item, item_widget)

        delete_button.clicked.connect(lambda: self.record_list.takeItem(self.record_list.row(item)))

    def on_number_click(self, text):
        current_text = self.percent_input.text()
        self.percent_input.setText(current_text + text)

    def on_backspace_click(self):
        current_text = self.percent_input.text()
        if current_text:
            self.percent_input.setText(current_text[:-1])

    def get_date_text(self):
        # 直接返回成员变量
        return self.current_date

    def on_complete_click(self):
        date = self.get_date_text()
        percent = self.percent_input.text()
        if date and percent:
            self.add_record(date, percent)
            self.percent_input.clear()

            self.save_current_weight_signal.emit(float(percent))

        self.close()

    def resizeEvent(self, event):
        self.bg_frame.setGeometry(0, 0, self.width(), self.height())
        super().resizeEvent(event)

    def on_date_click(self):
        print("日期区域被点击了")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    dialog2 = RecordListDialog(input_title="腰围", unit="cm")
    dialog2.show()

    sys.exit(app.exec())
