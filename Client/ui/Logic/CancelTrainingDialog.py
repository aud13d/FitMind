from PySide6 import QtCore
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QDialog
from Client.ui.Designer.ui_CancelTraining import Ui_Dialog_cancel_training
from Client.config import CancelTrainingQDialog_IconPath
from ..res_rc import *


class CancelTrainingDialog(QDialog, Ui_Dialog_cancel_training):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        icon_pixmap = QPixmap(CancelTrainingQDialog_IconPath)
        scaled_pixmap = icon_pixmap.scaled(86, 86, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        self.label_cancel_icon.setPixmap(scaled_pixmap)
        self.label_cancel_icon.setAlignment(QtCore.Qt.AlignCenter)

        self.bind()

        if parent:
            # 获取父级的左上角全局坐标
            parent_top_left = parent.mapToGlobal(QtCore.QPoint(0, 0))

            parent_width = parent.width()
            parent_height = parent.height()
            dialog_width = self.width()
            dialog_height = self.height()

            # 计算中心位置
            center_x = parent_top_left.x() + (parent_width - dialog_width) // 2
            center_y = parent_top_left.y() + (parent_height - dialog_height) // 2

            self.move(center_x, center_y)

        self.new_train_widget = None


    def bind(self):
        """绑定事件"""
        self.button_cancel_training.clicked.connect(self.handle_cancel_clicked)
        self.button_cancel.clicked.connect(self.close)

    def handle_cancel_clicked(self):
        """点击了取消按钮"""
        parent_widget = self.parent()  # 获取 NewTrainWidget

        if parent_widget:
            parent_widget.stop_timer()  # 停止计时
            parent_widget.close()  # 关闭 NewTrainWidget
        self.accept()  # 关闭对话框



