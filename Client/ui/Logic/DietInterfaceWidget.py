from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget
from Client.ui.Designer.ui_DietInterface import Ui_Widget_DietInterface
from Client.ui.Components.DringkingListDialog import DrinkingListDialog
from Client.ui.Logic.DietaryStatisticsWidget import DietaryStatisticsWidget
from Client.ui.Logic.MealRecodWidget import MealRecordWidget


class DietInterfaceWidget(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget_DietInterface()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.bind()

    def bind(self):
        self.ui.button_diet_drink.clicked.connect(self.open_drinking_record)
        self.ui.button_diet_statistics.clicked.connect(self.open_diet_statistics)
        self.ui.button_diet_breakfast.clicked.connect(self.open_meal_record)
        self.ui.button_diet_lunch.clicked.connect(self.open_meal_record)
        self.ui.button_diet_dinner.clicked.connect(self.open_meal_record)

    def open_drinking_record(self):
        self.dialog = DrinkingListDialog(self)
        self.dialog.setModal(True)

        self.dialog.exec()

    def open_diet_statistics(self) :
        self.diet_statistics = DietaryStatisticsWidget(self)
        self.diet_statistics.show()

    def open_meal_record(self):
        def open_meal_record_for(name):
            self.meal = MealRecordWidget(self,name)
            self.meal.show()

        if self.sender() == self.ui.button_diet_breakfast:
            open_meal_record_for("Breakfast Record")
        elif self.sender() == self.ui.button_diet_lunch:
            open_meal_record_for("Lunch Record")
        elif self.sender() == self.ui.button_diet_dinner:
            open_meal_record_for("Dinner Record")





