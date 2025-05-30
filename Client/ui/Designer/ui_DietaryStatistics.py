# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FitMind_Client_DietaryStatistics.ui'
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
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
from ..res_rc import *

class Ui_Widget_DietaryStatistics(object):
    def setupUi(self, Widget_DietaryStatistics):
        if not Widget_DietaryStatistics.objectName():
            Widget_DietaryStatistics.setObjectName(u"Widget_DietaryStatistics")
        Widget_DietaryStatistics.resize(362, 700)
        Widget_DietaryStatistics.setMinimumSize(QSize(300, 666))
        self.verticalLayout_8 = QVBoxLayout(Widget_DietaryStatistics)
        self.verticalLayout_8.setSpacing(6)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Widget_DietaryStatistics)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"#frame{\n"
"			border-top-right-radius:20px;\n"
"	border-top-left-radius:20px;\n"
"	border-bottom-right-radius:20px;\n"
"	border-bottom-left-radius:20px;\n"
"	background-color: qlineargradient(spread:pad, x1:0.477, y1:0, x2:0.5, y2:1, stop:0 rgba(246, 246, 246, 255), stop:1 rgba(231, 213, 200, 255));\n"
"}")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_head = QFrame(self.frame)
        self.frame_head.setObjectName(u"frame_head")
        self.frame_head.setStyleSheet(u"QFrame{\n"
"background-color:transparent;\n"
"}")
        self.frame_head.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_head.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_head)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.button_return = QPushButton(self.frame_head)
        self.button_return.setObjectName(u"button_return")
        self.button_return.setMaximumSize(QSize(60, 16777215))
        self.button_return.setStyleSheet(u"QPushButton{\n"
"background-color:transparent;\n"
"border:none;\n"
"padding:6px;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/icon/back.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_return.setIcon(icon)
        self.button_return.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.button_return)

        self.label = QLabel(self.frame_head)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label)

        self.button_quickSelect = QPushButton(self.frame_head)
        self.button_quickSelect.setObjectName(u"button_quickSelect")
        self.button_quickSelect.setMinimumSize(QSize(24, 24))
        self.button_quickSelect.setMaximumSize(QSize(90, 16777215))
        self.button_quickSelect.setStyleSheet(u"QPushButton{\n"
"background-color:rgb(199, 199, 199);\n"
"border-radius:6px;\n"
"padding:6px;\n"
"margin-right:12px\n"
"}")
        self.button_quickSelect.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.button_quickSelect)


        self.verticalLayout_5.addLayout(self.horizontalLayout)


        self.verticalLayout_6.addWidget(self.frame_head)

        self.frame_body = QFrame(self.frame)
        self.frame_body.setObjectName(u"frame_body")
        self.frame_body.setStyleSheet(u"QFrame{\n"
"background-color:transparent;\n"
"}")
        self.frame_body.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_body.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_body)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_standardIntake = QLabel(self.frame_body)
        self.label_standardIntake.setObjectName(u"label_standardIntake")
        self.label_standardIntake.setStyleSheet(u"QLabel{\n"
"font-size:27px;\n"
"}")

        self.horizontalLayout_2.addWidget(self.label_standardIntake)

        self.label_3 = QLabel(self.frame_body)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"QLabel{\n"
"font-size:18px;\n"
"color:rgb(130, 130, 130)\n"
"}")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.horizontalLayout_2.setStretch(1, 9)

        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.frame_body)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"QLabel{\n"
"font-size:15px;\n"
"color:rgb(154, 154, 154);\n"
"}")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.label_totalKcal = QLabel(self.frame_body)
        self.label_totalKcal.setObjectName(u"label_totalKcal")
        self.label_totalKcal.setStyleSheet(u"QLabel{\n"
"font-size:15px;\n"
"color:rgb(154, 154, 154);\n"
"}")

        self.horizontalLayout_3.addWidget(self.label_totalKcal)

        self.label_5 = QLabel(self.frame_body)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"QLabel{\n"
"font-size:15px;\n"
"color:rgb(154, 154, 154);\n"
"}")

        self.horizontalLayout_3.addWidget(self.label_5)

        self.horizontalLayout_3.setStretch(2, 9)

        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 0, 180, -1)
        self.button_startDate = QPushButton(self.frame_body)
        self.button_startDate.setObjectName(u"button_startDate")
        self.button_startDate.setStyleSheet(u"QPushButton{\n"
"font-size:15px;\n"
"border-radius:6px;\n"
"color:rgb(100, 100, 100);\n"
"background-color:rgb(195, 195, 195);\n"
"padding:6px;\n"
"}")

        self.horizontalLayout_4.addWidget(self.button_startDate)

        self.label_6 = QLabel(self.frame_body)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"QLabel{\n"
"font-size:21px;\n"
"color:rgb(100,100,100);\n"
"}")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_6)

        self.button_endDate = QPushButton(self.frame_body)
        self.button_endDate.setObjectName(u"button_endDate")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_endDate.sizePolicy().hasHeightForWidth())
        self.button_endDate.setSizePolicy(sizePolicy)
        self.button_endDate.setMinimumSize(QSize(0, 20))
        self.button_endDate.setStyleSheet(u"QPushButton{\n"
"font-size:15px;\n"
"border-radius:6px;\n"
"color:rgb(100, 100, 100);\n"
"background-color:rgb(195, 195, 195);\n"
"padding:6px;\n"
"}")

        self.horizontalLayout_4.addWidget(self.button_endDate)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.frame_2 = QFrame(self.frame_body)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"QFrame{\n"
"background-color:transparent;\n"
"}")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"QFrame{\n"
"background-color:transparent;\n"
"}")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_3)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_AveProteinNum = QLabel(self.frame_3)
        self.label_AveProteinNum.setObjectName(u"label_AveProteinNum")
        self.label_AveProteinNum.setStyleSheet(u"QLabel{\n"
"font-size:21px;\n"
"}")
        self.label_AveProteinNum.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label_AveProteinNum)

        self.label_7 = QLabel(self.frame_3)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_5.addWidget(self.label_7)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.label_8 = QLabel(self.frame_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"QLabel{\n"
"	color:rgb(100,100,100);\n"
"}")
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_8)


        self.verticalLayout_7.addLayout(self.verticalLayout)


        self.horizontalLayout_8.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"QFrame{\n"
"background-color:transparent;\n"
"}")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_4)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_AveCHO = QLabel(self.frame_4)
        self.label_AveCHO.setObjectName(u"label_AveCHO")
        self.label_AveCHO.setStyleSheet(u"QLabel{\n"
"font-size:21px;\n"
"}")
        self.label_AveCHO.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.label_AveCHO)

        self.label_10 = QLabel(self.frame_4)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_6.addWidget(self.label_10)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.label_11 = QLabel(self.frame_4)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"QLabel{\n"
"	color:rgb(100,100,100);\n"
"}")
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_11)


        self.verticalLayout_9.addLayout(self.verticalLayout_2)


        self.horizontalLayout_8.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"QFrame{\n"
"background-color:transparent;\n"
"}")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_5)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_AveFat = QLabel(self.frame_5)
        self.label_AveFat.setObjectName(u"label_AveFat")
        self.label_AveFat.setStyleSheet(u"QLabel{\n"
"font-size:21px;\n"
"}")
        self.label_AveFat.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_AveFat)

        self.label_13 = QLabel(self.frame_5)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_7.addWidget(self.label_13)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        self.label_14 = QLabel(self.frame_5)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"QLabel{\n"
"	color:rgb(100,100,100);\n"
"}")
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_14)


        self.verticalLayout_10.addLayout(self.verticalLayout_3)


        self.horizontalLayout_8.addWidget(self.frame_5)


        self.verticalLayout_4.addWidget(self.frame_2)

        self.label_4 = QLabel(self.frame_body)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"QLabel {\n"
"    qproperty-wordWrap: true;\n"
"	color:rgb(100,100,100);\n"
"	margin-top:20px;\n"
"}\n"
"")

        self.verticalLayout_4.addWidget(self.label_4)


        self.verticalLayout_6.addWidget(self.frame_body)

        self.frame_none = QFrame(self.frame)
        self.frame_none.setObjectName(u"frame_none")
        self.frame_none.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_none.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_6.addWidget(self.frame_none)

        self.verticalLayout_6.setStretch(0, 1)
        self.verticalLayout_6.setStretch(1, 8)
        self.verticalLayout_6.setStretch(2, 20)

        self.verticalLayout_8.addWidget(self.frame)


        self.retranslateUi(Widget_DietaryStatistics)
        self.button_return.clicked.connect(Widget_DietaryStatistics.close)

        QMetaObject.connectSlotsByName(Widget_DietaryStatistics)
    # setupUi

    def retranslateUi(self, Widget_DietaryStatistics):
        Widget_DietaryStatistics.setWindowTitle(QCoreApplication.translate("Widget_DietaryStatistics", u"Form", None))
        self.button_return.setText("")
        self.label.setText(QCoreApplication.translate("Widget_DietaryStatistics", u"Dietary  Statistics", None))
        self.button_quickSelect.setText(QCoreApplication.translate("Widget_DietaryStatistics", u"Quick Select", None))
        self.label_standardIntake.setText(QCoreApplication.translate("Widget_DietaryStatistics", u"1240", None))
        self.label_3.setText(QCoreApplication.translate("Widget_DietaryStatistics", u"kcal/day", None))
        self.label_2.setText(QCoreApplication.translate("Widget_DietaryStatistics", u"Calories:", None))
        self.label_totalKcal.setText(QCoreApplication.translate("Widget_DietaryStatistics", u"1130", None))
        self.label_5.setText(QCoreApplication.translate("Widget_DietaryStatistics", u"kacl", None))
        self.button_startDate.setText(QCoreApplication.translate("Widget_DietaryStatistics", u"5.26", None))
        self.label_6.setText(QCoreApplication.translate("Widget_DietaryStatistics", u"-", None))
        self.button_endDate.setText(QCoreApplication.translate("Widget_DietaryStatistics", u"6.1", None))
        self.label_AveProteinNum.setText(QCoreApplication.translate("Widget_DietaryStatistics", u"0", None))
        self.label_7.setText(QCoreApplication.translate("Widget_DietaryStatistics", u"g", None))
        self.label_8.setText(QCoreApplication.translate("Widget_DietaryStatistics", u"Ave Pro", None))
        self.label_AveCHO.setText(QCoreApplication.translate("Widget_DietaryStatistics", u"0", None))
        self.label_10.setText(QCoreApplication.translate("Widget_DietaryStatistics", u"g", None))
        self.label_11.setText(QCoreApplication.translate("Widget_DietaryStatistics", u"Ave CH\u2082O", None))
        self.label_AveFat.setText(QCoreApplication.translate("Widget_DietaryStatistics", u"0", None))
        self.label_13.setText(QCoreApplication.translate("Widget_DietaryStatistics", u"g", None))
        self.label_14.setText(QCoreApplication.translate("Widget_DietaryStatistics", u"Ave Fat", None))
        self.label_4.setText(QCoreApplication.translate("Widget_DietaryStatistics", u"Explanation: The dates on which data are available for average calories, total calories, average protein, average carbohydrates, and average fat.", None))
    # retranslateUi

