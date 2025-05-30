# 在原有代码基础上添加以下内容
from PySide6.QtCore import QRect, QPoint, QSize, Qt, QTimer
from PySide6.QtWidgets import QListWidget, QListWidgetItem, QHBoxLayout, QLabel, QSpacerItem, QSizePolicy, QWidget, \
    QPushButton

from Client.ui.Designer.ui_MealRecord import Ui_Widget_MealRecord
from Client.services.server_meal import MealService


class MealRecordWidget(QWidget, Ui_Widget_MealRecord):
    def __init__(self,parent=None,name=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.label.setText(name)
        # 初始化数据存储
        self.selected_foods = []  # 已选食品列表

        # 初始化UI增强
        self.setup_custom_widgets()
        self.label.setMinimumWidth(150)
        self.bind()

        # 初始化示例数据
        self.init_sample_data()

        # 初始化定时器,两秒后自动查询
        self.is_timer_triggered_search = False
        self.search_timer = QTimer(self)
        self.search_timer.setSingleShot(True)
        self.search_timer.timeout.connect(self.perform_search)

    def setup_custom_widgets(self):
        """初始化自定义控件"""
        # 食品列表弹窗
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
        """连接所有信号"""
        # 页面切换
        self.button_search.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.button_collect.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.button_set.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.button_customize.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))

        # 功能按钮
        # 搜索
        self.lineEdit_foodname.textChanged.connect(self.on_text_changed)
        self.lineEdit_foodname.returnPressed.connect(lambda: self.perform_search(triggered_by_timer=False))
        # 提交
        self.button_confrim.clicked.connect(self.submit_food_list)

        # 搜索功能
        self.lineEdit_foodname.returnPressed.connect(self.perform_search)
        self.button_search.clicked.connect(self.perform_search)

    def init_sample_data(self):
        """初始化示例数据"""
        # 搜索页面
        self.search_list = QListWidget(self.page_search)
        self.search_list.setGeometry(0, 0, 361, 491)
        self.search_list.itemDoubleClicked.connect(self.add_food_item)

        # 收藏页面
        self.collect_list = QListWidget(self.page_collect)
        self.collect_list.setGeometry(0, 0, 361, 491)
        self.collect_list.itemDoubleClicked.connect(self.add_food_item)

        # 初始化示例项
        for i in range(1, 6):
            self.search_list.addItem(f"示例食品 {i} 200g")
            self.collect_list.addItem(f"收藏食品 {i} 150g")

    def toggle_food_list(self):
        """切换食品列表显示"""
        if self.food_list_window.isVisible():
            self.food_list_window.hide()
        else:
            # 计算显示位置
            btn_pos = self.button_list.mapTo(self.frame_center, QPoint(0, 0))
            self.food_list_window.move(btn_pos.x(), btn_pos.y() - 150)
            self.food_list_window.show()
            self.food_list_window.raise_()

    def on_text_changed(self):
        """当输入框文本变化时，2 秒后自动搜索"""
        self.is_timer_triggered_search = True
        self.search_timer.start(2000)  # 重启定时器

    def perform_search(self,triggered_by_timer=True):
        """执行食物搜索"""
        if triggered_by_timer and not self.is_timer_triggered_search:
            # 不是定时器发起的，直接跳过
            return

        self.is_timer_triggered_search = False  # 重置标志

        keyword = self.lineEdit_foodname.text().strip()
        if not keyword:
            return

        self.search_list.clear()
        response = MealService.request_search_food(keyword)

        if response and response.status_code == 200:
            try:
                foods = response.json()
                for item in foods:
                    name = item.get("name", "未知")
                    energy = item.get("energy_kcal")
                    protein = item.get("protein_g")
                    carbs = item.get("carbs_g")
                    fat = item.get("fat_g")

                    # 构造显示字符串，单位是每100g
                    detail_str = f"{name} 100g | 热量: {energy if energy is not None else '--'} kcal | 蛋白质: {protein if protein is not None else '--'} g | 碳水: {carbs if carbs is not None else '--'} g | 脂肪: {fat if fat is not None else '--'} g"

                    self.search_list.addItem(detail_str)
            except Exception as e:
                print(f"解析搜索结果失败：{e}")
                self.search_list.addItem("解析搜索结果失败")
        else:
            self.search_list.addItem("搜索失败或无结果")

    def add_food_item(self, item):
        """添加食品项到列表"""
        food_info = item.text()

        # 创建自定义列表项
        list_item = QListWidgetItem()
        widget = QWidget()
        layout = QHBoxLayout(widget)
        layout.setContentsMargins(10, 5, 10, 5)

        # 解析食品信息
        parts = food_info.split()
        name = " ".join(parts[:-1])
        weight = parts[-1]

        # 添加组件
        layout.addWidget(QLabel(name))
        layout.addWidget(QLabel(weight))

        # 删除按钮
        del_btn = QPushButton("删除")
        del_btn.setFixedSize(60, 25)
        del_btn.setStyleSheet("""
            QPushButton {
                background-color: #ff4444;
                color: white;
                border-radius: 5px;
                font-size: 12px;
            }
            QPushButton:hover {
                background-color: #cc0000;
            }
        """)
        del_btn.clicked.connect(lambda: self.remove_food_item(list_item))

        # 布局管理
        layout.addStretch(1)
        layout.addWidget(del_btn)

        # 设置列表项
        list_item.setSizeHint(QSize(0, 40))  # 固定高度
        self.food_list_window.addItem(list_item)
        self.food_list_window.setItemWidget(list_item, widget)
        self.selected_foods.append(food_info)

        # 自动显示列表
        if not self.food_list_window.isVisible():
            self.toggle_food_list()

    def remove_food_item(self, item):
        """移除食品项"""
        row = self.food_list_window.row(item)
        if row >= 0:
            self.food_list_window.takeItem(row)
            if row < len(self.selected_foods):
                del self.selected_foods[row]

    def submit_food_list(self):
        """提交食品列表"""
        if self.selected_foods:
            print("提交的食品列表：")
            for idx, food in enumerate(self.selected_foods, 1):
                print(f"{idx}. {food}")
            # 清空列表
            self.food_list_window.clear()
            self.selected_foods.clear()
        else:
            print("当前没有选择任何食品")