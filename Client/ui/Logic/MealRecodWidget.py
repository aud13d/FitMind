from PySide6.QtCore import QRect, QPoint, QSize, Qt, QTimer
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QListWidget, QListWidgetItem, QHBoxLayout, QLabel, QSpacerItem, QSizePolicy, QWidget, \
    QPushButton, QVBoxLayout, QScrollArea

from Client.config import FoodQFrame_Mapping
from Client.ui.Components.FoodFrame import FoodFrame
from Client.ui.Designer.ui_MealRecord import Ui_Widget_MealRecord
from Client.services.server_meal import MealService


class MealRecordWidget(QWidget, Ui_Widget_MealRecord):
    def __init__(self, parent=None, name=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.label.setText(name)
        self.selected_foods = []

        self.setup_custom_widgets()
        self.label.setMinimumWidth(150)
        self.bind()

        self.is_timer_triggered_search = False
        self.search_timer = QTimer(self)
        self.search_timer.setSingleShot(True)
        self.search_timer.timeout.connect(self.perform_search)

        self.scroll_content = QWidget()
        self.scroll_content_layout = QVBoxLayout(self.scroll_content)
        self.scroll_content_layout.setContentsMargins(10, 10, 10, 10)
        self.scroll_content_layout.setSpacing(10)

        # 把内容容器放入 scrollArea 里
        self.scrollArea.setWidget(self.scroll_content)
        self.scrollArea.setWidgetResizable(True)

        # 把布局引用给后面添加卡片用
        self.search_result_area = self.scroll_content_layout

    def setup_custom_widgets(self):
        self.food_list_window = QListWidget(self.frame_center)
        self.food_list_window.setGeometry(QRect(0, 450, 361, 150))
        self.food_list_window.setStyleSheet("""
            QListWidget {
                background-color: white;
                border: 2px solid #ddd;
                border-radius: 10px;
                padding: 5px;
            }
            QListWidget::item {
                height: 40px;
                border-bottom: 1px solid #eee;
            }
        """)
        self.food_list_window.hide()

    def bind(self):
        self.button_search.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.button_collect.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.button_set.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.button_customize.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))

        self.lineEdit_foodname.textChanged.connect(self.on_text_changed)
        self.lineEdit_foodname.returnPressed.connect(lambda: self.perform_search(triggered_by_timer=False))

        self.lineEdit_foodname.returnPressed.connect(self.perform_search)
        self.button_search.clicked.connect(self.perform_search)

    def on_text_changed(self):
        self.is_timer_triggered_search = True
        self.search_timer.start(2000)

    def perform_search(self, triggered_by_timer=True):
        if triggered_by_timer and not self.is_timer_triggered_search:
            return

        self.is_timer_triggered_search = False

        keyword = self.lineEdit_foodname.text().strip()
        if not keyword:
            return

        for i in reversed(range(self.search_result_area.count())):
            widget = self.search_result_area.itemAt(i).widget()
            if widget:
                widget.setParent(None)

        response = MealService.request_search_food(keyword)

        if response and response.status_code == 200:
            try:
                foods = response.json()
                for item in foods:
                    icon = self.get_icon_by_name(item.get("name", ""))
                    card = FoodFrame(
                        name=item.get("name"),
                        energy=item.get("energy_kcal"),
                        protein=item.get("protein_g"),
                        carbs=item.get("carbs_g"),
                        fat=item.get("fat_g"),
                        icon=icon,
                        parent=self,
                        meal_record_widget=self
                    )
                    self.search_result_area.addWidget(card)
            except Exception as e:
                error_label = QLabel("解析搜索结果失败")
                self.search_result_area.addWidget(error_label)
        else:
            fail_label = QLabel("搜索失败或无结果")
            self.search_result_area.addWidget(fail_label)

    def get_icon_by_name(self,food_name: str) -> QIcon:
        name_lower = food_name.lower()
        for keyword, icon_path in FoodQFrame_Mapping.items():
            if keyword.lower() in name_lower:
                return QIcon(icon_path)
        return QIcon("icons/default.png")  # 没找到就用默认图标
