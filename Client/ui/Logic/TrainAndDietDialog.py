from PySide6 import QtCore
from PySide6.QtWidgets import QDialog
from Client.ui.Designer.ui_TrainAndDiet import Ui_Dialog_TD
from .NewTrainWidget import NewTrainWidget

class TrainAndDietDialog(QDialog,Ui_Dialog_TD):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)  # 加载 UI
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 无边框
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 透明背景
        self.bind()

        if parent:
            self.setFixedWidth(parent.width())  # 宽度等于主窗口
            self.move(parent.x(), parent.y()+100)  # 位置对齐

        self.new_train_widget = None

    def bind(self):
        """ 绑定事件 """
        self.button_new_train.clicked.connect(self.move_new_train)

    def move_new_train(self):
        """ 打开新的训练窗口 """
        self.new_train_widget = NewTrainWidget(self.parent())  # 父窗口是主窗口
        self.new_train_widget.show()

        if self.parent():
            self.parent().set_new_train_widget(self.new_train_widget)

        self.close()  # 关闭自己





