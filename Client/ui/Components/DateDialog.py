"""""日期选择弹窗"""""
from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QWidget, QFrame, QDateEdit, QSizePolicy
)
from PySide6.QtCore import Qt, QDate, Signal


class DateDialog(QDialog):

    date_confirmed = Signal(QDate)  # 信号：日期对象

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setup_ui()
        self.setStyleSheet("""
            * {
                font-family: "微软雅黑";
            }
            QFrame#main_frame {
                background-color: white;
                border-radius: 20px;
            }
            QPushButton#btn_back {
                border: none;
                background-color: transparent;
                font-size: 14px;
                color: #555;
                text-align: left;
            }
            QPushButton#btn_back:hover {
                color: #000;
            }
            QLabel#title_label {
                font-weight: bold;
                font-size: 16px;
                color: #333;
            }
            QPushButton#btn_confirm {
                background-color: #3c91e6;
                color: white;
                border-radius: 6px;
                padding: 6px 12px;
                font-weight: bold;
                font-size: 14px;
                border: none;
            }
            QPushButton#btn_confirm:hover {
                background-color: #2d78c5;
            }
            QDateEdit {
                font-size: 14px;
                padding: 4px;
                border: 1px solid #ccc;
                border-radius: 6px;
            }
            QDateEdit::drop-down {
                subcontrol-origin: padding;
                subcontrol-position: top right;
                width: 20px;
                border-left: 1px solid #ccc;
            }
        """)

    def setup_ui(self):
        """设置UI"""
        self.setFixedSize(340, 160)

        self.main_frame = QFrame(self)
        self.main_frame.setObjectName("main_frame")
        self.main_frame.setGeometry(self.rect())

        title_layout = QHBoxLayout()
        # 把上面空白和间距去掉得更紧凑
        title_layout.setContentsMargins(0, 0, 0, 0)
        title_layout.setSpacing(0)  # 比较紧凑的间距

        self.btn_back = QPushButton("返回", self.main_frame)
        self.btn_back.setObjectName("btn_back")
        self.btn_back.setFixedHeight(24)
        self.btn_back.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.btn_back.clicked.connect(self.reject)

        self.label_title = QLabel("选择日期", self.main_frame)
        self.label_title.setObjectName("title_label")
        self.label_title.setAlignment(Qt.AlignCenter)
        self.label_title.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        spacer_right = QWidget(self.main_frame)
        spacer_right.setFixedWidth(20)

        title_layout.addWidget(self.btn_back)
        title_layout.addWidget(self.label_title)
        title_layout.addWidget(spacer_right)

        main_layout = QVBoxLayout(self.main_frame)
        # 主布局边距改小一点，整体更紧凑
        main_layout.setContentsMargins(16, 8, 16, 16)
        main_layout.setSpacing(12)
        main_layout.addLayout(title_layout)

        self.date_edit = QDateEdit(self.main_frame)
        self.date_edit.setCalendarPopup(True)
        self.date_edit.setDate(QDate.currentDate())
        self.date_edit.setDisplayFormat("yyyy-MM-dd")
        main_layout.addWidget(self.date_edit)

        self.btn_confirm = QPushButton("confirm", self.main_frame)
        self.btn_confirm.setObjectName("btn_confirm")
        self.btn_confirm.clicked.connect(self.on_confirm)
        main_layout.addWidget(self.btn_confirm)

    def on_confirm(self):
        """发送提交信号"""
        self.date_confirmed.emit(self.date_edit.date())
        self.accept()
