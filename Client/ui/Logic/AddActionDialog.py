from PIL.ImageQt import QPixmap
from PySide6 import QtCore
from PySide6.QtWidgets import QDialog, QSizePolicy
from Client.ui.Designer.ui_AddAction import Ui_Dialog_add_action
from PySide6.QtCore import Qt
from Client.config import MoveAddActionQDialog_IconPath, GoAddActionQDialog_IconPath


class AddActionDialog(QDialog, Ui_Dialog_add_action):
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

        layout = self.scrollAreaWidgetContents.layout()
        if layout:
            layout.setAlignment(Qt.AlignTop)
            layout.setSpacing(10)  # 控件之间的间距
            layout.setContentsMargins(0, 0, 0, 0)  # 去掉边距

            #self.scrollAreaWidgetContents.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)

        if parent:
            self.setFixedSize(parent.width(),parent.height())
            self.move(parent.x(), parent.y())
