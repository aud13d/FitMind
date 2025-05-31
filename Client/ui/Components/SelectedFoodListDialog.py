from PySide6.QtCore import Qt
from Client.ui.Components.FoodFrame import FoodFrame
from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QScrollArea, QWidget


class SelectedFoodListDialog(QDialog):
    def __init__(self, selected_foods: list[dict] = None, parent=None):
        super().__init__(parent)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Dialog)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setFixedSize(400, 500)

        self.selected_foods = selected_foods or []

        self.setStyleSheet("background-color: white; border-radius: 16px;")

        # 主 layout
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(10)

        # 滚动区域
        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.scroll.setStyleSheet("border: none;")

        # 滚动内容和布局
        self.scroll_content = QWidget()
        self.scroll_layout = QVBoxLayout(self.scroll_content)
        self.scroll_layout.setSpacing(12)

        self.scroll.setWidget(self.scroll_content)
        self.main_layout.addWidget(self.scroll)

        # 初始化内容
        self.refresh_data()

    def refresh_data(self):
        # 清除旧组件
        layout = self.scroll_layout
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

        # 重新添加
        if not self.selected_foods:
            empty_label = QLabel("No food has been selected yet~")
            empty_label.setAlignment(Qt.AlignCenter)
            layout.addWidget(empty_label)
        else:
            layout.setAlignment(Qt.AlignTop)
            for food in self.selected_foods:
                frame = FoodFrame(
                    name=food.get("name"),
                    icon = food.get("icon"),
                    weight=food.get("weight"),
                    energy=food.get("energy"),
                    protein=food.get("protein"),
                    carbs=food.get("carbs"),
                    fat=food.get("fat")
                )
                layout.addWidget(frame)

    def update_foods(self, selected_foods: list[dict]):
        self.selected_foods = selected_foods
        self.refresh_data()
