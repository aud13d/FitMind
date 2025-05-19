# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FitMind_Client_NewRest.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QPushButton,
    QScrollArea, QSizePolicy, QTextEdit, QWidget)


class Ui_Dialog_add_action(object):
    def setupUi(self, Dialog_add_action):
        if not Dialog_add_action.objectName():
            Dialog_add_action.setObjectName(u"Dialog_add_action")
        Dialog_add_action.resize(362, 700)
        Dialog_add_action.setMinimumSize(QSize(300, 666))
        self.horizontalLayout = QHBoxLayout(Dialog_add_action)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Dialog_add_action)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"#frame{\n"
"	background-color:white;\n"
"	border-top-right-radius:20px;\n"
"	border-top-left-radius:20px;\n"
"	border-bottom-right-radius:20px;\n"
"	border-bottom-left-radius:20px;\n"
"}\n"
"\n"
"\n"
"#button_back {\n"
"    font: 9pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"    border-radius: 6px; /* \u8f7b\u5fae\u5706\u89d2 */\n"
"    background-color: white; /* \u7eaf\u767d\u80cc\u666f */\n"
"    color: black; /* \u9ed1\u8272\u6587\u5b57 */\n"
"    min-width: 60px;\n"
"    min-height: 45px;\n"
"\n"
"}\n"
"\n"
"#button_back:hover {\n"
"    background-color: #f0f0f0; /* \u6d45\u7070\u8272\u60ac\u6d6e\u6548\u679c */\n"
"    margin-top: 2px; /* \u8f7b\u5fae\u4e0b\u79fb\uff0c\u589e\u52a0\u6309\u538b\u611f */\n"
"}\n"
"\n"
"#button_back:pressed {\n"
"    background-color: #e0e0e0; /* \u6309\u4e0b\u65f6\u53d8\u6df1\u7070 */\n"
"    margin-top: 1px; /* \u6309\u4e0b\u65f6\u8f7b\u5fae\u4e0a\u79fb */\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #f8f8f8;\n"
"    color: gray;\n"
"    border-color: #ddd;\n"
"}"
                        "\n"
"\n"
"\n"
"#label {\n"
"	font: 700 12pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.frame.setLineWidth(0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 54, 362, 646))
        self.frame_2.setStyleSheet(u"#frame_2{\n"
"	background-color:white;\n"
"	border-top-right-radius:20px;\n"
"	border-top-left-radius:20px;\n"
"	border-bottom-right-radius:20px;\n"
"	border-bottom-left-radius:20px;\n"
"}\n"
"\n"
"QPushButton {\n"
"    font: 550 10pt \"\u5fae\u8f6f\u96c5\u9ed1\"; \n"
"    border-radius: 6px; /* \u8f7b\u5fae\u5706\u89d2 */\n"
"	background-color: none;\n"
"    color: black; /* \u9ed1\u8272\u6587\u5b57 */\n"
"	border:none;\n"
"	text-align: left;\n"
"}\n"
"\n"
"\n"
"QScrollArea {\n"
"	border:none;\n"
"	background-color: none;\n"
"	border-top-right-radius:15px;\n"
"	border-top-left-radius:15px;\n"
"	border-bottom-right-radius:15px;\n"
"	border-bottom-left-radius:15px;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    background: none;\n"
"    width: 4px;\n"
"    margin: 0px;\n"
"    border: none;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: rgba(100, 100, 100, 0.5);\n"
"    min-height: 20px;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: rgba(100, "
                        "100, 100, 0.8);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical,\n"
"QScrollBar::sub-line:vertical,\n"
"QScrollBar::add-page:vertical,\n"
"QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"    border: none;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"    background: transparent;\n"
"    height: 4px;\n"
"    margin: 0px;\n"
"    border: none;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgba(100, 100, 100, 0.5);\n"
"    min-width: 20px;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:hover {\n"
"    background: rgba(100, 100, 100, 0.8);\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal,\n"
"QScrollBar::sub-line:horizontal,\n"
"QScrollBar::add-page:horizontal,\n"
"QScrollBar::sub-page:horizontal {\n"
"    background: none;\n"
"    border: none;\n"
"}\n"
"")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_2.setLineWidth(0)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.frame_2)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QSize(362, 646))
        self.scrollArea.setStyleSheet(u"QFrame{\n"
"	background-color:white;\n"
"	border-top-right-radius:15px;\n"
"	border-top-left-radius:15px;\n"
"	border-bottom-right-radius:15px;\n"
"	border-bottom-left-radius:15px;\n"
"}\n"
"\n"
"QWidget{\n"
"	border-top-right-radius:20px;\n"
"	border-top-left-radius:20px;\n"
"	border-bottom-right-radius:20px;\n"
"	border-bottom-left-radius:20px;\n"
"}")
        self.scrollArea.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 362, 646))
        self.frame_fitness = QFrame(self.scrollAreaWidgetContents)
        self.frame_fitness.setObjectName(u"frame_fitness")
        self.frame_fitness.setGeometry(QRect(10, 40, 351, 55))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_fitness.sizePolicy().hasHeightForWidth())
        self.frame_fitness.setSizePolicy(sizePolicy1)
        self.frame_fitness.setMinimumSize(QSize(350, 55))
        self.frame_fitness.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_fitness.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_fitness)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(-1, 0, -1, 0)
        self.lineEdit = QLineEdit(self.frame_fitness)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_8.addWidget(self.lineEdit)

        self.label_fitness_go = QLabel(self.frame_fitness)
        self.label_fitness_go.setObjectName(u"label_fitness_go")

        self.horizontalLayout_8.addWidget(self.label_fitness_go)

        self.frame_jump_rope = QFrame(self.scrollAreaWidgetContents)
        self.frame_jump_rope.setObjectName(u"frame_jump_rope")
        self.frame_jump_rope.setGeometry(QRect(10, 370, 350, 55))
        sizePolicy1.setHeightForWidth(self.frame_jump_rope.sizePolicy().hasHeightForWidth())
        self.frame_jump_rope.setSizePolicy(sizePolicy1)
        self.frame_jump_rope.setMinimumSize(QSize(350, 55))
        self.frame_jump_rope.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_jump_rope.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_jump_rope)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, 0, -1, 0)
        self.pushButton_4 = QPushButton(self.frame_jump_rope)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(50, 50))
        self.pushButton_4.setMaximumSize(QSize(50, 50))
        self.pushButton_4.setStyleSheet(u"QPushButton {\n"
"    background-color: #FF0000;  /* \u8bbe\u7f6e\u7eaf\u8272\u80cc\u666f */\n"
"    border: none;             /* \u79fb\u9664\u9ed8\u8ba4\u8fb9\u6846 */\n"
"    margin: 5px;              /* \u8bbe\u7f6e\u5916\u8fb9\u8ddd\u4e3a5\u50cf\u7d20 */\n"
"}\n"
"QPushButton:pressed {\n"
"    /* \u9009\u4e2d\u72b6\u6001\u6837\u5f0f */\n"
"    border: 2px solid black;        /* \u9ed1\u8272\u5916\u6846 */\n"
"}")

        self.horizontalLayout_9.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.frame_jump_rope)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(50, 50))
        self.pushButton_5.setMaximumSize(QSize(50, 50))
        self.pushButton_5.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFA500;  /* \u8bbe\u7f6e\u7eaf\u8272\u80cc\u666f */\n"
"    border: none;             /* \u79fb\u9664\u9ed8\u8ba4\u8fb9\u6846 */\n"
"    margin: 5px;              /* \u8bbe\u7f6e\u5916\u8fb9\u8ddd\u4e3a5\u50cf\u7d20 */\n"
"}\n"
"QPushButton:pressed {\n"
"    /* \u9009\u4e2d\u72b6\u6001\u6837\u5f0f */\n"
"    border: 2px solid black;        /* \u9ed1\u8272\u5916\u6846 */\n"
"}")

        self.horizontalLayout_9.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.frame_jump_rope)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(50, 50))
        self.pushButton_6.setMaximumSize(QSize(50, 50))
        self.pushButton_6.setStyleSheet(u"QPushButton {\n"
"    background-color: #90EE90;  /* \u8bbe\u7f6e\u7eaf\u8272\u80cc\u666f */\n"
"    border: none;             /* \u79fb\u9664\u9ed8\u8ba4\u8fb9\u6846 */\n"
"    margin: 5px;              /* \u8bbe\u7f6e\u5916\u8fb9\u8ddd\u4e3a5\u50cf\u7d20 */\n"
"}\n"
"QPushButton:pressed {\n"
"    /* \u9009\u4e2d\u72b6\u6001\u6837\u5f0f */\n"
"    border: 2px solid black;        /* \u9ed1\u8272\u5916\u6846 */\n"
"}")

        self.horizontalLayout_9.addWidget(self.pushButton_6)

        self.pushButton_7 = QPushButton(self.frame_jump_rope)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(50, 50))
        self.pushButton_7.setMaximumSize(QSize(50, 50))
        self.pushButton_7.setStyleSheet(u"QPushButton {\n"
"    background-color: #87CEEB;  /* \u8bbe\u7f6e\u7eaf\u8272\u80cc\u666f */\n"
"    border: none;             /* \u79fb\u9664\u9ed8\u8ba4\u8fb9\u6846 */\n"
"    margin: 5px;              /* \u8bbe\u7f6e\u5916\u8fb9\u8ddd\u4e3a5\u50cf\u7d20 */\n"
"}\n"
"QPushButton:pressed {\n"
"    /* \u9009\u4e2d\u72b6\u6001\u6837\u5f0f */\n"
"    border: 2px solid black;        /* \u9ed1\u8272\u5916\u6846 */\n"
"}")

        self.horizontalLayout_9.addWidget(self.pushButton_7)

        self.pushButton_3 = QPushButton(self.frame_jump_rope)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(50, 50))
        self.pushButton_3.setMaximumSize(QSize(50, 50))
        self.pushButton_3.setStyleSheet(u"QPushButton {\n"
"    background-color: #DDA0DD;  /* \u8bbe\u7f6e\u7eaf\u8272\u80cc\u666f */\n"
"    border: none;             /* \u79fb\u9664\u9ed8\u8ba4\u8fb9\u6846 */\n"
"    margin: 5px;              /* \u8bbe\u7f6e\u5916\u8fb9\u8ddd\u4e3a5\u50cf\u7d20 */\n"
"}\n"
"QPushButton:pressed {\n"
"    /* \u9009\u4e2d\u72b6\u6001\u6837\u5f0f */\n"
"    border: 2px solid black;        /* \u9ed1\u8272\u5916\u6846 */\n"
"}")

        self.horizontalLayout_9.addWidget(self.pushButton_3)

        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 110, 151, 41))
        font = QFont()
        font.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font.setBold(True)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setStyleSheet(u"QLabel {\n"
"    color:  #808080;              /* \u767d\u8272\u6587\u5b57 */\n"
"    border: none;             /* \u79fb\u9664\u9ed8\u8ba4\u8fb9\u6846 */\n"
"    padding: 6px 12px;        /* \u5185\u8fb9\u8ddd\uff08\u6587\u5b57\u4e0e\u8fb9\u7f18\u95f4\u8ddd\uff09 */\n"
"    font-size: 12px;          /* \u6587\u5b57\u5927\u5c0f */\n"
"}")
        self.frame_fitness_2 = QFrame(self.scrollAreaWidgetContents)
        self.frame_fitness_2.setObjectName(u"frame_fitness_2")
        self.frame_fitness_2.setGeometry(QRect(10, 150, 351, 55))
        sizePolicy1.setHeightForWidth(self.frame_fitness_2.sizePolicy().hasHeightForWidth())
        self.frame_fitness_2.setSizePolicy(sizePolicy1)
        self.frame_fitness_2.setMinimumSize(QSize(350, 55))
        self.frame_fitness_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_fitness_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_fitness_2)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(-1, 0, -1, 0)
        self.label_8 = QLabel(self.frame_fitness_2)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_10.addWidget(self.label_8)

        self.pushButton_9 = QPushButton(self.frame_fitness_2)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMinimumSize(QSize(0, 0))
        self.pushButton_9.setStyleSheet(u"QPushButton {\n"
"    background-color: white;\n"
"    color: #2a7fff;\n"
"    border: 1px solid #CCCCCC;\n"
"    padding: 4px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #F0F0F0; /* \u60ac\u505c\u65f6\u80cc\u666f\u53d8\u6d45\u7070 */\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #E0E0E0; /* \u6309\u4e0b\u65f6\u80cc\u666f\u66f4\u6df1\u7070 */\n"
"}")

        self.horizontalLayout_10.addWidget(self.pushButton_9)

        self.pushButton_10 = QPushButton(self.frame_fitness_2)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setStyleSheet(u"QPushButton {\n"
"    background-color: white;\n"
"    color: #2a7fff;\n"
"    border: 1px solid #CCCCCC;\n"
"    padding: 4px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #F0F0F0; /* \u60ac\u505c\u65f6\u80cc\u666f\u53d8\u6d45\u7070 */\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #E0E0E0; /* \u6309\u4e0b\u65f6\u80cc\u666f\u66f4\u6df1\u7070 */\n"
"}")

        self.horizontalLayout_10.addWidget(self.pushButton_10)

        self.pushButton_12 = QPushButton(self.frame_fitness_2)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setStyleSheet(u"QPushButton {\n"
"    background-color: white;\n"
"    color: #2a7fff;\n"
"    border: 1px solid #CCCCCC;\n"
"    padding: 4px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #F0F0F0; /* \u60ac\u505c\u65f6\u80cc\u666f\u53d8\u6d45\u7070 */\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #E0E0E0; /* \u6309\u4e0b\u65f6\u80cc\u666f\u66f4\u6df1\u7070 */\n"
"}")

        self.horizontalLayout_10.addWidget(self.pushButton_12)

        self.pushButton_11 = QPushButton(self.frame_fitness_2)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setStyleSheet(u"QPushButton {\n"
"    background-color: white;\n"
"    color: #2a7fff;\n"
"    border: 1px solid #CCCCCC;\n"
"    padding: 4px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #F0F0F0; /* \u60ac\u505c\u65f6\u80cc\u666f\u53d8\u6d45\u7070 */\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #E0E0E0; /* \u6309\u4e0b\u65f6\u80cc\u666f\u66f4\u6df1\u7070 */\n"
"}")

        self.horizontalLayout_10.addWidget(self.pushButton_11)

        self.label_fitness_move_2 = QLabel(self.frame_fitness_2)
        self.label_fitness_move_2.setObjectName(u"label_fitness_move_2")
        self.label_fitness_move_2.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_10.addWidget(self.label_fitness_move_2)

        self.label_fitness_go_2 = QLabel(self.frame_fitness_2)
        self.label_fitness_go_2.setObjectName(u"label_fitness_go_2")

        self.horizontalLayout_10.addWidget(self.label_fitness_go_2)

        self.horizontalLayout_10.setStretch(5, 2)
        self.aerobic_name = QLabel(self.scrollAreaWidgetContents)
        self.aerobic_name.setObjectName(u"aerobic_name")
        self.aerobic_name.setGeometry(QRect(10, 0, 131, 41))
        self.aerobic_name.setFont(font)
        self.aerobic_name.setStyleSheet(u"QLabel {\n"
"    color:  #808080;              /* \u767d\u8272\u6587\u5b57 */\n"
"    border: none;             /* \u79fb\u9664\u9ed8\u8ba4\u8fb9\u6846 */\n"
"    padding: 6px 12px;        /* \u5185\u8fb9\u8ddd\uff08\u6587\u5b57\u4e0e\u8fb9\u7f18\u95f4\u8ddd\uff09 */\n"
"    font-size: 12px;          /* \u6587\u5b57\u5927\u5c0f */\n"
"}")
        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 330, 151, 41))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"QLabel {\n"
"    color:  #808080;              /* \u767d\u8272\u6587\u5b57 */\n"
"    border: none;             /* \u79fb\u9664\u9ed8\u8ba4\u8fb9\u6846 */\n"
"    padding: 6px 12px;        /* \u5185\u8fb9\u8ddd\uff08\u6587\u5b57\u4e0e\u8fb9\u7f18\u95f4\u8ddd\uff09 */\n"
"    font-size: 12px;          /* \u6587\u5b57\u5927\u5c0f */\n"
"}")
        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 220, 151, 41))
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"QLabel {\n"
"    color:  #808080;              /* \u767d\u8272\u6587\u5b57 */\n"
"    border: none;             /* \u79fb\u9664\u9ed8\u8ba4\u8fb9\u6846 */\n"
"    padding: 6px 12px;        /* \u5185\u8fb9\u8ddd\uff08\u6587\u5b57\u4e0e\u8fb9\u7f18\u95f4\u8ddd\uff09 */\n"
"    font-size: 12px;          /* \u6587\u5b57\u5927\u5c0f */\n"
"}")
        self.frame_fitness_3 = QFrame(self.scrollAreaWidgetContents)
        self.frame_fitness_3.setObjectName(u"frame_fitness_3")
        self.frame_fitness_3.setGeometry(QRect(10, 260, 351, 55))
        sizePolicy1.setHeightForWidth(self.frame_fitness_3.sizePolicy().hasHeightForWidth())
        self.frame_fitness_3.setSizePolicy(sizePolicy1)
        self.frame_fitness_3.setMinimumSize(QSize(350, 55))
        self.frame_fitness_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_fitness_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_fitness_3)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(-1, 0, -1, 0)
        self.pushButton_8 = QPushButton(self.frame_fitness_3)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setStyleSheet(u"QPushButton {\n"
"    color:  #808080;              /* \u767d\u8272\u6587\u5b57 */\n"
"    border: none;             /* \u79fb\u9664\u9ed8\u8ba4\u8fb9\u6846 */\n"
"    padding: 6px 12px;        /* \u5185\u8fb9\u8ddd\uff08\u6587\u5b57\u4e0e\u8fb9\u7f18\u95f4\u8ddd\uff09 */\n"
"    font-size: 12px;          /* \u6587\u5b57\u5927\u5c0f */\n"
"}")

        self.horizontalLayout_11.addWidget(self.pushButton_8)

        self.lineEdit_2 = QLineEdit(self.frame_fitness_3)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setStyleSheet(u"QPushButton {\n"
"    color:  #808080;              /* \u767d\u8272\u6587\u5b57 */\n"
"    border: none;             /* \u79fb\u9664\u9ed8\u8ba4\u8fb9\u6846 */\n"
"    padding: 6px 12px;        /* \u5185\u8fb9\u8ddd\uff08\u6587\u5b57\u4e0e\u8fb9\u7f18\u95f4\u8ddd\uff09 */\n"
"    font-size: 12px;          /* \u6587\u5b57\u5927\u5c0f */\n"
"}")

        self.horizontalLayout_11.addWidget(self.lineEdit_2)

        self.label_fitness_go_3 = QLabel(self.frame_fitness_3)
        self.label_fitness_go_3.setObjectName(u"label_fitness_go_3")

        self.horizontalLayout_11.addWidget(self.label_fitness_go_3)

        self.textEdit = QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(10, 420, 351, 61))
        self.textEdit.setStyleSheet(u"QTextEdit {\n"
"    color:  #808080;              /* \u767d\u8272\u6587\u5b57 */\n"
"    border: none;             /* \u79fb\u9664\u9ed8\u8ba4\u8fb9\u6846 */\n"
"    padding: 6px 12px;        /* \u5185\u8fb9\u8ddd\uff08\u6587\u5b57\u4e0e\u8fb9\u7f18\u95f4\u8ddd\uff09 */\n"
"    font-size: 12px;          /* \u6587\u5b57\u5927\u5c0f */\n"
"}")
        self.textEdit.setReadOnly(True)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_3.addWidget(self.scrollArea)

        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(280, 10, 75, 24))
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"    /* \u57fa\u7840\u6837\u5f0f */\n"
"    background-color: #2a7fff;  /* \u84dd\u8272\u80cc\u666f */\n"
"    color: white;              /* \u767d\u8272\u6587\u5b57 */\n"
"    border: none;             /* \u79fb\u9664\u9ed8\u8ba4\u8fb9\u6846 */\n"
"    border-radius: 8px;       /* \u5706\u89d2\u534a\u5f84\uff08\u53ef\u8c03\u6574\uff09 */\n"
"    padding: 6px 12px;        /* \u5185\u8fb9\u8ddd\uff08\u6587\u5b57\u4e0e\u8fb9\u7f18\u95f4\u8ddd\uff09 */\n"
"    font-size: 14px;          /* \u6587\u5b57\u5927\u5c0f */\n"
"}\n"
"\n"
"/* \u60ac\u505c\u72b6\u6001 */\n"
"QToolButton:hover {\n"
"    background-color: #1976D2;  /* \u66f4\u6df1\u7684\u84dd\u8272 */\n"
"}\n"
"\n"
"/* \u6309\u4e0b\u72b6\u6001 */\n"
"QToolButton:pressed {\n"
"    background-color: #1565C0;  /* \u6700\u6df1\u7684\u84dd\u8272 */\n"
"}")
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 10, 75, 24))
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"    color: #000000;              /* \u767d\u8272\u6587\u5b57 */\n"
"    border: none;             /* \u79fb\u9664\u9ed8\u8ba4\u8fb9\u6846 */\n"
"    border-radius: 8px;       /* \u5706\u89d2\u534a\u5f84\uff08\u53ef\u8c03\u6574\uff09 */\n"
"    padding: 6px 12px;        /* \u5185\u8fb9\u8ddd\uff08\u6587\u5b57\u4e0e\u8fb9\u7f18\u95f4\u8ddd\uff09 */\n"
"    font-size: 14px;          /* \u6587\u5b57\u5927\u5c0f */\n"
"}")

        self.horizontalLayout.addWidget(self.frame)


        self.retranslateUi(Dialog_add_action)

        QMetaObject.connectSlotsByName(Dialog_add_action)
    # setupUi

    def retranslateUi(self, Dialog_add_action):
        Dialog_add_action.setWindowTitle(QCoreApplication.translate("Dialog_add_action", u"Dialog", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Dialog_add_action", u"Enter a title, such as leg injury, aunt, etc", None))
        self.label_fitness_go.setText("")
        self.pushButton_4.setText("")
        self.pushButton_5.setText("")
        self.pushButton_6.setText("")
        self.pushButton_7.setText("")
        self.pushButton_3.setText("")
        self.label.setText(QCoreApplication.translate("Dialog_add_action", u"Common Reasons", None))
        self.label_8.setText("")
        self.pushButton_9.setText(QCoreApplication.translate("Dialog_add_action", u"Rest Day", None))
        self.pushButton_10.setText(QCoreApplication.translate("Dialog_add_action", u"Busy", None))
        self.pushButton_12.setText(QCoreApplication.translate("Dialog_add_action", u"Fall Ill ", None))
        self.pushButton_11.setText(QCoreApplication.translate("Dialog_add_action", u"Be Injured", None))
        self.label_fitness_move_2.setText("")
        self.label_fitness_go_2.setText("")
        self.aerobic_name.setText(QCoreApplication.translate("Dialog_add_action", u"Rest Day Title", None))
        self.label_2.setText(QCoreApplication.translate("Dialog_add_action", u"Set Display Color", None))
        self.label_3.setText(QCoreApplication.translate("Dialog_add_action", u"Date Setting", None))
        self.pushButton_8.setText(QCoreApplication.translate("Dialog_add_action", u"2025-05-16", None))
        self.label_fitness_go_3.setText("")
        self.textEdit.setHtml(QCoreApplication.translate("Dialog_add_action", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:12px; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Attention: Represents the display color of this rest day label on the calendar</span></p></body></html>", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog_add_action", u"Save", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog_add_action", u"Return", None))
    # retranslateUi

