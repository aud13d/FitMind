from PySide6.QtWidgets import (
    QLabel, QDialog, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton,
    QSpacerItem, QSizePolicy, QFrame, QGridLayout
)
from PySide6.QtCore import Qt, QSize, Signal
from PySide6.QtGui import QPixmap, QIcon, QPainter, QPainterPath, QIntValidator


class FoodListDialog(QDialog):
    food_added = Signal(dict)
    def __init__(self, parent=None, food_data=None):
        super().__init__(parent)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Dialog)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.setFixedSize(362, 700)
        if parent:
            self.move(parent.mapToGlobal(parent.rect().topLeft()))

        self.food_data = food_data or {}

        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)  # 无边距

        self.frame = QFrame(self)
        self.frame.setStyleSheet("""
            QFrame {
                background-color: white;
                border-radius: 20px;
            }
        """)
        self.frame_layout = QVBoxLayout(self.frame)
        self.frame_layout.setContentsMargins(15, 15, 15, 15)  # 内边距，保证内容不贴边

        # 返回按钮
        self.button_return = QPushButton("Back")
        self.button_return.setStyleSheet("font:700 12pt '微软雅黑'; color: rgb(12, 12, 255); background: transparent;")
        self.button_return.setFixedHeight(30)
        self.button_return.clicked.connect(self.close)
        self.frame_layout.addWidget(self.button_return, alignment=Qt.AlignRight)

        # 1. 图标 + 名字（紧凑）
        icon = QLabel()
        icon.setFixedSize(36, 36)
        food_icon = self.food_data.get("icon", QIcon())
        if food_icon:
            raw_pixmap = food_icon.pixmap(36, 36)
            # 创建一个圆形遮罩的图
            rounded = QPixmap(36, 36)
            rounded.fill(Qt.transparent)

            painter = QPainter(rounded)
            painter.setRenderHint(QPainter.Antialiasing)
            path = QPainterPath()
            path.addEllipse(0, 0, 36, 36)
            painter.setClipPath(path)
            painter.drawPixmap(0, 0, raw_pixmap)
            painter.end()

            icon.setPixmap(rounded)
        else:
            icon.setStyleSheet("background-color: #ccc; border-radius: 18px;")

        name_label = QLabel(f"<b>{self.food_data.get('name', 'Food')}</b>")
        name_label.setStyleSheet("font-size: 14px;")
        name_label.setWordWrap(True)  # 自动换行
        name_label.setFixedWidth(300)  # 限制宽度，控制换行，具体宽度可调
        name_label.setMaximumHeight(50)

        top_row = QHBoxLayout()
        top_row.setSpacing(5)
        top_row.addWidget(icon)
        top_row.addWidget(name_label)
        top_row.addStretch()
        self.frame_layout.addLayout(top_row)

        # 2. 当前重量和营养信息（缩小字体和高度）
        self.weight = 100
        self.energy = self.food_data.get("energy", 0)
        self.protein = self.food_data.get("protein", 0)
        self.carbs = self.food_data.get("carbs", 0)
        self.fat = self.food_data.get("fat", 0)

        self.weight_label = QLabel(f"{self.weight} g")
        self.weight_label.setStyleSheet("font-size: 11px;")
        self.weight_label.setFixedHeight(20)

        self.kcal_label = QLabel()
        self.kcal_label.setStyleSheet("font-size: 11px;")
        self.kcal_label.setFixedHeight(20)

        self.nutrition_label = QLabel()
        self.nutrition_label.setStyleSheet("font-size: 11px;")
        self.nutrition_label.setFixedHeight(20)

        nutrition_row = QHBoxLayout()
        nutrition_row.addWidget(self.weight_label)
        nutrition_row.addSpacing(8)
        nutrition_row.addWidget(self.kcal_label)
        nutrition_row.addStretch()
        nutrition_row.addWidget(self.nutrition_label)
        self.frame_layout.addLayout(nutrition_row)

        # 3. 输入框 + 单位标签
        input_row = QHBoxLayout()

        # 左边空白占位
        input_row.addSpacerItem(QSpacerItem(40, 10, QSizePolicy.Expanding, QSizePolicy.Minimum))

        self.input_edit = QLineEdit("100")
        self.input_edit.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.input_edit.setFixedHeight(35)
        self.input_edit.setMaximumWidth(100)  # 限制宽度
        self.input_edit.setReadOnly(True)  # 禁止输入
        self.input_edit.setValidator(QIntValidator(0, 9999, self))  # 设置最大值
        self.input_edit.setStyleSheet("""
            QLineEdit {
                border: none;
                border-bottom: 2px solid rgb(0, 38, 255);
                font-size: 20px;
                color: rgb(0, 38, 255);
                padding-right: 10px;
            }
        """)

        unit_label = QLabel("g")
        unit_label.setStyleSheet("font-size: 16px; color: rgb(0, 38, 255);")

        input_row.addWidget(self.input_edit)
        input_row.addWidget(unit_label)

        # 右边空白占位
        input_row.addSpacerItem(QSpacerItem(40, 10, QSizePolicy.Expanding, QSizePolicy.Minimum))

        self.frame_layout.addLayout(input_row)

        # 4. 数字键盘输入区域
        self.frame_input = QFrame(self.frame)
        self.frame_input.setStyleSheet("""
            QPushButton {
                background-color: white;
                font-size: 20px;
                border-radius: 8px;
                padding: 10px;
                border: none;
            }
            QPushButton:hover {
                background-color: #f0f0f0;
                padding-bottom: 2px;
            }
            QPushButton:pressed {
                background-color: #e0e0e0;
                padding-bottom: 1px;
            }
            QPushButton:disabled {
                background-color: #f8f8f8;
                color: gray;
                border-color: #ddd;
            }
        """)
        self.gridLayout = QGridLayout(self.frame_input)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(5)

        for row_values in (["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"], ["0", ".", "back"]):
            row = QHBoxLayout()
            row.setSpacing(5)
            for text in row_values:
                btn = QPushButton(text, self.frame_input)
                btn.setMinimumSize(QSize(80, 45))
                btn.clicked.connect(self.handle_keypad_button)
                row.addWidget(btn)
            self.verticalLayout.addLayout(row)

        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.frame_layout.addWidget(self.frame_input)

        # 5. 添加食物按钮
        self.button_add = QPushButton("Add Food")
        self.button_add.clicked.connect(self.emit_food_data)
        self.button_add.setMinimumSize(QSize(0,60))
        self.button_add.setStyleSheet("""
                QPushButton{
                    font: 700 10pt "微软雅黑";
                    background-color:rgb(0, 85, 255);
                    color:white;
                    border-radius:10px;
                    margin-top:15px;
                    margin-bottom:15px;
                    padding-left:10px;
                    padding-right:10px;
                }
        """)
        self.frame_layout.addWidget(self.button_add, alignment=Qt.AlignHCenter | Qt.AlignVCenter)

        self.main_layout.addWidget(self.frame)

        self.update_nutrition_display()

    def update_nutrition_display(self):
        try:
            weight = float(self.input_edit.text())
        except ValueError:
            weight = 0
        self.weight_label.setText(f"{weight} g")
        if self.energy:
            kcal = round(self.energy * weight / 100, 1)
        else:
            kcal = "--"
        protein = round(self.protein * weight / 100, 1)
        carbs = round(self.carbs * weight / 100, 1)
        fat = round(self.fat * weight / 100, 1)

        self.kcal_label.setText(f"{kcal} kcal")
        self.nutrition_label.setText(
            f"<span style='color:#FFD700;'>P {protein}</span>&nbsp;&nbsp;"
            f"<span style='color:#1E90FF;'>C {carbs}</span>&nbsp;&nbsp;"
            f"<span style='color:#FF6347;'>F {fat}</span>"
        )

    def handle_keypad_button(self):
        btn = self.sender()
        if not btn:
            return
        text = btn.text()
        cur_text = self.input_edit.text()

        if text == "back":
            new_text = cur_text[:-1]
        else:
            if text == "." and "." in cur_text:
                return
            new_text = cur_text + text

        # 合法性检查
        try:
            if new_text and new_text != ".":
                value = float(new_text)
                if value > 9999.00:
                    value = 9999.00
                    new_text = "9999.00"
                else:
                    # 限制小数点后最多两位
                    if "." in new_text:
                        int_part, dec_part = new_text.split(".", 1)
                        dec_part = dec_part[:2]  # 取最多两位
                        new_text = int_part + "." + dec_part
        except ValueError:
            return

        self.input_edit.setText(new_text)
        self.update_nutrition_display()

    def emit_food_data(self):
        try:
            weight = float(self.input_edit.text())
        except ValueError:
            weight = 0.0

        kcal = round(self.energy * weight / 100, 1)
        protein = round(self.protein * weight / 100, 1)
        carbs = round(self.carbs * weight / 100, 1)
        fat = round(self.fat * weight / 100, 1)

        data = {
            "name": self.food_data.get("name", "Food"),
            "icon": self.food_data.get("icon"),
            "weight": weight,
            "energy": kcal,
            "protein": protein,
            "carbs": carbs,
            "fat": fat,
        }

        self.food_added.emit(data)
        self.accept()  # 关闭对话框





