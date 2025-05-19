# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FitMind_Client_NewAerobic.ui'
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

class Ui_NewAerobicDialog(object):
    def setupUi(self, NewAerobicDialog):
        if not NewAerobicDialog.objectName():
            NewAerobicDialog.setObjectName(u"NewAerobicDialog")
        NewAerobicDialog.resize(362, 700)
        NewAerobicDialog.setMinimumSize(QSize(300, 666))
        self.horizontalLayout = QHBoxLayout(NewAerobicDialog)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(NewAerobicDialog)
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
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 362, 646))
        self.frame_5 = QFrame(self.scrollAreaWidgetContents)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(10, 50, 350, 55))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy1)
        self.frame_5.setMinimumSize(QSize(350, 55))
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.lineEdit_Aerobic_name = QLineEdit(self.frame_5)
        self.lineEdit_Aerobic_name.setObjectName(u"lineEdit_Aerobic_name")

        self.horizontalLayout_4.addWidget(self.lineEdit_Aerobic_name)

        self.frame_3 = QFrame(self.scrollAreaWidgetContents)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(10, 310, 350, 55))
        sizePolicy1.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy1)
        self.frame_3.setMinimumSize(QSize(350, 55))
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(-1, 0, -1, 0)
        self.icon_training_date = QLabel(self.frame_3)
        self.icon_training_date.setObjectName(u"icon_training_date")

        self.horizontalLayout_8.addWidget(self.icon_training_date)

        self.Training_date = QLabel(self.frame_3)
        self.Training_date.setObjectName(u"Training_date")

        self.horizontalLayout_8.addWidget(self.Training_date)

        self.label_fitness_move = QLabel(self.frame_3)
        self.label_fitness_move.setObjectName(u"label_fitness_move")
        self.label_fitness_move.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_8.addWidget(self.label_fitness_move)

        self.button_trainging_date = QPushButton(self.frame_3)
        self.button_trainging_date.setObjectName(u"button_trainging_date")
        self.button_trainging_date.setStyleSheet(u"QPushButton {\n"
"    color:  #808080;              /* \u767d\u8272\u6587\u5b57 */\n"
"    border: none;             /* \u79fb\u9664\u9ed8\u8ba4\u8fb9\u6846 */\n"
"    padding: 6px 12px;        /* \u5185\u8fb9\u8ddd\uff08\u6587\u5b57\u4e0e\u8fb9\u7f18\u95f4\u8ddd\uff09 */\n"
"    font-size: 12px;          /* \u6587\u5b57\u5927\u5c0f */\n"
"}")

        self.horizontalLayout_8.addWidget(self.button_trainging_date)

        self.horizontalLayout_8.setStretch(2, 2)
        self.frame_4 = QFrame(self.scrollAreaWidgetContents)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(10, 380, 350, 55))
        sizePolicy1.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy1)
        self.frame_4.setMinimumSize(QSize(350, 55))
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, 0, -1, 0)
        self.label_4 = QLabel(self.frame_4)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_9.addWidget(self.label_4)

        self.button_complete = QPushButton(self.frame_4)
        self.button_complete.setObjectName(u"button_complete")
        self.button_complete.setStyleSheet(u"QPushButton {\n"
"    color: #2a7fff;              /* \u767d\u8272\u6587\u5b57 */\n"
"    border: none;             /* \u79fb\u9664\u9ed8\u8ba4\u8fb9\u6846 */\n"
"    border-radius: 8px;       /* \u5706\u89d2\u534a\u5f84\uff08\u53ef\u8c03\u6574\uff09 */\n"
"    padding: 6px 12px;        /* \u5185\u8fb9\u8ddd\uff08\u6587\u5b57\u4e0e\u8fb9\u7f18\u95f4\u8ddd\uff09 */\n"
"    font-size: 14px;          /* \u6587\u5b57\u5927\u5c0f */\n"
"}")

        self.horizontalLayout_9.addWidget(self.button_complete)

        self.label_6 = QLabel(self.frame_4)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_9.addWidget(self.label_6)

        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 120, 151, 41))
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
        self.frame_6 = QFrame(self.scrollAreaWidgetContents)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(10, 240, 350, 55))
        sizePolicy1.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy1)
        self.frame_6.setMinimumSize(QSize(350, 55))
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(-1, 0, -1, 0)
        self.icon_time_setting = QLabel(self.frame_6)
        self.icon_time_setting.setObjectName(u"icon_time_setting")

        self.horizontalLayout_7.addWidget(self.icon_time_setting)

        self.Time_setting = QLabel(self.frame_6)
        self.Time_setting.setObjectName(u"Time_setting")

        self.horizontalLayout_7.addWidget(self.Time_setting)

        self.label_walk_move_2 = QLabel(self.frame_6)
        self.label_walk_move_2.setObjectName(u"label_walk_move_2")

        self.horizontalLayout_7.addWidget(self.label_walk_move_2)

        self.button_time_setting = QPushButton(self.frame_6)
        self.button_time_setting.setObjectName(u"button_time_setting")
        self.button_time_setting.setStyleSheet(u"QPushButton {\n"
"    color:  #808080;              /* \u767d\u8272\u6587\u5b57 */\n"
"    border: none;             /* \u79fb\u9664\u9ed8\u8ba4\u8fb9\u6846 */\n"
"    padding: 6px 12px;        /* \u5185\u8fb9\u8ddd\uff08\u6587\u5b57\u4e0e\u8fb9\u7f18\u95f4\u8ddd\uff09 */\n"
"    font-size: 12px;          /* \u6587\u5b57\u5927\u5c0f */\n"
"}")

        self.horizontalLayout_7.addWidget(self.button_time_setting)

        self.horizontalLayout_7.setStretch(2, 2)
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
        self.frame_7 = QFrame(self.scrollAreaWidgetContents)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(10, 170, 350, 55))
        sizePolicy1.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy1)
        self.frame_7.setMinimumSize(QSize(350, 55))
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(-1, 0, -1, 0)
        self.icon_type_selection = QLabel(self.frame_7)
        self.icon_type_selection.setObjectName(u"icon_type_selection")

        self.horizontalLayout_10.addWidget(self.icon_type_selection)

        self.type_selections = QLabel(self.frame_7)
        self.type_selections.setObjectName(u"type_selections")

        self.horizontalLayout_10.addWidget(self.type_selections)

        self.label_walk_move_3 = QLabel(self.frame_7)
        self.label_walk_move_3.setObjectName(u"label_walk_move_3")

        self.horizontalLayout_10.addWidget(self.label_walk_move_3)

        self.button_type_selection = QPushButton(self.frame_7)
        self.button_type_selection.setObjectName(u"button_type_selection")
        self.button_type_selection.setStyleSheet(u"QPushButton {\n"
"    color:  #808080;              /* \u767d\u8272\u6587\u5b57 */\n"
"    border: none;             /* \u79fb\u9664\u9ed8\u8ba4\u8fb9\u6846 */\n"
"    padding: 6px 12px;        /* \u5185\u8fb9\u8ddd\uff08\u6587\u5b57\u4e0e\u8fb9\u7f18\u95f4\u8ddd\uff09 */\n"
"    font-size: 12px;          /* \u6587\u5b57\u5927\u5c0f */\n"
"}")

        self.horizontalLayout_10.addWidget(self.button_type_selection)

        self.horizontalLayout_10.setStretch(2, 2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_3.addWidget(self.scrollArea)

        self.button_start = QPushButton(self.frame)
        self.button_start.setObjectName(u"button_start")
        self.button_start.setGeometry(QRect(280, 10, 75, 24))
        self.button_start.setStyleSheet(u"QPushButton {\n"
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


        self.retranslateUi(NewAerobicDialog)
        self.button_return.clicked.connect(NewAerobicDialog.close)

        QMetaObject.connectSlotsByName(NewAerobicDialog)
    # setupUi

    def retranslateUi(self, NewAerobicDialog):
        NewAerobicDialog.setWindowTitle(QCoreApplication.translate("NewAerobicDialog", u"Dialog", None))
        self.lineEdit_Aerobic_name.setPlaceholderText(QCoreApplication.translate("NewAerobicDialog", u"Click to enter a name...", None))
        self.icon_training_date.setText("")
        self.Training_date.setText(QCoreApplication.translate("NewAerobicDialog", u"Training Date", None))
        self.label_fitness_move.setText("")
        self.button_trainging_date.setText(QCoreApplication.translate("NewAerobicDialog", u"2025-5-17", None))
        self.label_4.setText("")
        self.button_complete.setText(QCoreApplication.translate("NewAerobicDialog", u"Complete training directly", None))
        self.label_6.setText("")
        self.label.setText(QCoreApplication.translate("NewAerobicDialog", u"Training Settings", None))
        self.icon_time_setting.setText("")
        self.Time_setting.setText(QCoreApplication.translate("NewAerobicDialog", u"Time Setting", None))
        self.label_walk_move_2.setText("")
        self.button_time_setting.setText(QCoreApplication.translate("NewAerobicDialog", u"1 minute  >", None))
        self.aerobic_name.setText(QCoreApplication.translate("NewAerobicDialog", u"Aerobic Name", None))
        self.icon_type_selection.setText("")
        self.type_selections.setText(QCoreApplication.translate("NewAerobicDialog", u"Type Selection", None))
        self.label_walk_move_3.setText("")
        self.button_type_selection.setText(QCoreApplication.translate("NewAerobicDialog", u"Uniform Aerobic  >", None))
        self.button_start.setText(QCoreApplication.translate("NewAerobicDialog", u"Start", None))
        self.button_return.setText(QCoreApplication.translate("NewAerobicDialog", u"Return", None))
    # retranslateUi

