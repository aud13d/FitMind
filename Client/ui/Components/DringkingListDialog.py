from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QFrame, QPushButton, QLineEdit, QLabel,
    QSpacerItem, QSizePolicy, QHBoxLayout, QGridLayout, QListWidget
)
from PySide6.QtCore import Qt, QSize


class DrinkingListDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        if parent:
            self.setFixedSize(parent.size())
            global_pos = parent.mapToGlobal(parent.rect().topLeft())
            self.move(global_pos)
        self.setObjectName("DrinkingListDialog")
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.resize(362, 700)
        self.setMinimumSize(QSize(300, 666))

        self.verticalLayout_2 = QVBoxLayout(self)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)

        self.frame = QFrame(self)
        self.frame.setObjectName("frame")
        self.frame.setStyleSheet("""
            QPushButton {
                font: 9pt "微软雅黑"; 
                border: 1px solid #ccc; 
                border-radius: 6px; 
                background-color: white; 
                color: black; 
                border:none;
                min-width: 60px;
                min-height: 25px;
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
            
            #frame{
                background-color: white;
                border-top-right-radius:20px;
                border-top-left-radius:20px;
                border-bottom-right-radius:20px;
                border-bottom-left-radius:20px;
            }
        """)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)

        # 头部
        self.frame_head = QFrame(self.frame)
        self.frame_head.setObjectName("frame_head")
        self.frame_head.setStyleSheet("""
              QFrame{ 
              background-color: white; 
              border-top-right-radius:20px;
              border-top-left-radius:20px;
              }
        """)
        self.frame_head.setFrameShape(QFrame.StyledPanel)
        self.frame_head.setFrameShadow(QFrame.Raised)

        self.button_return = QPushButton("Return", self.frame_head)
        self.button_return.setStyleSheet("""
            QPushButton {
                font: 700 12pt "微软雅黑";
                background-color: white;
                color: rgb(12, 12, 255);
            }
        """)

        self.head_layout = QHBoxLayout(self.frame_head)
        self.head_layout.setContentsMargins(10, 10, 10, 10)
        self.head_layout.addWidget(self.button_return, alignment=Qt.AlignLeft | Qt.AlignVCenter)

        self.verticalLayout_3.addWidget(self.frame_head)

        # 中部
        self.frame_center = QFrame(self.frame)
        self.frame_center.setObjectName("frame_center")
        self.frame_center.setStyleSheet("QFrame { background-color: white; }")
        self.frame_center.setFrameShape(QFrame.StyledPanel)
        self.frame_center.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3.addWidget(self.frame_center)

        self.record_list = QListWidget(self.frame_center)
        self.record_list.setStyleSheet("""
            QListWidget {
                background-color: white;
                border: none;
                font: 10pt "微软雅黑";
                padding: 10px;
            }
            QListWidget::item {
                padding: 10px;
                border-bottom: 1px solid #eee;
            }
            QListWidget::item:selected {
                background-color: #e6f0ff;
                color: black;
            }
        """)
        self.vertical_center_layout = QVBoxLayout(self.frame_center)
        self.vertical_center_layout.setContentsMargins(10, 10, 10, 10)
        self.vertical_center_layout.addWidget(self.record_list)

        # 底部
        self.frame_foot = QFrame(self.frame)
        self.frame_foot.setObjectName("frame_foot")
        self.frame_foot.setFrameShape(QFrame.StyledPanel)
        self.frame_foot.setFrameShadow(QFrame.Raised)

        self.verticalLayout_4 = QVBoxLayout(self.frame_foot)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalSpacer = QSpacerItem(120, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.lineEdit_waterNum = QLineEdit(self.frame_foot)
        self.lineEdit_waterNum.setMinimumSize(QSize(30, 30))
        self.lineEdit_waterNum.setReadOnly(True)
        self.lineEdit_waterNum.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.lineEdit_waterNum.setStyleSheet("""
            QLineEdit {
                background-color: transparent;
                border: none;
                border-bottom: 2px solid rgb(0, 38, 255);
                font-size: 20px;
                color: rgb(0, 38, 255);
                padding: 2px;
            }
        """)

        self.label_ml = QLabel("ml", self.frame_foot)
        self.label_ml.setStyleSheet("font: 10pt \"微软雅黑\"; color:rgb(50, 114, 209)")

        self.horizontalSpacer_2 = QSpacerItem(108, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)
        self.horizontalLayout.addWidget(self.lineEdit_waterNum)
        self.horizontalLayout.addWidget(self.label_ml)
        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.verticalLayout_4.addLayout(self.horizontalLayout)

        # 输入框区域
        self.frame_input = QFrame(self.frame_foot)
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

        self.row_buttons = []
        for row_values in (["1", "2", "3"], ["4", "5", "6"],["7", "8", "9"], ["0", ".", "back"]):
            row = QHBoxLayout()
            for text in row_values:
                btn = QPushButton(text, self.frame_input)
                btn.setMinimumSize(QSize(80, 45))
                row.addWidget(btn)
            self.verticalLayout.addLayout(row)

        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.verticalLayout_4.addWidget(self.frame_input)

        self.verticalLayout_3.addWidget(self.frame_foot)
        self.verticalLayout_2.addWidget(self.frame)

        # 添加饮水按钮
        self.button_add = QPushButton("Add Drinking", self.frame_foot)
        self.button_add.setMinimumSize(QSize(0, 60))
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
        self.verticalLayout_4.addWidget(self.button_add, alignment=Qt.AlignHCenter| Qt.AlignVCenter)

        self.bind()

    def bind(self):
            self.button_return.clicked.connect(self.close)

