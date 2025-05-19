from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QPushButton,
    QSlider, QLabel, QButtonGroup, QSizePolicy, QWidget, QFrame
)
from PySide6.QtCore import Qt, Signal


class TypeSelectionDialog(QDialog):
    type_confirmed = Signal(str, int)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Select Type")
        self.setFixedSize(340, 160)
        self.setWindowFlags(Qt.Dialog | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)

        self.setStyleSheet("""
            * {
                font-family: "Microsoft YaHei";
            }
            QFrame#main_frame {
                background-color: white;
                border-radius: 20px;
            }
            QPushButton[typeButton="true"] {
                background-color: transparent;
                color: #333;
                border: none;
                padding: 6px 10px;
                font-size: 14px;
            }
            QPushButton[typeButton="true"]:checked {
                background-color: #3c91e6;
                color: white;
                border-radius: 8px;
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

        # 最外层布局，装QFrame
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        # 白底圆角QFrame
        self.frame = QFrame(self)
        self.frame.setObjectName("main_frame")

        # QFrame内部布局
        frame_layout = QVBoxLayout(self.frame)
        frame_layout.setSpacing(12)
        frame_layout.setContentsMargins(16, 16, 16, 16)

        layout.addWidget(self.frame)

        # 顶部布局：返回按钮 + 标题 + 右侧占位
        title_layout = QHBoxLayout()
        self.btn_back = QPushButton("Return")
        self.btn_back.setObjectName("btn_back")
        self.btn_back.setFixedHeight(24)
        self.btn_back.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.btn_back.clicked.connect(self.reject)

        spacer_right = QWidget()
        spacer_right.setFixedWidth(20)

        self.label_title = QLabel("type selection")
        self.label_title.setObjectName("title_label")
        self.label_title.setAlignment(Qt.AlignCenter)
        self.label_title.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        title_layout.addWidget(self.btn_back)
        title_layout.addWidget(self.label_title)
        title_layout.addWidget(spacer_right)

        frame_layout.addLayout(title_layout)

        # 类型选择按钮横排
        self.btn_uniform = QPushButton("Uniform Aerobic")
        self.btn_variable = QPushButton("Variable Speed")
        for btn in (self.btn_uniform, self.btn_variable):
            btn.setCheckable(True)
            btn.setProperty("typeButton", "true")
        self.btn_uniform.setChecked(True)

        btn_group = QButtonGroup(self)
        btn_group.setExclusive(True)
        btn_group.addButton(self.btn_uniform)
        btn_group.addButton(self.btn_variable)

        btn_layout = QHBoxLayout()
        btn_layout.setSpacing(10)
        btn_layout.addWidget(self.btn_uniform)
        btn_layout.addWidget(self.btn_variable)
        frame_layout.addLayout(btn_layout)

        # 滑动条及显示标签（初始隐藏）
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(5, 60)
        self.slider.setSingleStep(5)
        self.slider.setValue(5)
        self.slider.setVisible(False)

        self.slider_label = QLabel("5s")
        self.slider_label.setVisible(False)

        frame_layout.addWidget(self.slider)
        frame_layout.addWidget(self.slider_label)

        # 确认按钮
        self.btn_confirm = QPushButton("Confirm")
        self.btn_confirm.setObjectName("btn_confirm")
        frame_layout.addStretch()
        frame_layout.addWidget(self.btn_confirm)

        # 信号绑定
        self.btn_variable.toggled.connect(self.on_mode_toggle)
        self.slider.valueChanged.connect(lambda v: self.slider_label.setText(f"{v}s"))
        self.btn_confirm.clicked.connect(self.on_confirm)

    def on_mode_toggle(self, checked):
        if checked:
            self.slider.setVisible(True)
            self.slider_label.setVisible(True)
            self.setFixedSize(340, 240)
        else:
            self.slider.setVisible(False)
            self.slider_label.setVisible(False)
            self.setFixedSize(340, 160)

    def on_confirm(self):
        if self.btn_uniform.isChecked():
            self.type_confirmed.emit("匀速有氧", 0)
        else:
            seconds = self.slider.value()
            self.type_confirmed.emit("变速有氧", seconds)
        self.accept()
