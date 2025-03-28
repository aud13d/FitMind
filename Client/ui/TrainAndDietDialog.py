from PySide6 import QtCore
from PySide6.QtWidgets import QDialog
from .ui_TrainAndDiet import Ui_Dialog_TD  # 这里导入上一步生成的 UI 文件

class TrainAndDietDialog(QDialog, Ui_Dialog_TD):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)  # 加载 UI
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 无边框
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 透明背景

        if parent:
            self.setFixedWidth(parent.width())  # 宽度等于主窗口
            self.move(parent.x(), parent.y() + 100)  # 位置对齐（适当调整 Y 轴）
