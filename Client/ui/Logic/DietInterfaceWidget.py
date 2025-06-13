from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget
from Client.ui.Designer.ui_DietInterface import Ui_Widget_DietInterface
from Client.ui.Components.DringkingListDialog import DrinkingListDialog
from Client.ui.Logic.DietaryStatisticsWidget import DietaryStatisticsWidget
from Client.ui.Logic.MealRecodWidget import MealRecordWidget
from Client.cache.user_dietdata import UserDietData


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
            self.meal.meal_add_signal.connect(self.handle_meal_add)

        if self.sender() == self.ui.button_diet_breakfast:
            open_meal_record_for("Breakfast Record")
        elif self.sender() == self.ui.button_diet_lunch:
            open_meal_record_for("Lunch Record")
        elif self.sender() == self.ui.button_diet_dinner:
            open_meal_record_for("Dinner Record")

    def update_summary_display(self):
        from Client.cache.user_dietdata import UserDietData
        summary = UserDietData.get_summary()

        # 目标值
        target_protein = 19
        target_carbs = 212
        target_fat = 20
        target_drinks = 1000
        target_energy = 1104

        protein = round(summary["protein"])
        carbs = round(summary["carbs"])
        fat = round(summary["fat"])
        drinks = round(summary["drinks"])
        energy = round(summary["energy"])

        def format_label(name, unit, value, target):
            percent = round(value / target * 100) if target > 0 else 0
            return f"{name}({unit})\n{value}/{target}\n{percent}%"

        self.ui.label_diet_energy.setText(f"{energy}/ Target {target_energy} kcal")
        self.ui.label_diet_protein.setText(format_label("Pro", "g", protein, target_protein))
        self.ui.label_diet_carbohydrate.setText(format_label("Carb", "g", carbs, target_carbs))
        self.ui.label_diet_fat.setText(format_label("Fat", "g", fat, target_fat))
        self.ui.label_diet_water.setText(format_label("Drink", "ml", drinks, target_drinks))

    def handle_meal_add(self, meal_name, meal):
        name_map = {
            "Breakfast Record": "Breakfast",
            "Lunch Record": "Lunch",
            "Dinner Record": "Dinner"
        }
        real_meal_name = name_map.get(meal_name, meal_name)

        for item in meal:
            UserDietData.update(item)
        self.update_summary_display()










