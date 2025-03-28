from PySide6.QtWidgets import QMainWindow, QButtonGroup, QCalendarWidget
from PySide6.QtCore import QLocale, Qt
from .ui_MainInterface import Ui_MainWindow
from .TrainAndDietDialog import TrainAndDietDialog
from .MaskWidget import MaskWidget

class MainInterfaceWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.setup_BottomStatusBar_button_group()
        self.setup_Train_ParentPlan_button_group()
        self.setup_Train_SonsPlan_button_group()
        self.setup_Histroy_button_group()

        self.ui.calendarWidget.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)

        # 设置语言为英语
        self.ui.calendarWidget.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        # 设置星期栏显示为简短的星期格式
        self.ui.calendarWidget.setFirstDayOfWeek(Qt.Monday)

        self.bind()

    def bind(self):
        """信号与槽的连接"""
        #界面切换
        self.ui.button_train.clicked.connect(self.move_to_train)
        self.ui.button_sports.clicked.connect(self.move_to_sports)
        self.ui.button_history.clicked.connect(self.move_to_history)
        self.ui.button_user.clicked.connect(self.move_to_user)

        #打开训练/饮食窗口
        self.ui.button_TrainAndDiet.clicked.connect(self.open_TrainAndDiet)

    def move_to_train(self):
        """切换到训练界面"""
        self.ui.stackedWidget.setCurrentIndex(0)

    def move_to_sports(self):
        """切换到运动界面"""
        self.ui.stackedWidget.setCurrentIndex(1)

    def move_to_history(self):
        """切换到历史界面"""
        self.ui.stackedWidget.setCurrentIndex(2)

    def move_to_user(self):
        """切换到个人信息界面"""
        self.ui.stackedWidget.setCurrentIndex(3)

    def setup_BottomStatusBar_button_group(self):
        """设置底部状态栏按钮组"""
        self.button_group = QButtonGroup(self)
        self.button_group.setExclusive(True)  # 设置互斥

        # 将4个ToolButton加入按钮组
        self.button_group.addButton(self.ui.button_train, 0)
        self.button_group.addButton(self.ui.button_sports, 1)
        self.button_group.addButton(self.ui.button_history, 2)
        self.button_group.addButton(self.ui.button_user, 3)

        # 设置默认选中按钮（比如第一个）
        self.ui.button_train.setChecked(True)

    def setup_Train_ParentPlan_button_group(self):
        """设置训练计划按钮组"""
        self.button_group = QButtonGroup(self)
        self.button_group.setExclusive(True)  # 设置互斥

        self.button_group.addButton(self.ui.button_train_official_plan, 0)
        self.button_group.addButton(self.ui.button_train_personal_plan, 1)

        self.ui.button_train_official_plan.setChecked(True)

    def setup_Train_SonsPlan_button_group(self):
        """设置训练计划子按钮组"""
        self.button_group = QButtonGroup(self)
        self.button_group.setExclusive(True)  # 设置互斥

        self.button_group.addButton(self.ui.button_train_plan1, 0)
        self.button_group.addButton(self.ui.button_train_plan2, 1)
        self.button_group.addButton(self.ui.button_train_plan3, 2)
        self.button_group.addButton(self.ui.button_train_plan4, 3)

        self.ui.button_train_plan1.setChecked(True)

    def setup_Histroy_button_group(self):
        """设置历史记录按钮组"""
        self.button_group = QButtonGroup(self)
        self.button_group.addButton(self.ui.button_history_history,0)
        self.button_group.addButton(self.ui.button_history_statistics,1)

        self.ui.button_history_history.setChecked(True)

    def open_TrainAndDiet(self):
        """打开训练/饮食窗口"""
        # 创建遮罩层
        self.mask = MaskWidget(self)
        self.mask.show()  # 显示遮罩层

        # 创建并显示对话框
        self.dialog = TrainAndDietDialog(self)
        self.dialog.setModal(True)
        self.dialog.show()
        self.dialog.raise_()  # 确保对话框在遮罩层之上
        self.dialog.exec_()  # 运行对话框

        # 关闭遮罩层
        self.mask.close()

