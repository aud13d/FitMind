# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FitMind_Client_NewRest.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
    QScrollArea, QSizePolicy, QWidget)
from ..res_rc import *

class Ui_Dialog_NewRest(object):
    def setupUi(self, Dialog_NewRest):
        if not Dialog_NewRest.objectName():
            Dialog_NewRest.setObjectName(u"Dialog_NewRest")
        Dialog_NewRest.resize(362, 700)
        Dialog_NewRest.setMinimumSize(QSize(300, 666))
        self.horizontalLayout = QHBoxLayout(Dialog_NewRest)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Dialog_NewRest)
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
        self.frame_rest_title = QFrame(self.scrollAreaWidgetContents)
        self.frame_rest_title.setObjectName(u"frame_rest_title")
        self.frame_rest_title.setGeometry(QRect(10, 40, 351, 55))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_rest_title.sizePolicy().hasHeightForWidth())
        self.frame_rest_title.setSizePolicy(sizePolicy1)
        self.frame_rest_title.setMinimumSize(QSize(350, 55))
        self.frame_rest_title.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_rest_title.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_rest_title)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(-1, 0, -1, 0)
        self.lineEdit_rest_title = QLineEdit(self.frame_rest_title)
        self.lineEdit_rest_title.setObjectName(u"lineEdit_rest_title")

        self.horizontalLayout_8.addWidget(self.lineEdit_rest_title)

        self.label_fitness_go = QLabel(self.frame_rest_title)
        self.label_fitness_go.setObjectName(u"label_fitness_go")

        self.horizontalLayout_8.addWidget(self.label_fitness_go)

        self.frame_color = QFrame(self.scrollAreaWidgetContents)
        self.frame_color.setObjectName(u"frame_color")
        self.frame_color.setGeometry(QRect(-1, 370, 361, 55))
        sizePolicy1.setHeightForWidth(self.frame_color.sizePolicy().hasHeightForWidth())
        self.frame_color.setSizePolicy(sizePolicy1)
        self.frame_color.setMinimumSize(QSize(350, 55))
        self.frame_color.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_color.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_color)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, 0, -1, 0)
        self.button_rest_setred = QPushButton(self.frame_color)
        self.button_rest_setred.setObjectName(u"button_rest_setred")
        self.button_rest_setred.setMinimumSize(QSize(50, 50))
        self.button_rest_setred.setMaximumSize(QSize(50, 50))
        self.button_rest_setred.setStyleSheet(u"QPushButton {\n"
"    background-color: #FF0000;  /* \u8bbe\u7f6e\u7eaf\u8272\u80cc\u666f */\n"
"    border: none;             /* \u79fb\u9664\u9ed8\u8ba4\u8fb9\u6846 */\n"
"    margin: 5px;              /* \u8bbe\u7f6e\u5916\u8fb9\u8ddd\u4e3a5\u50cf\u7d20 */\n"
"}\n"
"QPushButton:pressed {\n"
"    /* \u9009\u4e2d\u72b6\u6001\u6837\u5f0f */\n"
"    border: 2px solid black;        /* \u9ed1\u8272\u5916\u6846 */\n"
"}")

        self.horizontalLayout_9.addWidget(self.button_rest_setred)

        self.button_rest_setroange = QPushButton(self.frame_color)
        self.button_rest_setroange.setObjectName(u"button_rest_setroange")
        self.button_rest_setroange.setMinimumSize(QSize(50, 50))
        self.button_rest_setroange.setMaximumSize(QSize(50, 50))
        self.button_rest_setroange.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFA500;  /* \u8bbe\u7f6e\u7eaf\u8272\u80cc\u666f */\n"
"    border: none;             /* \u79fb\u9664\u9ed8\u8ba4\u8fb9\u6846 */\n"
"    margin: 5px;              /* \u8bbe\u7f6e\u5916\u8fb9\u8ddd\u4e3a5\u50cf\u7d20 */\n"
"}\n"
"QPushButton:pressed {\n"
"    /* \u9009\u4e2d\u72b6\u6001\u6837\u5f0f */\n"
"    border: 2px solid black;        /* \u9ed1\u8272\u5916\u6846 */\n"
"}")

        self.horizontalLayout_9.addWidget(self.button_rest_setroange)

        self.button_rest_setgreen = QPushButton(self.frame_color)
        self.button_rest_setgreen.setObjectName(u"button_rest_setgreen")
        self.button_rest_setgreen.setMinimumSize(QSize(50, 50))
        self.button_rest_setgreen.setMaximumSize(QSize(50, 50))
        self.button_rest_setgreen.setStyleSheet(u"QPushButton {\n"
"    background-color: #90EE90;  /* \u8bbe\u7f6e\u7eaf\u8272\u80cc\u666f */\n"
"    border: none;             /* \u79fb\u9664\u9ed8\u8ba4\u8fb9\u6846 */\n"
"    margin: 5px;              /* \u8bbe\u7f6e\u5916\u8fb9\u8ddd\u4e3a5\u50cf\u7d20 */\n"
"}\n"
"QPushButton:pressed {\n"
"    /* \u9009\u4e2d\u72b6\u6001\u6837\u5f0f */\n"
"    border: 2px solid black;        /* \u9ed1\u8272\u5916\u6846 */\n"
"}")

        self.horizontalLayout_9.addWidget(self.button_rest_setgreen)

        self.button_rest_setblue = QPushButton(self.frame_color)
        self.button_rest_setblue.setObjectName(u"button_rest_setblue")
        self.button_rest_setblue.setMinimumSize(QSize(50, 50))
        self.button_rest_setblue.setMaximumSize(QSize(50, 50))
        self.button_rest_setblue.setStyleSheet(u"QPushButton {\n"
"    background-color: #87CEEB;  /* \u8bbe\u7f6e\u7eaf\u8272\u80cc\u666f */\n"
"    border: none;             /* \u79fb\u9664\u9ed8\u8ba4\u8fb9\u6846 */\n"
"    margin: 5px;              /* \u8bbe\u7f6e\u5916\u8fb9\u8ddd\u4e3a5\u50cf\u7d20 */\n"
"}\n"
"QPushButton:pressed {\n"
"    /* \u9009\u4e2d\u72b6\u6001\u6837\u5f0f */\n"
"    border: 2px solid black;        /* \u9ed1\u8272\u5916\u6846 */\n"
"}")

        self.horizontalLayout_9.addWidget(self.button_rest_setblue)

        self.button_rest_setpurple = QPushButton(self.frame_color)
        self.button_rest_setpurple.setObjectName(u"button_rest_setpurple")
        self.button_rest_setpurple.setMinimumSize(QSize(50, 50))
        self.button_rest_setpurple.setMaximumSize(QSize(50, 50))
        self.button_rest_setpurple.setStyleSheet(u"QPushButton {\n"
"    background-color: #DDA0DD;  /* \u8bbe\u7f6e\u7eaf\u8272\u80cc\u666f */\n"
"    border: none;             /* \u79fb\u9664\u9ed8\u8ba4\u8fb9\u6846 */\n"
"    margin: 5px;              /* \u8bbe\u7f6e\u5916\u8fb9\u8ddd\u4e3a5\u50cf\u7d20 */\n"
"}\n"
"QPushButton:pressed {\n"
"    /* \u9009\u4e2d\u72b6\u6001\u6837\u5f0f */\n"
"    border: 2px solid black;        /* \u9ed1\u8272\u5916\u6846 */\n"
"}")

        self.horizontalLayout_9.addWidget(self.button_rest_setpurple)

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
        self.frame_common_reasons = QFrame(self.scrollAreaWidgetContents)
        self.frame_common_reasons.setObjectName(u"frame_common_reasons")
        self.frame_common_reasons.setGeometry(QRect(10, 150, 351, 55))
        sizePolicy1.setHeightForWidth(self.frame_common_reasons.sizePolicy().hasHeightForWidth())
        self.frame_common_reasons.setSizePolicy(sizePolicy1)
        self.frame_common_reasons.setMinimumSize(QSize(350, 55))
        self.frame_common_reasons.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_common_reasons.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_common_reasons)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(-1, 0, -1, 0)
        self.label_8 = QLabel(self.frame_common_reasons)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_10.addWidget(self.label_8)

        self.button_choice_1 = QPushButton(self.frame_common_reasons)
        self.button_choice_1.setObjectName(u"button_choice_1")
        self.button_choice_1.setMinimumSize(QSize(0, 0))
        self.button_choice_1.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_10.addWidget(self.button_choice_1)

        self.button_choice_2 = QPushButton(self.frame_common_reasons)
        self.button_choice_2.setObjectName(u"button_choice_2")
        self.button_choice_2.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_10.addWidget(self.button_choice_2)

        self.button_choice_3 = QPushButton(self.frame_common_reasons)
        self.button_choice_3.setObjectName(u"button_choice_3")
        self.button_choice_3.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_10.addWidget(self.button_choice_3)

        self.button_choice_4 = QPushButton(self.frame_common_reasons)
        self.button_choice_4.setObjectName(u"button_choice_4")
        self.button_choice_4.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_10.addWidget(self.button_choice_4)

        self.label_10 = QLabel(self.frame_common_reasons)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_10.addWidget(self.label_10)

        self.label_9 = QLabel(self.frame_common_reasons)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_10.addWidget(self.label_9)

        self.horizontalLayout_10.setStretch(5, 2)
        self.label_4 = QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 0, 131, 41))
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"QLabel {\n"
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
        self.frame_date_setting = QFrame(self.scrollAreaWidgetContents)
        self.frame_date_setting.setObjectName(u"frame_date_setting")
        self.frame_date_setting.setGeometry(QRect(10, 260, 351, 55))
        sizePolicy1.setHeightForWidth(self.frame_date_setting.sizePolicy().hasHeightForWidth())
        self.frame_date_setting.setSizePolicy(sizePolicy1)
        self.frame_date_setting.setMinimumSize(QSize(350, 55))
        self.frame_date_setting.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_date_setting.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_date_setting)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(-1, 0, -1, 0)
        self.button_date_setting = QPushButton(self.frame_date_setting)
        self.button_date_setting.setObjectName(u"button_date_setting")
        self.button_date_setting.setStyleSheet(u"QPushButton {\n"
"    color:  #808080;              /* \u767d\u8272\u6587\u5b57 */\n"
"    border: none;             /* \u79fb\u9664\u9ed8\u8ba4\u8fb9\u6846 */\n"
"    padding: 6px 12px;        /* \u5185\u8fb9\u8ddd\uff08\u6587\u5b57\u4e0e\u8fb9\u7f18\u95f4\u8ddd\uff09 */\n"
"    font-size: 12px;          /* \u6587\u5b57\u5927\u5c0f */\n"
"}")

        self.horizontalLayout_11.addWidget(self.button_date_setting)

        self.lineEdit_2 = QLineEdit(self.frame_date_setting)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setStyleSheet(u"QPushButton {\n"
"    color:  #808080;              /* \u767d\u8272\u6587\u5b57 */\n"
"    border: none;             /* \u79fb\u9664\u9ed8\u8ba4\u8fb9\u6846 */\n"
"    padding: 6px 12px;        /* \u5185\u8fb9\u8ddd\uff08\u6587\u5b57\u4e0e\u8fb9\u7f18\u95f4\u8ddd\uff09 */\n"
"    font-size: 12px;          /* \u6587\u5b57\u5927\u5c0f */\n"
"}")

        self.horizontalLayout_11.addWidget(self.lineEdit_2)

        self.label_fitness_go_3 = QLabel(self.frame_date_setting)
        self.label_fitness_go_3.setObjectName(u"label_fitness_go_3")

        self.horizontalLayout_11.addWidget(self.label_fitness_go_3)

        self.label_5 = QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(0, 430, 361, 41))
        self.label_5.setStyleSheet(u"QLabel{\n"
"	    color:  #808080;              /* \u767d\u8272\u6587\u5b57 */\n"
"    border: none;             /* \u79fb\u9664\u9ed8\u8ba4\u8fb9\u6846 */\n"
"    padding: 6px 12px;        /* \u5185\u8fb9\u8ddd\uff08\u6587\u5b57\u4e0e\u8fb9\u7f18\u95f4\u8ddd\uff09 */\n"
"    font-size: 12px;          /* \u6587\u5b57\u5927\u5c0f */\n"
"}")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_3.addWidget(self.scrollArea)

        self.button_save = QPushButton(self.frame)
        self.button_save.setObjectName(u"button_save")
        self.button_save.setGeometry(QRect(280, 10, 75, 24))
        self.button_save.setStyleSheet(u"QPushButton {\n"
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
        self.button_return = QPushButton(self.frame)
        self.button_return.setObjectName(u"button_return")
        self.button_return.setGeometry(QRect(10, 10, 75, 24))
        self.button_return.setStyleSheet(u"QPushButton {\n"
"    color: #000000;              /* \u767d\u8272\u6587\u5b57 */\n"
"    border: none;             /* \u79fb\u9664\u9ed8\u8ba4\u8fb9\u6846 */\n"
"    border-radius: 8px;       /* \u5706\u89d2\u534a\u5f84\uff08\u53ef\u8c03\u6574\uff09 */\n"
"    padding: 6px 12px;        /* \u5185\u8fb9\u8ddd\uff08\u6587\u5b57\u4e0e\u8fb9\u7f18\u95f4\u8ddd\uff09 */\n"
"    font-size: 14px;          /* \u6587\u5b57\u5927\u5c0f */\n"
"}")

        self.horizontalLayout.addWidget(self.frame)


        self.retranslateUi(Dialog_NewRest)

        QMetaObject.connectSlotsByName(Dialog_NewRest)
    # setupUi

    def retranslateUi(self, Dialog_NewRest):
        Dialog_NewRest.setWindowTitle(QCoreApplication.translate("Dialog_NewRest", u"Dialog", None))
        self.lineEdit_rest_title.setPlaceholderText(QCoreApplication.translate("Dialog_NewRest", u"Enter a title, such as leg injury, aunt, etc", None))
        self.label_fitness_go.setText("")
        self.button_rest_setred.setText("")
        self.button_rest_setroange.setText("")
        self.button_rest_setgreen.setText("")
        self.button_rest_setblue.setText("")
        self.button_rest_setpurple.setText("")
        self.label.setText(QCoreApplication.translate("Dialog_NewRest", u"Common Reasons", None))
        self.label_8.setText("")
        self.button_choice_1.setText(QCoreApplication.translate("Dialog_NewRest", u"Rest Day", None))
        self.button_choice_2.setText(QCoreApplication.translate("Dialog_NewRest", u"Busy", None))
        self.button_choice_3.setText(QCoreApplication.translate("Dialog_NewRest", u"Fall Ill ", None))
        self.button_choice_4.setText(QCoreApplication.translate("Dialog_NewRest", u"Be Injured", None))
        self.label_10.setText("")
        self.label_9.setText("")
        self.label_4.setText(QCoreApplication.translate("Dialog_NewRest", u"Rest Day Title", None))
        self.label_2.setText(QCoreApplication.translate("Dialog_NewRest", u"Set Display Color", None))
        self.label_3.setText(QCoreApplication.translate("Dialog_NewRest", u"Date Setting", None))
        self.button_date_setting.setText(QCoreApplication.translate("Dialog_NewRest", u"2025-05-16", None))
        self.label_fitness_go_3.setText("")
        self.label_5.setText(QCoreApplication.translate("Dialog_NewRest", u"Attention: Represents the display color of this rest day label\n"
" on the calendar", None))
        self.button_save.setText(QCoreApplication.translate("Dialog_NewRest", u"Save", None))
        self.button_return.setText(QCoreApplication.translate("Dialog_NewRest", u"Return", None))
    # retranslateUi

