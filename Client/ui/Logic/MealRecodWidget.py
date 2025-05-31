from PySide6.QtCore import QRect, Qt, QTimer
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QListWidget,  QLabel,  QWidget, \
 QVBoxLayout

from Client.config import FoodQFrame_Mapping
from Client.ui.Components.FoodFrame import FoodFrame
from Client.ui.Components.MaskWidget import MaskWidget
from Client.ui.Components.SelectedFoodListDialog import SelectedFoodListDialog
from Client.ui.Designer.ui_MealRecord import Ui_Widget_MealRecord
from Client.services.server_meal import MealService


class MealRecordWidget(QWidget, Ui_Widget_MealRecord):
    def __init__(self, parent=None, name=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # 已选食物和已选食物清单
        self.selected_foods=[]
        self.food_dialog = SelectedFoodListDialog(parent=self, selected_foods=self.selected_foods)

        self.label.setText(name)

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

    def bind(self):
        self.button_search.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.button_collect.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.button_set.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.button_customize.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))

        # 搜索功能
        self.lineEdit_foodname.textChanged.connect(self.on_text_changed)
        self.lineEdit_foodname.returnPressed.connect(lambda: self.perform_search(triggered_by_timer=False))
        self.lineEdit_foodname.returnPressed.connect(self.perform_search)
        self.button_search.clicked.connect(self.perform_search)

        # 食品清单
        self.button_list.clicked.connect(self.open_selected_food_list)


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

                    card.food_added.connect(self.on_food_added)
                    self.search_result_area.setAlignment(Qt.AlignTop)
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

    def open_selected_food_list(self):
        height_ratio = 0.65
        # 创建遮罩层
        self.mask = MaskWidget(self)
        self.mask.setGeometry(0, 0, self.width(), int(self.height() * height_ratio))
        self.mask.show()

        # 创建食品清单窗口（子窗口）
        self.food_dialog.setFixedSize(self.width(), int(self.height() * height_ratio))

        # 获取弹窗左上角的全局坐标（使其贴近底部）
        local_pos = self.rect().bottomLeft() - self.food_dialog.rect().bottomLeft()
        global_pos = self.mapToGlobal(local_pos)


        self.food_dialog.move(global_pos)

        self.food_dialog.finished.connect(self.mask.close)
        self.food_dialog.exec()

    def on_food_added(self, food_data: dict):
        name = food_data.get("name")

        # 查找是否已存在同名食物
        for existing in self.selected_foods:
            if existing["name"] == name:
                # 更新现有数据
                existing.update(food_data)
                break
        else:
            # 没有重复，才新增
            self.selected_foods.append(food_data)

        self.food_dialog.update_foods(self.selected_foods)

        # 刷新显示
        self.food_dialog.refresh_data()



