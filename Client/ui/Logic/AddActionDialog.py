from PIL.ImageQt import QPixmap
from PySide6 import QtCore
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QDialog, QSizePolicy, QVBoxLayout

from Client.ui.Designer.ui_AddAction import Ui_Dialog_add_action
from PySide6.QtCore import Qt, Signal
from Client.config import MoveAddActionQDialog_IconPath, GoAddActionQDialog_IconPath


class AddActionDialog(QDialog, Ui_Dialog_add_action):
    addaction_signal = Signal(str,QIcon)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        icon_pixmap_move = QPixmap(MoveAddActionQDialog_IconPath)
        scaled_pixmap_move = icon_pixmap_move.scaled(32, 32, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        self.label_running_outside_move.setPixmap(scaled_pixmap_move)
        self.label_running_inside_move.setPixmap(scaled_pixmap_move)
        self.label_walk_move.setPixmap(scaled_pixmap_move)
        self.label_riding_move.setPixmap(scaled_pixmap_move)
        self.label_fitness_move.setPixmap(scaled_pixmap_move)
        self.label_jump_rope_move.setPixmap(scaled_pixmap_move)


        icon_pixmap_go = QPixmap(GoAddActionQDialog_IconPath)
        scaled_pixmap_go = icon_pixmap_go.scaled(32, 32, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        self.label_running_outside_go.setPixmap(scaled_pixmap_go)
        self.label_running_inside_go.setPixmap(scaled_pixmap_go)
        self.label_walk_go.setPixmap(scaled_pixmap_go)
        self.label_riding_go.setPixmap(scaled_pixmap_go)
        self.label_fitness_go.setPixmap(scaled_pixmap_go)
        self.label_jump_rope_go.setPixmap(scaled_pixmap_go)

        # 清理并重建 layout
        layout = QVBoxLayout(self.scrollAreaWidgetContents)
        layout.setAlignment(Qt.AlignTop)
        layout.setSpacing(10)  # 控件之间的间距
        layout.setContentsMargins(10,0,10,0)  # 左 10, 上 0, 右 10, 下 0

        # 确保 scrollArea 可以随内容拉伸
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)

        # 按顺序添加控件
        layout.addWidget(self.label_2)
        layout.addWidget(self.frame_running_outside)
        layout.addWidget(self.frame_running_inside)
        layout.addWidget(self.frame_walk)
        layout.addWidget(self.frame_riding)
        layout.addWidget(self.frame_fitness)
        layout.addWidget(self.frame_jump_rope)

        if parent:
            self.setFixedSize(parent.width(),parent.height())
            self.move(parent.x(), parent.y())

        self.bind()

        self.icon_map = {
            "running_outside": self.button_running_outside.icon(),
            "running_inside": self.button_running_inside.icon(),
            "walk": self.button_walk.icon(),
            "riding": self.button_riding.icon(),
            "fitness": self.button_fitness.icon(),
            "jump_rope": self.button_jump_rope.icon()
        }

    def bind(self):
        self.button_running_outside.clicked.connect(lambda: self.add_action("running_outside"))
        self.button_running_inside.clicked.connect(lambda: self.add_action("running_inside"))
        self.button_walk.clicked.connect(lambda: self.add_action("walk"))
        self.button_riding.clicked.connect(lambda: self.add_action("riding"))
        self.button_fitness.clicked.connect(lambda: self.add_action("fitness"))
        self.button_jump_rope.clicked.connect(lambda: self.add_action("jump_rope"))

    def add_action(self, action_name):
        icon=self.icon_map.get(action_name)
        self.addaction_signal.emit(action_name,icon)
        self.accept() # 关闭对话框