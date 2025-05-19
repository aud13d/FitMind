from PySide6.QtWidgets import QApplication, QLabel, QFrame
from PySide6.QtGui import QPixmap, QPainter, QPen,  QColor
from PySide6.QtCore import Qt, QPoint, QRect
import sys

from Client.config import BodyQFrame_ImagePath


class BodyFrame(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("身体数据图")
        self.setMinimumSize(362, 700)

        self.pixmap = QPixmap(BodyQFrame_ImagePath)  # 替换成你的图片路径
        if self.pixmap.isNull():
            print("警告: 图片加载失败，使用空白图像")
            self.pixmap = QPixmap(362, 700)
            self.pixmap.fill(Qt.gray)

        self.image_rect = QRect()

        # 格式: 名称 => (身体部位点比例, 标签位置比例)
        # 单点部位
        self.single_parts = {
            "肩宽": ((0.58, 0.2), (0.75, 0.10)),
            "脖围": ((0.49, 0.16), (0.1, 0.07)),
            "胸围": ((0.5, 0.25), (0.75, 0.19)),
            "腰围": ((0.57, 0.40), (0.75, 0.34)),
            "臀围": ((0.43, 0.48), (0.1, 0.42)),
        }

        # 双点部位
        self.paired_parts = {
            "臂围": ((0.395, 0.28), (0.1, 0.19)),  # 用左点
            "小臂": ((0.39, 0.4), (0.1, 0.31)),  # 用左点
            "腿围": ((0.56, 0.62), (0.75, 0.52)),   # 用右点
            "小腿": ((0.45, 0.8), (0.1, 0.7)),   # 用左点
        }

        self.body_points = {}
        self.label_points = {}

        self.labels = {}

        # 创建单点部位标签
        for name in self.single_parts:
            label = QLabel(name, self)
            label.setStyleSheet("background: white; border: none; border-radius: 4px; padding: 2px;")
            label.adjustSize()
            self.labels[name] = label

        # 创建成对部位标签，左右两行文字
        for name in self.paired_parts:
            text = f"{name}-20cm左\n{name}-20cm右"
            label = QLabel(text, self)
            label.setStyleSheet("background: white; border: none; border-radius: 4px; padding: 2px;")
            label.setAlignment(Qt.AlignLeft)
            label.adjustSize()
            self.labels[name] = label

        self.bind()

    def bind(self):
        # 为所有标签绑定点击事件
        for name in self.labels:
            label = self.labels[name]
            label.mousePressEvent = self.set_body_part_data(name, label)

    def set_body_part_data(self, name, label):
        """设置身体部位数据"""
        def handler(event):
            cx = label.x() + label.width() // 2
            cy = label.y() + label.height() // 2
            print(f"点击部位: {name}，中心坐标: ({cx}, {cy})")

        return handler

    def resizeEvent(self, event):
        """综合调整大小"""
        self.update_image_rect()
        self.update_labels()
        self.update()
        super().resizeEvent(event)

    def update_image_rect(self):
        """更新图片矩形区域"""
        target_size = self.size()
        scaled_size = self.pixmap.size().scaled(target_size, Qt.KeepAspectRatio)
        x = (target_size.width() - scaled_size.width()) // 2
        y = (target_size.height() - scaled_size.height()) // 2
        self.image_rect = QRect(x, y, scaled_size.width(), scaled_size.height())
        self.calculate_absolute_positions()

    def calculate_absolute_positions(self):
        """计算绝对位置"""
        for name, ((bx_ratio, by_ratio), (lx_ratio, ly_ratio)) in self.single_parts.items():
            bx = int(self.image_rect.left() + self.image_rect.width() * bx_ratio)
            by = int(self.image_rect.top() + self.image_rect.height() * by_ratio)
            lx = int(self.image_rect.left() + self.image_rect.width() * lx_ratio)
            ly = int(self.image_rect.top() + self.image_rect.height() * ly_ratio)
            self.body_points[name] = (bx, by)
            self.label_points[name] = (lx, ly)

        for name, (body_ratio, label_ratio) in self.paired_parts.items():
            bx = int(self.image_rect.left() + self.image_rect.width() * body_ratio[0])
            by = int(self.image_rect.top() + self.image_rect.height() * body_ratio[1])
            lx = int(self.image_rect.left() + self.image_rect.width() * label_ratio[0])
            ly = int(self.image_rect.top() + self.image_rect.height() * label_ratio[1])
            self.body_points[name] = (bx, by)
            self.label_points[name] = (lx, ly)

    def update_labels(self):
        """更新标签位置"""
        for name, (lx, ly) in self.label_points.items():
            label = self.labels[name]
            label_w = label.width()
            label_h = label.height()

            if lx + label_w > self.width():
                lx = self.width() - label_w
            if ly + label_h > self.height():
                ly = self.height() - label_h

            label.move(lx, ly)

    def paintEvent(self, event):
        """绘制部位点与标签的连线"""
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        painter.fillRect(self.rect(), Qt.white)
        painter.drawPixmap(self.image_rect, self.pixmap)

        pen = QPen(Qt.darkGray, 1.5)
        painter.setPen(pen)
        painter.setBrush( QColor(100, 220, 150))

        offset = 2  # 竖线偏移量
        extend = 10  # 横线延伸长度
        width_mid = self.width() / 2  # 窗体水平中线

        # 单点部位连线
        for name, (bx, by) in self.body_points.items():
            if name in self.single_parts:
                label = self.labels[name]
                lx = label.x() + label.width() // 2
                ly = label.y() + label.height() + offset

                if lx < width_mid:
                    end_x = lx - extend
                else:
                    end_x = lx + extend

                painter.drawLine(bx, by, bx, ly)
                painter.drawLine(bx, ly, end_x, ly)
                painter.drawEllipse(QPoint(bx, by), 5, 5)

        # 成对部位连线
        for name, (bx, by) in self.body_points.items():
            if name in self.paired_parts:
                label = self.labels[name]
                lx = label.x()
                ly = label.y() + label.height() + offset
                label_center_x = lx + label.width() / 2

                # 左侧横线终点（有问题这里）
                if label_center_x < width_mid:
                    left_end_x = lx + extend
                else:
                    left_end_x = lx - extend

                # 右侧横线起点和终点(有问题这里)
                label_right_x = lx + label.width()
                if label_center_x < width_mid:
                    right_end_x = label_right_x + extend
                else:
                    right_end_x = label_right_x - extend

                # 画竖线
                painter.drawLine(bx, by, bx, ly)

                # 画左侧横线
                painter.drawLine(bx, ly, left_end_x, ly)

                # 画右侧横线
                painter.drawLine(bx, ly, right_end_x, ly)

                painter.drawEllipse(QPoint(bx, by), 5, 5)

        painter.setBrush(Qt.NoBrush)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BodyFrame()
    window.show()
    sys.exit(app.exec())
