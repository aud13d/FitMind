from PySide6.QtWidgets import QMainWindow, QButtonGroup, QCalendarWidget, QPushButton
from PySide6.QtCore import QLocale, Qt
from Client.ui.Designer.ui_MainInterface import Ui_MainWindow
from .MealRecodWidget import MealRecordWidget
from .TrainAndDietDialog import TrainAndDietDialog
from Client.ui.Components.MaskWidget import MaskWidget
from Client.cache.user_bodydata import UserBodyData
from Client.cache.user_session import UserSession
from Client.ui.Logic.DietInterfaceWidget import DietInterfaceWidget
from Client.ui.Components.DringkingListDialog import DrinkingListDialog


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

        # 创建悬浮按钮(用于返回最小化的NewTrainWidget窗口)
        self.new_train_widget_mini_floating_button = self.create_new_train_widget_mini_floating_button()
        self.new_train_widget_mini_floating_button.setVisible(False)  # 默认隐藏
        self.new_train_widget = None

        self.bind()


    def create_new_train_widget_mini_floating_button(self):
        """创建悬浮按钮并返回"""
        button = QPushButton("Training in progress", self)
        button.setFixedSize(100, 40)
        button.move(self.width() - 120, self.height() - 130)  # 调整位置
        button.setStyleSheet(
            "background-color: rgba(0, 0, 255, 100); color: white; border-radius: 10px; font-size: 11px;"
        )
        return button

    def bind(self):
        """信号与槽的连接"""
        #界面切换
        self.ui.button_train.clicked.connect(self.move_to_train)
        self.ui.button_sports.clicked.connect(self.move_to_sports)
        self.ui.button_history.clicked.connect(self.move_to_history)
        self.ui.button_user.clicked.connect(self.move_to_user)
        self.new_train_widget_mini_floating_button.clicked.connect(self.restore_NewTrain)

        #打开训练/饮食窗口
        self.ui.button_TrainAndDiet.clicked.connect(self.open_TrainAndDiet)
        #打开饮食界面
        self.ui.frame_dietRecord.clicked.connect(self.open_DietInterface)
        self.ui.button_train_drink.clicked.connect(self.open_DrinkingList)
        self.ui.button_train_breakfast.clicked.connect(self.open_BreakfastList)
        self.ui.button_train_lunch.clicked.connect(self.open_LunchList)
        self.ui.button_train_dinner.clicked.connect(self.open_DinnerList)



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

    def open_DietInterface(self):
        """打开饮食记录窗口"""
        self.add_meal_widget = DietInterfaceWidget(self)
        self.add_meal_widget.show()

    def open_DrinkingList(self):
        """打开喝水记录窗口（先打开饮食记录，然后打开喝水记录）"""
        self.add_meal_widget = DietInterfaceWidget(self)
        self.add_meal_widget.show()
        self.add_meal_widget.ui.button_diet_drink.clicked.emit()

    def open_BreakfastList(self):
        """打开饮食记录窗口"""
        self.add_meal_widget = DietInterfaceWidget(self)
        self.add_meal_widget.show()

        self.add_meal_widget.ui.button_diet_breakfast.clicked.emit()

    def open_LunchList(self):
        """打开饮食记录窗口"""
        self.add_meal_widget = DietInterfaceWidget(self)
        self.add_meal_widget.show()

        self.add_meal_widget.ui.button_diet_lunch.clicked.emit()

    def open_DinnerList(self):
        """打开饮食记录窗口"""
        self.add_meal_widget = DietInterfaceWidget(self)
        self.add_meal_widget.show()

        self.add_meal_widget.ui.button_diet_dinner.clicked.emit()




    def set_new_train_widget(self, widget):
        """保存 NewTrainWidget 引用并监听最小化"""
        self.new_train_widget = widget
        self.new_train_widget.minimized_signal.connect(self.show_floating_button)  # 监听最小化

    def show_floating_button(self):
        """显示悬浮按钮"""
        if not self.new_train_widget:
            self.new_train_widget_mini_floating_button.setVisible(False)
            return

        self.new_train_widget_mini_floating_button.setText("Training in progress")
        self.new_train_widget_mini_floating_button.setVisible(True)
        self.new_train_widget_mini_floating_button.raise_()  # 确保悬浮按钮在最上层

    def restore_NewTrain(self):
        """恢复 NewTrainWidget"""
        if self.new_train_widget:
            self.new_train_widget.showNormal()
            self.new_train_widget.raise_()
            self.new_train_widget_mini_floating_button.setVisible(False)

    def closeEvent(self, event):
        """当主窗口关闭时触发"""
        UserBodyData.clear()
        UserSession.clear()
        print("用户缓存已清空")
        super().closeEvent(event)





