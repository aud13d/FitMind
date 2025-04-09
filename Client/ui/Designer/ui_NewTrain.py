# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FitMind_Client_NewTrain.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QToolButton,
    QVBoxLayout, QWidget)


class Ui_Widget_NewTrain(object):
    def setupUi(self, Widget_NewTrain):
        if not Widget_NewTrain.objectName():
            Widget_NewTrain.setObjectName(u"Widget_NewTrain")
        Widget_NewTrain.resize(362, 700)
        Widget_NewTrain.setMinimumSize(QSize(300, 666))
        self.horizontalLayout_2 = QHBoxLayout(Widget_NewTrain)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(Widget_NewTrain)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"#frame_2{\n"
"	background-color:qlineargradient(spread:pad, x1:0.518, y1:1, x2:0.514, y2:0.00227273, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255))\n"
"}")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_2.setLineWidth(0)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.frame_2)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet(u"QLineEdit {\n"
"    font: 9pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"    border: none; /* \u79fb\u9664\u6240\u6709\u8fb9\u6846 */\n"
"    background-color: rgba(255, 255, 255, 0); /* \u534a\u900f\u660e\u80cc\u666f */\n"
"    padding: 5px 8px; /* \u9002\u5f53\u7684\u5185\u8fb9\u8ddd */\n"
"    color: #999999; /* \u5f85\u673a\u72b6\u6001\u5b57\u4f53\u989c\u8272\uff1a\u6d45\u7070\u8272 */\n"
"    selection-background-color: #a8d8ff; /* \u9009\u4e2d\u6587\u5b57\u7684\u80cc\u666f */\n"
"    transition: border-bottom 0.3s ease-in-out, color 0.3s ease-in-out; /* \u6dfb\u52a0\u989c\u8272\u6e10\u53d8 */\n"
"}\n"
"\n"
"\n"
"")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, -1, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, -1, 190, 30)
        self.label_newtrain_time = QLabel(self.frame)
        self.label_newtrain_time.setObjectName(u"label_newtrain_time")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_newtrain_time.sizePolicy().hasHeightForWidth())
        self.label_newtrain_time.setSizePolicy(sizePolicy1)
        self.label_newtrain_time.setMinimumSize(QSize(70, 30))
        self.label_newtrain_time.setMaximumSize(QSize(0, 0))
        self.label_newtrain_time.setStyleSheet(u"font: 700 18pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"")
        self.label_newtrain_time.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_newtrain_time)

        self.button_newtrain_start = QPushButton(self.frame)
        self.button_newtrain_start.setObjectName(u"button_newtrain_start")
        sizePolicy1.setHeightForWidth(self.button_newtrain_start.sizePolicy().hasHeightForWidth())
        self.button_newtrain_start.setSizePolicy(sizePolicy1)
        self.button_newtrain_start.setMinimumSize(QSize(30, 30))
        self.button_newtrain_start.setMaximumSize(QSize(0, 0))
        self.button_newtrain_start.setStyleSheet(u"QPushButton {\n"
"    font: 9pt \"\u5fae\u8f6f\u96c5\u9ed1\"; \n"
"    border: 1px solid #ccc; /* \u7ec6\u8fb9\u6846 */\n"
"    border-radius: 12px; /* \u8f7b\u5fae\u5706\u89d2 */\n"
"    background-color: white; /* \u7eaf\u767d\u80cc\u666f */\n"
"    color: black; /* \u9ed1\u8272\u6587\u5b57 */\n"
"	border:none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #f0f0f0; /* \u6d45\u7070\u8272\u60ac\u6d6e\u6548\u679c */\n"
"    padding-bottom: 2px; /* \u8f7b\u5fae\u4e0b\u79fb\uff0c\u589e\u52a0\u6309\u538b\u611f */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #e0e0e0; /* \u66f4\u6df1\u7684\u7070\u8272\uff0c\u6309\u4e0b\u6548\u679c */\n"
"    padding-bottom: 1px;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #f8f8f8;\n"
"    color: gray;\n"
"    border-color: #ddd;\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u":/icons/icon/kaishi.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_newtrain_start.setIcon(icon)

        self.horizontalLayout_3.addWidget(self.button_newtrain_start)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)

        self.button_newtrain_finish = QPushButton(self.frame)
        self.button_newtrain_finish.setObjectName(u"button_newtrain_finish")
        self.button_newtrain_finish.setMinimumSize(QSize(10, 20))
        self.button_newtrain_finish.setMaximumSize(QSize(60, 30))
        self.button_newtrain_finish.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.button_newtrain_finish.setStyleSheet(u"QPushButton {\n"
"    font: 700 9pt \"\u5fae\u8f6f\u96c5\u9ed1\"; \n"
"    border: 1px solid #ccc; /* \u7ec6\u8fb9\u6846 */\n"
"    border-radius: 9px; /* \u8f7b\u5fae\u5706\u89d2 */\n"
"    background-color: rgb(0, 85, 255); /* \u7eaf\u767d\u80cc\u666f */\n"
"    color: white; /* \u9ed1\u8272\u6587\u5b57 */\n"
"	border:none;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(0, 95, 255); /* \u6d45\u7070\u8272\u60ac\u6d6e\u6548\u679c */\n"
"    padding-bottom: 2px; /* \u8f7b\u5fae\u4e0b\u79fb\uff0c\u589e\u52a0\u6309\u538b\u611f */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(0, 105, 255); /* \u66f4\u6df1\u7684\u7070\u8272\uff0c\u6309\u4e0b\u6548\u679c */\n"
"    padding-bottom: 1px;\n"
"}\n"
"\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #f0f0f0;\n"
"    border-color: #ddd;\n"
"}\n"
"")
        self.button_newtrain_finish.setInputMethodHints(Qt.InputMethodHint.ImhDate)

        self.horizontalLayout_4.addWidget(self.button_newtrain_finish)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.lineEdit_newtrain_trainging_title = QLineEdit(self.frame)
        self.lineEdit_newtrain_trainging_title.setObjectName(u"lineEdit_newtrain_trainging_title")
        self.lineEdit_newtrain_trainging_title.setMinimumSize(QSize(100, 40))
        self.lineEdit_newtrain_trainging_title.setStyleSheet(u"    background-image: url(:Images/search.svg); /* actual size, e.g. 16x16 */\n"
"    background-repeat: no-repeat;\n"
"    background-position: left;")
        self.lineEdit_newtrain_trainging_title.setCursorMoveStyle(Qt.CursorMoveStyle.LogicalMoveStyle)

        self.verticalLayout_2.addWidget(self.lineEdit_newtrain_trainging_title)


        self.verticalLayout.addWidget(self.frame)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(9)
        sizePolicy2.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy2)
        self.frame_4.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-top-right-radius:20px;\n"
"	border-top-left-radius:20px;\n"
"	border:none\n"
"}")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_4.setLineWidth(0)

        self.verticalLayout.addWidget(self.frame_4)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy3)
        self.frame_3.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border:none\n"
"}\n"
"\n"
"QToolButton {\n"
"    font: 9pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"    border-radius: 6px; /* \u8f7b\u5fae\u5706\u89d2 */\n"
"    background-color: white; /* \u7eaf\u767d\u80cc\u666f */\n"
"    color: black; /* \u9ed1\u8272\u6587\u5b57 */\n"
"    min-width: 60px;\n"
"    min-height: 25px;\n"
"\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"    background-color: #f0f0f0; /* \u6d45\u7070\u8272\u60ac\u6d6e\u6548\u679c */\n"
"    margin-top: 2px; /* \u8f7b\u5fae\u4e0b\u79fb\uff0c\u589e\u52a0\u6309\u538b\u611f */\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: #e0e0e0; /* \u6309\u4e0b\u65f6\u53d8\u6df1\u7070 */\n"
"    margin-top: 1px; /* \u6309\u4e0b\u65f6\u8f7b\u5fae\u4e0a\u79fb */\n"
"}\n"
"\n"
"QToolButton:disabled {\n"
"    background-color: #f8f8f8;\n"
"    color: gray;\n"
"    border-color: #ddd;\n"
"}\n"
"\n"
"")
        self.frame_3.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.button_newtrain_minimize = QToolButton(self.frame_3)
        self.button_newtrain_minimize.setObjectName(u"button_newtrain_minimize")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.button_newtrain_minimize.sizePolicy().hasHeightForWidth())
        self.button_newtrain_minimize.setSizePolicy(sizePolicy4)
        icon1 = QIcon()
        icon1.addFile(u":/icons/icon/zuixiaohua.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_newtrain_minimize.setIcon(icon1)
        self.button_newtrain_minimize.setIconSize(QSize(20, 20))
        self.button_newtrain_minimize.setCheckable(False)
        self.button_newtrain_minimize.setChecked(False)
        self.button_newtrain_minimize.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.horizontalLayout.addWidget(self.button_newtrain_minimize)

        self.button_newtrain_add_action = QToolButton(self.frame_3)
        self.button_newtrain_add_action.setObjectName(u"button_newtrain_add_action")
        sizePolicy4.setHeightForWidth(self.button_newtrain_add_action.sizePolicy().hasHeightForWidth())
        self.button_newtrain_add_action.setSizePolicy(sizePolicy4)
        icon2 = QIcon()
        icon2.addFile(u":/icons/icon/tianjia.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_newtrain_add_action.setIcon(icon2)
        self.button_newtrain_add_action.setIconSize(QSize(20, 20))
        self.button_newtrain_add_action.setCheckable(False)
        self.button_newtrain_add_action.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.horizontalLayout.addWidget(self.button_newtrain_add_action)

        self.button_newtrain_experience = QToolButton(self.frame_3)
        self.button_newtrain_experience.setObjectName(u"button_newtrain_experience")
        sizePolicy4.setHeightForWidth(self.button_newtrain_experience.sizePolicy().hasHeightForWidth())
        self.button_newtrain_experience.setSizePolicy(sizePolicy4)
        icon3 = QIcon()
        icon3.addFile(u":/icons/icon/xinde-.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_newtrain_experience.setIcon(icon3)
        self.button_newtrain_experience.setIconSize(QSize(20, 20))
        self.button_newtrain_experience.setCheckable(False)
        self.button_newtrain_experience.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.horizontalLayout.addWidget(self.button_newtrain_experience)

        self.button_newtrain_setting = QToolButton(self.frame_3)
        self.button_newtrain_setting.setObjectName(u"button_newtrain_setting")
        sizePolicy4.setHeightForWidth(self.button_newtrain_setting.sizePolicy().hasHeightForWidth())
        self.button_newtrain_setting.setSizePolicy(sizePolicy4)
        icon4 = QIcon()
        icon4.addFile(u":/icons/icon/shezhi.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_newtrain_setting.setIcon(icon4)
        self.button_newtrain_setting.setIconSize(QSize(20, 20))
        self.button_newtrain_setting.setCheckable(False)
        self.button_newtrain_setting.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.horizontalLayout.addWidget(self.button_newtrain_setting)


        self.verticalLayout.addWidget(self.frame_3)


        self.horizontalLayout_2.addWidget(self.frame_2)


        self.retranslateUi(Widget_NewTrain)

        QMetaObject.connectSlotsByName(Widget_NewTrain)
    # setupUi

    def retranslateUi(self, Widget_NewTrain):
        Widget_NewTrain.setWindowTitle(QCoreApplication.translate("Widget_NewTrain", u"Form", None))
        self.label_newtrain_time.setText(QCoreApplication.translate("Widget_NewTrain", u"00:00", None))
        self.button_newtrain_start.setText("")
        self.button_newtrain_finish.setText(QCoreApplication.translate("Widget_NewTrain", u"Finish", None))
        self.lineEdit_newtrain_trainging_title.setText("")
        self.lineEdit_newtrain_trainging_title.setPlaceholderText(QCoreApplication.translate("Widget_NewTrain", u"Click to enter training title", None))
        self.button_newtrain_minimize.setText(QCoreApplication.translate("Widget_NewTrain", u"minimize", None))
        self.button_newtrain_add_action.setText(QCoreApplication.translate("Widget_NewTrain", u"add action", None))
        self.button_newtrain_experience.setText(QCoreApplication.translate("Widget_NewTrain", u"experience", None))
        self.button_newtrain_setting.setText(QCoreApplication.translate("Widget_NewTrain", u"setting", None))
    # retranslateUi

