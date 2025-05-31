from PIL.ImageQt import QPixmap
from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter, QPainterPath
from PySide6.QtWidgets import QHBoxLayout, QLabel, QVBoxLayout

from Client.ui.Components.ClickableFrame import ClickableFrame
from Client.ui.Components.FoodListDialog import FoodListDialog
from Client.ui.Components.MaskWidget import MaskWidget


class FoodFrame(ClickableFrame):
    def __init__(self, name, energy, protein, carbs, fat, icon=None, parent=None,meal_record_widget=None):
        super().__init__(parent)
        self.meal_record_widget = meal_record_widget
        self.setStyleSheet("""
            ClickableFrame {
                background-color: white;
                border-radius: 15px;
                border: 1px solid #ddd;
            }
        """)
        self.setMinimumHeight(65)
        self.setMinimumWidth(335)

        layout = QHBoxLayout(self)
        layout.setContentsMargins(10, 5, 10, 5)

        icon_label = QLabel()
        icon_label.setFixedSize(36, 36)
        if icon:
            raw_pixmap = icon.pixmap(36, 36)

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

            icon_label.setPixmap(rounded)
        else:
            icon_label.setStyleSheet("background-color: #ccc; border-radius: 18px;")

        text_layout = QVBoxLayout()
        # 构建左边的食物名称 + kcal 热量
        name_label = QLabel(f"<b>{name}</b>")

        kcal_label = QLabel(f"{energy if energy is not None else '--'} kcal / 100g")
        kcal_label.setStyleSheet("font-size: 11px; color: #666;")

        # 构建右边的营养素彩色数据
        nutrient_label = QLabel()
        nutrient_label.setStyleSheet("font-size: 11px;")
        nutrient_label.setText(
            f"<span style='color:#FFD700;'>P {protein or 0}</span>&nbsp;<span style='color:#e5e5e5;'>|</span>&nbsp;"
            f"<span style='color:#1E90FF;'>C {carbs or 0}</span>&nbsp;<span style='color:#e5e5e5;'>|</span>&nbsp;"
            f"<span style='color:#FF6347;'>F {fat or 0}</span>"
        )

        # 横向排布：kcal + 彩色数据
        row_layout = QHBoxLayout()
        row_layout.addWidget(kcal_label)
        row_layout.addStretch()
        row_layout.addWidget(nutrient_label)

        # 再放到主文本布局中
        text_layout = QVBoxLayout()
        text_layout.addWidget(name_label)
        text_layout.addLayout(row_layout)

        # 最终添加到主 layout 中
        layout.addWidget(icon_label)
        layout.addLayout(text_layout)

        self.food_data = {
            "name": name,
            "energy": energy,
            "protein": protein,
            "carbs": carbs,
            "fat": fat,
            "icon": icon,
        }

        self.bind()

    def bind(self):
        self.clicked.connect(self.open_food_list_dialog)

    def open_food_list_dialog(self):
        if not self.meal_record_widget:
            return

        parent_size = self.meal_record_widget.size()
        height_ratio = 0.65  # 调整成65%高度

        # 创建遮罩层
        mask = MaskWidget(self.meal_record_widget)
        mask.setGeometry(0, 0, parent_size.width(), int(parent_size.height() * height_ratio))
        mask.show()

        dialog = FoodListDialog(self.meal_record_widget, self.food_data)
        dialog.setFixedSize(parent_size.width(), int(parent_size.height() * height_ratio))
        # 移动到父控件下部分
        parent_pos = self.meal_record_widget.mapToGlobal(self.meal_record_widget.rect().topLeft())
        dialog.move(parent_pos.x(), parent_pos.y() + int(parent_size.height() * (1 - height_ratio)))

        # 关闭对话框时自动关闭遮罩
        dialog.finished.connect(mask.close)

        dialog.exec()



