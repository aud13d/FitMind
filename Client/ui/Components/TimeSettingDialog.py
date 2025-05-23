"""“”设置时间的弹窗"""""

from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QPushButton,
    QSlider, QLabel, QSizePolicy, QFrame, QWidget
)
from PySide6.QtCore import Qt, Signal


class TimeSettingDialog(QDialog):
    time_confirmed = Signal(int)  # 信号：分钟数

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("时间设置")
        self.setFixedSize(340, 160)
        self.setWindowFlags(Qt.Dialog | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)

        self.setStyleSheet("""
            * {
                font-family: "微软雅黑";
            }
            QFrame#main_frame {
                background-color: white;
                border-radius: 20px;
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
            QSlider::handle:horizontal {
                background-color: #3c91e6;
                width: 12px;
                margin: -4px 0;
                border-radius: 6px;
            }
            QSlider::groove:horizontal {
                height: 6px;
                background: #ddd;
                border-radius: 3px;
            }
        """)

        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)

        self.frame = QFrame(self)
        self.frame.setObjectName("main_frame")
        frame_layout = QVBoxLayout(self.frame)
        frame_layout.setContentsMargins(16, 16, 16, 16)
        frame_layout.setSpacing(12)

        main_layout.addWidget(self.frame)

        # 顶部水平布局，放返回按钮 + 标题 + 占位
        title_layout = QHBoxLayout()

        self.btn_back = QPushButton("return")
        self.btn_back.setObjectName("btn_back")
        self.btn_back.setFixedHeight(24)
        self.btn_back.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.btn_back.clicked.connect(self.reject)

        spacer_right = QWidget()
        spacer_right.setFixedWidth(20)

        self.label_title = QLabel("time setting")
        self.label_title.setObjectName("title_label")
        self.label_title.setAlignment(Qt.AlignCenter)
        self.label_title.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        title_layout.addWidget(self.btn_back)
        title_layout.addWidget(self.label_title)
        title_layout.addWidget(spacer_right)

        frame_layout.addLayout(title_layout)

        # 滑动条和标签横排布局
        slider_layout = QHBoxLayout()
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(1, 120)
        self.slider.setValue(1)
        self.slider.setFixedHeight(24)

        self.label = QLabel(f"{self.slider.value()}min")
        self.label.setFixedWidth(70)
        self.label.setAlignment(Qt.AlignCenter)

        slider_layout.addWidget(self.slider)
        slider_layout.addWidget(self.label)
        frame_layout.addLayout(slider_layout)

        # 确认按钮
        self.btn_confirm = QPushButton("confirm")
        self.btn_confirm.setObjectName("btn_confirm")
        self.btn_confirm.setFixedHeight(32)
        self.btn_confirm.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        frame_layout.addWidget(self.btn_confirm)

        # 绑定信号
        self.slider.valueChanged.connect(lambda v: self.label.setText(f"{v}min"))
        self.btn_confirm.clicked.connect(self.on_confirm)

    def on_confirm(self):
        self.time_confirmed.emit(self.slider.value())
        self.accept()
