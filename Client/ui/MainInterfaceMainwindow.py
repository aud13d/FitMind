from PySide6.QtWidgets import QMainWindow, QButtonGroup, QCalendarWidget
from PySide6.QtCore import QLocale, Qt
from .ui_MainInterface import Ui_MainWindow

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
        self.ui.button_train.clicked.connect(self.move_to_train)
        self.ui.button_sports.clicked.connect(self.move_to_sports)
        self.ui.button_history.clicked.connect(self.move_to_history)
        self.ui.button_user.clicked.connect(self.move_to_user)

    def move_to_train(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def move_to_sports(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def move_to_history(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def move_to_user(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def setup_BottomStatusBar_button_group(self):
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
        self.button_group = QButtonGroup(self)
        self.button_group.setExclusive(True)  # 设置互斥

        self.button_group.addButton(self.ui.button_train_official_plan, 0)
        self.button_group.addButton(self.ui.button_train_personal_plan, 1)

        self.ui.button_train_official_plan.setChecked(True)

    def setup_Train_SonsPlan_button_group(self):
        self.button_group = QButtonGroup(self)
        self.button_group.setExclusive(True)  # 设置互斥

        self.button_group.addButton(self.ui.button_train_plan1, 0)
        self.button_group.addButton(self.ui.button_train_plan2, 1)
        self.button_group.addButton(self.ui.button_train_plan3, 2)
        self.button_group.addButton(self.ui.button_train_plan4, 3)

        self.ui.button_train_plan1.setChecked(True)

    def setup_Histroy_button_group(self):
        self.button_group = QButtonGroup(self)
        self.button_group.addButton(self.ui.button_history_history,0)
        self.button_group.addButton(self.ui.button_history_statistics,1)

        self.ui.button_history_history.setChecked(True)

