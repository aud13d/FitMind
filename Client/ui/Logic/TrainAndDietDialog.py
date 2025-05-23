from PySide6 import QtCore
from PySide6.QtWidgets import QDialog
from Client.ui.Designer.ui_TrainAndDiet import Ui_Dialog_TD
from .NewTrainWidget import NewTrainWidget
from .NewAerobicDialog import NewAerobicDialog
from .NewRestDialog import NewRestDialog
from .BodyDataWidget import BodyDataWidget

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
        self.new_aerobic_widget = None
        self.new_rest_widget = None

    def bind(self):
        """ 绑定事件 """
        self.button_new_train.clicked.connect(self.move_new_train)
        self.button_new_aerobic.clicked.connect(self.move_new_aerobic)
        self.button_new_rest.clicked.connect(self.move_new_rest)
        self.button_body_data.clicked.connect(self.move_body_data)

    def move_new_train(self):
        """ 打开新的训练窗口 """
        self.new_train_widget = NewTrainWidget(self.parent())  # 父窗口是主窗口
        self.new_train_widget.show()

        if self.parent():
            self.parent().set_new_train_widget(self.new_train_widget)

        self.close()  # 关闭自己

    def move_new_aerobic(self):
        """ 打开新的有氧界面 """
        self.new_aerobic_widget = NewAerobicDialog(self.parent())
        self.new_aerobic_widget.show()

        self.close()

    def move_new_rest(self):
        """ 打开新的休息界面 """
        self.new_rest_widget = NewRestDialog(self.parent())
        self.new_rest_widget.show()

        self.close()

    def move_body_data(self):
        """ 打开身体数据界面 """
        self.body_data_widget = BodyDataWidget(self.parent())
        self.body_data_widget.show()

        self.close()



