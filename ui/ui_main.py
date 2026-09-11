# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainCcWnHG.ui'
##
## Created by: Qt User Interface Compiler version 6.11.2
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QPlainTextEdit, QProgressBar, QPushButton,
    QSizePolicy, QSpinBox, QTabWidget, QTextBrowser,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(840, 599)
        self.verticalLayout_6 = QVBoxLayout(Form)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tab_piano = QWidget()
        self.tab_piano.setObjectName(u"tab_piano")
        self.verticalLayout_2 = QVBoxLayout(self.tab_piano)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.textBrowser = QTextBrowser(self.tab_piano)
        self.textBrowser.setObjectName(u"textBrowser")

        self.verticalLayout_2.addWidget(self.textBrowser)

        self.line = QFrame(self.tab_piano)
        self.line.setObjectName(u"line")
        self.line.setFrameShadow(QFrame.Shadow.Plain)
        self.line.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout_2.addWidget(self.line)

        self.tabWidget_2 = QTabWidget(self.tab_piano)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.horizontalLayout_8 = QHBoxLayout(self.tab)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.label_2)

        self.comboBox = QComboBox(self.tab)
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout.addWidget(self.comboBox)


        self.verticalLayout_8.addLayout(self.horizontalLayout)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_10 = QLabel(self.tab)
        self.label_10.setObjectName(u"label_10")
        sizePolicy1.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy1)

        self.gridLayout_4.addWidget(self.label_10, 0, 0, 1, 1)

        self.doubleSpinBox_3 = QDoubleSpinBox(self.tab)
        self.doubleSpinBox_3.setObjectName(u"doubleSpinBox_3")
        self.doubleSpinBox_3.setMaximum(1.000000000000000)
        self.doubleSpinBox_3.setSingleStep(0.050000000000000)

        self.gridLayout_4.addWidget(self.doubleSpinBox_3, 0, 1, 1, 1)

        self.label_11 = QLabel(self.tab)
        self.label_11.setObjectName(u"label_11")
        sizePolicy1.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy1)

        self.gridLayout_4.addWidget(self.label_11, 1, 0, 1, 1)

        self.doubleSpinBox_2 = QDoubleSpinBox(self.tab)
        self.doubleSpinBox_2.setObjectName(u"doubleSpinBox_2")
        self.doubleSpinBox_2.setMaximum(1.000000000000000)
        self.doubleSpinBox_2.setSingleStep(0.050000000000000)

        self.gridLayout_4.addWidget(self.doubleSpinBox_2, 1, 1, 1, 1)


        self.verticalLayout_8.addLayout(self.gridLayout_4)


        self.horizontalLayout_8.addLayout(self.verticalLayout_8)

        self.line_9 = QFrame(self.tab)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShadow(QFrame.Shadow.Plain)
        self.line_9.setFrameShape(QFrame.Shape.VLine)

        self.horizontalLayout_8.addWidget(self.line_9)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_13 = QLabel(self.tab)
        self.label_13.setObjectName(u"label_13")
        sizePolicy1.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy1)
        self.label_13.setTextFormat(Qt.TextFormat.AutoText)

        self.horizontalLayout_9.addWidget(self.label_13)

        self.comboBox_3 = QComboBox(self.tab)
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.horizontalLayout_9.addWidget(self.comboBox_3)

        self.pushButton_2 = QPushButton(self.tab)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy2)

        self.horizontalLayout_9.addWidget(self.pushButton_2)


        self.verticalLayout.addLayout(self.horizontalLayout_9)

        self.label_14 = QLabel(self.tab)
        self.label_14.setObjectName(u"label_14")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy3)

        self.verticalLayout.addWidget(self.label_14)


        self.verticalLayout_9.addLayout(self.verticalLayout)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_9 = QLabel(self.tab)
        self.label_9.setObjectName(u"label_9")
        sizePolicy1.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy1)

        self.horizontalLayout_12.addWidget(self.label_9)

        self.spinBox_5 = QSpinBox(self.tab)
        self.spinBox_5.setObjectName(u"spinBox_5")
        self.spinBox_5.setMaximum(2147483647)

        self.horizontalLayout_12.addWidget(self.spinBox_5)


        self.verticalLayout_3.addLayout(self.horizontalLayout_12)


        self.verticalLayout_9.addLayout(self.verticalLayout_3)


        self.horizontalLayout_8.addLayout(self.verticalLayout_9)

        self.line_12 = QFrame(self.tab)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setFrameShadow(QFrame.Shadow.Plain)
        self.line_12.setFrameShape(QFrame.Shape.VLine)

        self.horizontalLayout_8.addWidget(self.line_12)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_8 = QLabel(self.tab)
        self.label_8.setObjectName(u"label_8")
        sizePolicy1.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy1)

        self.horizontalLayout_10.addWidget(self.label_8)

        self.spinBox_4 = QSpinBox(self.tab)
        self.spinBox_4.setObjectName(u"spinBox_4")
        self.spinBox_4.setMinimum(1)

        self.horizontalLayout_10.addWidget(self.spinBox_4)


        self.verticalLayout_10.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_12 = QLabel(self.tab)
        self.label_12.setObjectName(u"label_12")
        sizePolicy1.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy1)

        self.horizontalLayout_13.addWidget(self.label_12)

        self.spinBox_6 = QSpinBox(self.tab)
        self.spinBox_6.setObjectName(u"spinBox_6")
        self.spinBox_6.setMaximum(2147483647)

        self.horizontalLayout_13.addWidget(self.spinBox_6)


        self.verticalLayout_10.addLayout(self.horizontalLayout_13)


        self.horizontalLayout_8.addLayout(self.verticalLayout_10)

        self.tabWidget_2.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.horizontalLayout_14 = QHBoxLayout(self.tab_2)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.checkBox = QCheckBox(self.tab_2)
        self.checkBox.setObjectName(u"checkBox")
        sizePolicy3.setHeightForWidth(self.checkBox.sizePolicy().hasHeightForWidth())
        self.checkBox.setSizePolicy(sizePolicy3)
        self.checkBox.setTristate(False)

        self.verticalLayout_11.addWidget(self.checkBox)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_6 = QLabel(self.tab_2)
        self.label_6.setObjectName(u"label_6")
        sizePolicy1.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy1)

        self.horizontalLayout_5.addWidget(self.label_6)

        self.spinBox_3 = QSpinBox(self.tab_2)
        self.spinBox_3.setObjectName(u"spinBox_3")
        sizePolicy3.setHeightForWidth(self.spinBox_3.sizePolicy().hasHeightForWidth())
        self.spinBox_3.setSizePolicy(sizePolicy3)
        self.spinBox_3.setMaximum(2147483647)

        self.horizontalLayout_5.addWidget(self.spinBox_3)


        self.verticalLayout_11.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_5 = QLabel(self.tab_2)
        self.label_5.setObjectName(u"label_5")
        sizePolicy1.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy1)

        self.horizontalLayout_4.addWidget(self.label_5)

        self.doubleSpinBox = QDoubleSpinBox(self.tab_2)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        sizePolicy3.setHeightForWidth(self.doubleSpinBox.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox.setSizePolicy(sizePolicy3)

        self.horizontalLayout_4.addWidget(self.doubleSpinBox)


        self.verticalLayout_11.addLayout(self.horizontalLayout_4)


        self.horizontalLayout_14.addLayout(self.verticalLayout_11)

        self.line_8 = QFrame(self.tab_2)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShadow(QFrame.Shadow.Plain)
        self.line_8.setFrameShape(QFrame.Shape.VLine)

        self.horizontalLayout_14.addWidget(self.line_8)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_7 = QLabel(self.tab_2)
        self.label_7.setObjectName(u"label_7")
        sizePolicy1.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy1)

        self.horizontalLayout_6.addWidget(self.label_7)

        self.lineEdit = QLineEdit(self.tab_2)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy3.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy3)

        self.horizontalLayout_6.addWidget(self.lineEdit)


        self.verticalLayout_12.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self.tab_2)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.label_3)

        self.spinBox = QSpinBox(self.tab_2)
        self.spinBox.setObjectName(u"spinBox")
        sizePolicy3.setHeightForWidth(self.spinBox.sizePolicy().hasHeightForWidth())
        self.spinBox.setSizePolicy(sizePolicy3)

        self.horizontalLayout_2.addWidget(self.spinBox)


        self.verticalLayout_12.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(self.tab_2)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.label_4)

        self.spinBox_2 = QSpinBox(self.tab_2)
        self.spinBox_2.setObjectName(u"spinBox_2")
        sizePolicy3.setHeightForWidth(self.spinBox_2.sizePolicy().hasHeightForWidth())
        self.spinBox_2.setSizePolicy(sizePolicy3)

        self.horizontalLayout_3.addWidget(self.spinBox_2)


        self.verticalLayout_12.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_14.addLayout(self.verticalLayout_12)

        self.tabWidget_2.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.horizontalLayout_15 = QHBoxLayout(self.tab_3)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.checkBox_2 = QCheckBox(self.tab_3)
        self.checkBox_2.setObjectName(u"checkBox_2")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.checkBox_2.sizePolicy().hasHeightForWidth())
        self.checkBox_2.setSizePolicy(sizePolicy4)

        self.verticalLayout_16.addWidget(self.checkBox_2)


        self.horizontalLayout_15.addLayout(self.verticalLayout_16)

        self.line_2 = QFrame(self.tab_3)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShadow(QFrame.Shadow.Plain)
        self.line_2.setFrameShape(QFrame.Shape.VLine)

        self.horizontalLayout_15.addWidget(self.line_2)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_16 = QLabel(self.tab_3)
        self.label_16.setObjectName(u"label_16")
        sizePolicy1.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy1)

        self.horizontalLayout_11.addWidget(self.label_16)

        self.comboBox_2 = QComboBox(self.tab_3)
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.horizontalLayout_11.addWidget(self.comboBox_2)

        self.pushButton_3 = QPushButton(self.tab_3)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy2.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy2)

        self.horizontalLayout_11.addWidget(self.pushButton_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_11)

        self.label_15 = QLabel(self.tab_3)
        self.label_15.setObjectName(u"label_15")
        sizePolicy3.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy3)

        self.verticalLayout_4.addWidget(self.label_15)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_17 = QLabel(self.tab_3)
        self.label_17.setObjectName(u"label_17")
        sizePolicy1.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy1)

        self.horizontalLayout_16.addWidget(self.label_17)

        self.doubleSpinBox_4 = QDoubleSpinBox(self.tab_3)
        self.doubleSpinBox_4.setObjectName(u"doubleSpinBox_4")
        self.doubleSpinBox_4.setMaximum(10.000000000000000)
        self.doubleSpinBox_4.setSingleStep(0.500000000000000)

        self.horizontalLayout_16.addWidget(self.doubleSpinBox_4)


        self.verticalLayout_5.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_18 = QLabel(self.tab_3)
        self.label_18.setObjectName(u"label_18")
        sizePolicy1.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy1)

        self.horizontalLayout_18.addWidget(self.label_18)

        self.doubleSpinBox_5 = QDoubleSpinBox(self.tab_3)
        self.doubleSpinBox_5.setObjectName(u"doubleSpinBox_5")
        self.doubleSpinBox_5.setMaximum(10.000000000000000)
        self.doubleSpinBox_5.setSingleStep(0.500000000000000)

        self.horizontalLayout_18.addWidget(self.doubleSpinBox_5)


        self.verticalLayout_5.addLayout(self.horizontalLayout_18)


        self.horizontalLayout_15.addLayout(self.verticalLayout_5)

        self.line_3 = QFrame(self.tab_3)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShadow(QFrame.Shadow.Plain)
        self.line_3.setFrameShape(QFrame.Shape.VLine)

        self.horizontalLayout_15.addWidget(self.line_3)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_23 = QLabel(self.tab_3)
        self.label_23.setObjectName(u"label_23")
        sizePolicy1.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy1)

        self.horizontalLayout_23.addWidget(self.label_23)

        self.spinBox_8 = QSpinBox(self.tab_3)
        self.spinBox_8.setObjectName(u"spinBox_8")
        self.spinBox_8.setMinimum(-2147483647)
        self.spinBox_8.setMaximum(2147483647)

        self.horizontalLayout_23.addWidget(self.spinBox_8)


        self.verticalLayout_7.addLayout(self.horizontalLayout_23)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_24 = QLabel(self.tab_3)
        self.label_24.setObjectName(u"label_24")
        sizePolicy1.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy1)

        self.horizontalLayout_26.addWidget(self.label_24)

        self.spinBox_9 = QSpinBox(self.tab_3)
        self.spinBox_9.setObjectName(u"spinBox_9")
        self.spinBox_9.setMinimum(-2147483647)
        self.spinBox_9.setMaximum(2147483647)

        self.horizontalLayout_26.addWidget(self.spinBox_9)


        self.verticalLayout_7.addLayout(self.horizontalLayout_26)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_25 = QLabel(self.tab_3)
        self.label_25.setObjectName(u"label_25")
        sizePolicy1.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy1)

        self.horizontalLayout_25.addWidget(self.label_25)

        self.spinBox_10 = QSpinBox(self.tab_3)
        self.spinBox_10.setObjectName(u"spinBox_10")
        self.spinBox_10.setMinimum(-2147483647)
        self.spinBox_10.setMaximum(2147483647)

        self.horizontalLayout_25.addWidget(self.spinBox_10)


        self.verticalLayout_7.addLayout(self.horizontalLayout_25)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_19 = QLabel(self.tab_3)
        self.label_19.setObjectName(u"label_19")
        sizePolicy1.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy1)

        self.horizontalLayout_17.addWidget(self.label_19)

        self.spinBox_7 = QSpinBox(self.tab_3)
        self.spinBox_7.setObjectName(u"spinBox_7")
        self.spinBox_7.setMaximum(2147483647)

        self.horizontalLayout_17.addWidget(self.spinBox_7)


        self.verticalLayout_7.addLayout(self.horizontalLayout_17)

        self.label_20 = QLabel(self.tab_3)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setWordWrap(True)

        self.verticalLayout_7.addWidget(self.label_20)


        self.horizontalLayout_15.addLayout(self.verticalLayout_7)

        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.label = QLabel(self.tab_4)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 151, 51))
        self.tabWidget_2.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.gridLayout_5 = QGridLayout(self.tab_5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_22 = QLabel(self.tab_5)
        self.label_22.setObjectName(u"label_22")

        self.horizontalLayout_22.addWidget(self.label_22)

        self.progressBar = QProgressBar(self.tab_5)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.horizontalLayout_22.addWidget(self.progressBar)


        self.gridLayout_5.addLayout(self.horizontalLayout_22, 1, 2, 1, 1)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_21 = QLabel(self.tab_5)
        self.label_21.setObjectName(u"label_21")
        sizePolicy1.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy1)

        self.horizontalLayout_19.addWidget(self.label_21)

        self.lineEdit_2 = QLineEdit(self.tab_5)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        sizePolicy3.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy3)

        self.horizontalLayout_19.addWidget(self.lineEdit_2)


        self.gridLayout_5.addLayout(self.horizontalLayout_19, 0, 0, 1, 1)

        self.plainTextEdit = QPlainTextEdit(self.tab_5)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.plainTextEdit.sizePolicy().hasHeightForWidth())
        self.plainTextEdit.setSizePolicy(sizePolicy5)
        self.plainTextEdit.setStyleSheet(u"background-color: #333333;\n"
"color: #DCDCDC;\n"
"border:3px solid #cccccc;\n"
"font-family:Consolas;\n"
"font-size:11pt;\n"
"selection-background-color:#355070;\n"
"selection-color:#ffffff;\n"
"")
        self.plainTextEdit.setReadOnly(True)

        self.gridLayout_5.addWidget(self.plainTextEdit, 0, 2, 1, 1)

        self.pushButton = QPushButton(self.tab_5)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy2.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.pushButton, 1, 0, 1, 1)

        self.tabWidget_2.addTab(self.tab_5, "")

        self.verticalLayout_2.addWidget(self.tabWidget_2)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 1)
        self.tabWidget.addTab(self.tab_piano, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.verticalLayout_13 = QVBoxLayout(self.tab_6)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_26 = QLabel(self.tab_6)
        self.label_26.setObjectName(u"label_26")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy6)

        self.horizontalLayout_7.addWidget(self.label_26)

        self.textBrowser_2 = QTextBrowser(self.tab_6)
        self.textBrowser_2.setObjectName(u"textBrowser_2")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.textBrowser_2.sizePolicy().hasHeightForWidth())
        self.textBrowser_2.setSizePolicy(sizePolicy7)

        self.horizontalLayout_7.addWidget(self.textBrowser_2)

        self.horizontalLayout_7.setStretch(0, 1)
        self.horizontalLayout_7.setStretch(1, 1)

        self.verticalLayout_13.addLayout(self.horizontalLayout_7)

        self.tabWidget.addTab(self.tab_6, "")

        self.verticalLayout_6.addWidget(self.tabWidget)


        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Minecraft\u539f\u751f\u52a8\u753b\u751f\u6210\u5668", None))
        self.textBrowser.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:6px; margin-bottom:6px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">\u94a2\u7434\u52a8\u753b\u751f\u6210\u6a21\u5757 \u5e2e\u52a9\u6587\u6863</span></p>\n"
"<p style=\" margin-top:8px; margin-bottom:8px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u8be5\u6a21\u5757\u53ef\u751f\u6210\u7528\u4e8e\u5728 Minecraft \u4e2d\u6f14\u594f MIDI \u94a2\u7434\u66f2\u7684\u52a8"
                        "\u753b\u6570\u636e\u5305\uff0c\u540c\u65f6\u652f\u6301\u65b9\u5757\u629b\u5c04\u7ed8\u753b\u3001\u7434\u952e\u6307\u793a\u5668\u3001\u7011\u5e03\u6d41\u7b49\u9644\u52a0\u7279\u6548\u3002\u5f53\u524d\u7248\u672c\u7a0b\u5e8f\u751f\u6210\u7684\u6570\u636e\u5305\u9002\u914dMinecraft Java 1.21.11\u3002</p>\n"
"<h4 style=\" margin-top:14px; margin-bottom:6px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:medium; font-weight:700;\">\u8d44\u6e90\u51c6\u5907\u5de5\u4f5c</span></h4>\n"
"<p style=\" margin-top:6px; margin-bottom:6px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u6240\u6709\u751f\u6210\u6570\u636e\u5305\u9700\u8981\u7684\u8d44\u6e90\u6587\u4ef6\u90fd\u9700\u8981\u653e\u5165\u8be5\u7a0b\u5e8f\u6839\u76ee\u5f55\u4e0b\u7684resources\u6587\u4ef6\u5939\u4e2d\uff0c\u8fd9\u6837\u7a0b\u5e8f\u624d\u53ef\u4ee5\u626b\u63cf\u5230\u3002\u5982\u679c\u5411resources\u6587\u4ef6\u5939\u4e2d\u6dfb\u52a0\u4e86\u65b0\u7684\u8d44\u6e90\u6587\u4ef6"
                        "\uff0c\u8bf7\u70b9\u51fb\u9009\u62e9\u6587\u4ef6\u4e0b\u62c9\u6846\u65c1\u8fb9\u7684\u5237\u65b0\u6309\u94ae\uff0c\u7a0b\u5e8f\u5c06\u91cd\u65b0\u626b\u63cfresources\u6587\u4ef6\u5939\u4e2d\u7684\u6587\u4ef6\u5e76\u5c55\u793a\u5728\u4e0b\u62c9\u6846\u4e2d\u3002</p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" margin-top:4px; margin-bottom:4px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">.mid\u6587\u4ef6\uff1a</span>\u4f60\u9700\u8981\u51c6\u5907\u597d\u4e00\u9996\u7eaf\u94a2\u7434\u66f2\uff08\u4e0d\u542b\u5176\u4ed6\u4e50\u5668\u58f0\u90e8\uff09\u7684MIDI\u6587\u4ef6\u3002\u63a8\u8350\u4f7f\u7528\u5236\u8c31\u6216\u7f16\u66f2\u8f6f\u4ef6\uff08\u4f8b\u5982Musescore\uff09\u5c06\u94a2\u7434\u8c31\u5bfc\u51fa\u4e3aMIDI\u6587\u4ef6\u3002</li>\n"
"<li style=\" margin-top:4px; margin-bottom:4px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><s"
                        "pan style=\" font-weight:700;\">.schem\u6587\u4ef6\uff1a</span>\u63a8\u8350\u901a\u8fc7WorldEdit\u6a21\u7ec4\u5728\u6e38\u620f\u5185\u751f\u6210\uff0c\u9009\u533a\u5185\u5e94\u5305\u542b\u65b9\u5757\u629b\u5c04\u7ed8\u753b\u6210\u54c1\u6240\u9700\u5168\u90e8\u65b9\u5757\u3002\u4e5f\u53ef\u4ee5\u4f7f\u7528.txt\u6587\u4ef6\u66ff\u4ee3.schem\u6587\u4ef6\uff0c\u6587\u4ef6\u5185\u6bcf\u4e00\u884c\u683c\u5f0f\u5fc5\u987b\u4e3a&lt;\u65b9\u5757ID&gt; &lt;x\u5750\u6807&gt; &lt;y\u5750\u6807&gt; &lt;z\u5750\u6807&gt;\u3002</li></ul>\n"
"<h4 style=\" margin-top:14px; margin-bottom:6px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:medium; font-weight:700;\">\u914d\u7f6e\u5de5\u4f5c</span></h4>\n"
"<p style=\" margin-top:6px; margin-bottom:6px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u9996\u5148\u5e94\u5728\u201c\u901a\u7528\u914d\u7f6e\u201d\u9009\u9879\u5361\u9009\u5b9a\u9884\u8bbe\u914d\u7f6e\uff0c\u7a0b\u5e8f\u4f1a\u81ea\u52a8\u586b"
                        "\u5145\u9884\u8bbe\u53c2\u6570\uff0c\u4e4b\u540e\u4f60\u53ef\u5728\u5404\u4e2a\u9009\u9879\u5361\u5fae\u8c03\u9700\u8981\u4fee\u6539\u7684\u914d\u7f6e\u9879\u3002\u82e5\u4f60\u4e0d\u6e05\u695a\u67d0\u9879\u914d\u7f6e\u7684\u6548\u679c\uff0c\u8bf7\u4fdd\u6301\u9ed8\u8ba4\u914d\u7f6e\uff0c\u907f\u514d\u5728\u6e38\u620f\u5185\u64ad\u653e\u65f6\u4ea7\u751f\u4e25\u91cd\u6027\u80fd\u95ee\u9898\u6216\u6307\u4ee4\u9519\u8bef\u3002</p>\n"
"<p style=\" margin-top:8px; margin-bottom:8px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">\u786e\u5b9a\u5408\u9002\u7684Tick\u9891\u7387</span></p>\n"
"<p style=\" margin-top:6px; margin-bottom:6px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Minecraft\u9ed8\u8ba4\u6e38\u620ftick\u9891\u7387\u4e3a20\u6b21\u6bcf\u79d2\uff0c\u8fd9\u662f\u6240\u6709\u6e38\u620f\u673a\u5236\u7684\u5237\u65b0\u9891\u7387\uff0c\u610f\u5473\u7740\u9ed8\u8ba4\u60c5\u51b5\u4e0b\u6bcf\u79d2\u4ec5\u670920\u4e2a\u65f6\u523b"
                        "\u53ef\u4ee5\u6267\u884c\u64ad\u653e\u97f3\u6548\u7b49\u6307\u4ee4\u3002\u8be5\u9650\u5236\u53ef\u80fd\u9020\u6210\u4e50\u66f2\u8282\u62cd\u9519\u4f4d\uff0c\u542c\u611f\u53d8\u5dee\u3002\u4f60\u53ef\u4ee5\u5c1d\u8bd5\u8c03\u6574tick\u9891\u7387\u6765\u964d\u4f4e\u8282\u62cd\u9519\u4f4d\u8bef\u5dee\uff0c\u5bfc\u51fa\u6570\u636e\u5305\u65f6\u63a7\u5236\u53f0\u4f1a\u8f93\u51fa\u8bef\u5dee\u5927\u5c0f\u4f9b\u4f60\u53c2\u8003\u3002</p>\n"
"<p style=\" margin-top:6px; margin-bottom:6px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u53e6\u5916\uff0ctick\u9891\u7387\u8d85\u8fc720\u65f6\uff0c\u629b\u5c04\u65b9\u5757\u7684\u4e0b\u843d\u52a8\u753b\u4f1a\u9519\u4f4d\u3002\u56e0\u6b64\u89c6\u9891\u5236\u4f5c\u8005\u63a8\u8350\u65b9\u6848\uff1a\u5bfc\u51fatick\u9891\u738720\u7684\u6570\u636e\u5305\u7528\u4e8e\u5f55\u5236\u753b\u9762\uff0c\u518d\u5bfc\u51fa\u8bef\u5dee\u66f4\u5c0f\u7684\u9ad8tick\u9891\u7387\u6570\u636e\u5305\u7528\u4e8e\u5f55\u5236\u97f3\u9891\u3002</p>\n"
"<p style=\" margin-t"
                        "op:8px; margin-bottom:8px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">\u786e\u5b9a\u5408\u9002\u7684\u65b9\u5757\u629b\u5c04\u6ce2\u6570</span></p>\n"
"<p style=\" margin-top:6px; margin-bottom:6px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u8bfb\u53d6\u7684\u65b9\u5757\u4f1a\u6309\u6307\u5b9a\u6ce2\u6570\u5206\u6279\u629b\u5c04\uff0c\u6bcf\u5f53\u89e6\u53d1\u97f3\u7b26\u6309\u4e0b\u4e8b\u4ef6\u65f6\u629b\u51fa\u4e00\u6ce2\u65b9\u5757\u3002\u82e5\u629b\u5c04\u6ce2\u6570\u5927\u4e8e\u97f3\u7b26\u6309\u4e0b\u4e8b\u4ef6\u603b\u6570\uff08\u591a\u97f3\u7b26\u540c\u65f6\u6309\u4e0b\u7b97\u4f5c\u5355\u4e2a\u4e8b\u4ef6\uff09\uff0c\u5efa\u7b51\u6216\u7ed8\u753b\u4e2d\u7684\u90e8\u5206\u65b9\u5757\u5c06\u65e0\u6cd5\u751f\u6210\u3002\u82e5\u629b\u5c04\u6ce2\u6570\u8fc7\u5c0f\uff0c\u65b9\u5757\u7ed8\u753b\u52a8\u753b\u4f1a\u63d0\u524d\u7ed3\u675f\uff0c\u540c\u65f6\u4e00\u6b21\u6027\u751f\u6210\u5927\u91cf\u65b9\u5757\u5b9e\u4f53"
                        "\u8fd8\u4f1a\u5f15\u53d1\u6027\u80fd\u95ee\u9898\u3002\u5bfc\u51fa\u6570\u636e\u5305\u65f6\u8bf7\u67e5\u770b\u63a7\u5236\u53f0\u8f93\u51fa\u4fe1\u606f\uff0c\u5224\u65ad\u629b\u5c04\u6ce2\u6570\u662f\u5426\u5408\u7406\u3002</p>\n"
"<h4 style=\" margin-top:14px; margin-bottom:6px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:medium; font-weight:700;\">\u6570\u636e\u5305\u4e0e\u8d44\u6e90\u5305\u52a0\u8f7d</span></h4>\n"
"<p style=\" margin-top:6px; margin-bottom:6px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u6a21\u5757\u8f93\u51fa\u7684\u6bcf\u4e00\u4e2a\u6570\u636e\u5305\u5bf9\u5e94\u4e00\u9996\u4e50\u66f2\u3002\u4f7f\u7528\u65f6\uff0c\u9700\u5c06\u751f\u6210\u7684\u4e50\u66f2\u6570\u636e\u5305\u4e0e\u901a\u7528\u94a2\u7434\u6570\u636e\u5305\u4e00\u540c\u653e\u5165\u5b58\u6863\u7684<span style=\" font-family:'Courier New';\">datapacks\u6587\u4ef6\u5939\u5185</span>\uff0c\u5e76\u52a0\u8f7d\u5bf9\u5e94\u7684\u94a2\u7434\u97f3\u6e90"
                        "\u8d44\u6e90\u5305\u3002</p>\n"
"<h4 style=\" margin-top:14px; margin-bottom:6px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:medium; font-weight:700;\">\u52a8\u753b\u64ad\u653e\u64cd\u4f5c</span></h4>\n"
"<ol style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" margin-top:8px; margin-bottom:8px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u64ad\u653e\u4e50\u66f2\u524d\uff0c\u9700\u8981\u6267\u884c\u6307\u4ee4\u521b\u5efa\u9884\u8bbe\u94a2\u7434\u952e\u76d8\uff0c\u76ee\u524d\u63d0\u4f9b 4 \u5957\u952e\u76d8\u65b9\u6848\uff1a\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 2;\">\n"
"<li style=\" margin-top:4px; margin-bottom:4px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u5927\u578b\u65b9\u5757\u952e\u76d8\uff1a<span style=\" font-family:'Courier New';\">/function core"
                        ":keyboard/create</span></li>\n"
"<li style=\" margin-top:4px; margin-bottom:4px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u5c0f\u578b\u952e\u76d8\uff1a<span style=\" font-family:'Courier New';\">/function core:keyboard_v2/create</span></li>\n"
"<li style=\" margin-top:4px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u6da1\u65cb\u952e\u76d8\uff1a<span style=\" font-family:'Courier New';\">/function core:keyboard_v2/create_vortex</span></li></ul></li>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 2;\">\n"
"<li style=\" margin-top:4px; margin-bottom:4px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u5927\u578b\u952e\u76d8\uff1a<span style=\" font-family:'Courier New';\">/function core:keyboard_v2/create_large</span></li></ul>\n"
"<li style=\" margin-top:8px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-inden"
                        "t:0px;\">\u90e8\u7f72\u5b8c\u6210\u540e\uff0c\u6267\u884c\u64ad\u653e\u6307\u4ee4\u542f\u52a8\u52a8\u753b\uff1a<span style=\" font-family:'Courier New';\">/function &lt;\u81ea\u5b9a\u4e49\u6570\u636e\u5305\u540d\u79f0&gt;:start</span>\u3002\u5982\u679c\u9884\u8bbe\u7684\u64ad\u653etick\u9891\u7387\u4e0d\u662f20\uff0c\u4f60\u8fd8\u9700\u8981\u4f7f\u7528 <span style=\" font-family:'Courier New';\">/tick rate &lt;\u64ad\u653etick\u9891\u7387&gt;</span> \u6765\u4fee\u6539\u3002</li>\n"
"<li style=\" margin-top:8px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u7ec8\u6b62\u64ad\u653e\uff1a<span style=\" font-family:'Courier New';\">/function &lt;\u81ea\u5b9a\u4e49\u6570\u636e\u5305\u540d\u79f0&gt;:reset</span></li></ol></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"right\">\u9884\u8bbe\u914d\u7f6e\uff1a</p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"right\">\u6700\u5927\u97f3\u6548\u97f3\u91cf\uff1a</p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"right\">\u6700\u5c0f\u97f3\u6548\u97f3\u91cf\uff1a</p></body></html>", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>Midi\u6587\u4ef6\uff1a</p></body></html>", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u5237\u65b0", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>\uff08.mid\u6587\u4ef6\u9700\u653e\u5728\u7a0b\u5e8f\u76ee\u5f55\u7684resources\u6587\u4ef6\u5939\u4e2d\uff09</p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"right\">\u989d\u5916\u5ef6\u97f3(ms)\uff1a</p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"right\">\u64ad\u653etick\u9891\u7387\uff1a</p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"right\">\u64ad\u653e\u8d77\u59cb\u65f6\u523b(ms)\uff1a</p></body></html>", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab), QCoreApplication.translate("Form", u"\u901a\u7528\u8bbe\u7f6e", None))
        self.checkBox.setText(QCoreApplication.translate("Form", u"\u542f\u7528\u7434\u952e\u663e\u793a\u5668", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"right\">\u6700\u5927\u8df3\u8dc3\u65f6\u957f\uff1a</p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"right\">\u6700\u5927\u8df3\u8dc3\u9ad8\u5ea6\uff1a</p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>\u6307\u793a\u5668\u65b9\u5757ID\uff1a</p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"right\">\u5de6\u624b\u663e\u793a\u5668\u6570\u91cf\uff1a</p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"right\">\u53f3\u624b\u663e\u793a\u5668\u6570\u91cf\uff1a</p></body></html>", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_2), QCoreApplication.translate("Form", u"\u7434\u952e\u6307\u793a\u5668\u8bbe\u7f6e", None))
        self.checkBox_2.setText(QCoreApplication.translate("Form", u"\u542f\u7528\u65b9\u5757\u629b\u5c04\u7ed8\u753b", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"right\">Schem\u6587\u4ef6\uff1a</p></body></html>", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"\u5237\u65b0", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>\uff08.schem\u6587\u4ef6\u9700\u653e\u5165\u7a0b\u5e8f\u76ee\u5f55\u7684resources\u6587\u4ef6\u5939\u4e2d\uff09</p></body></html>", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"right\">\u57fa\u7840Y\u8f74\u629b\u5c04\u521d\u901f\uff1a</p></body></html>", None))
        self.label_18.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"right\">\u6700\u5927\u589e\u76caY\u8f74\u629b\u5c04\u901f\u5ea6\uff1a</p></body></html>", None))
        self.label_23.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"right\">\u76f8\u5bf9\u8d77\u59cb\u5750\u6807x\uff1a</p></body></html>", None))
        self.label_24.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"right\">\u76f8\u5bf9\u8d77\u59cb\u5750\u6807y\uff1a</p></body></html>", None))
        self.label_25.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"right\">\u76f8\u5bf9\u8d77\u59cb\u5750\u6807z\uff1a</p></body></html>", None))
        self.label_19.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"right\">\u65b9\u5757\u629b\u5c04\u6ce2\u6570\uff1a</p></body></html>", None))
        self.label_20.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>\uff08\u6240\u6709\u65b9\u5757\u5c06\u5206\u6210\u76ee\u6807\u6ce2\u6570\u629b\u5c04\u51fa\u53bb\uff0c\u6ce2\u6570\u8bbe\u7f6e\u8fc7\u5c0f\u4f1a\u4e00\u6b21\u629b\u5c04\u8fc7\u591a\u65b9\u5757\uff0c\u6ce2\u6570\u8d85\u8fc7\u97f3\u7b26\u603b\u6570\u65f6\u7ed8\u753b\u4f1a\u4e0d\u5b8c\u6574\uff09</p></body></html>", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), QCoreApplication.translate("Form", u"\u65b9\u5757\u629b\u5c04\u7ed8\u753b\u8bbe\u7f6e", None))
        self.label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">\u529f\u80fd\u5f00\u53d1\u4e2d...</span></p></body></html>", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), QCoreApplication.translate("Form", u"\u7011\u5e03\u6d41\u8bbe\u7f6e", None))
        self.label_22.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-weight:700;\">\u8fdb\u5ea6\uff1a</span></p></body></html>", None))
        self.label_21.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"right\">\u81ea\u5b9a\u4e49\u6570\u636e\u5305\u540d\u79f0\uff1a</p></body></html>", None))
        self.plainTextEdit.setPlainText("")
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u5bfc\u51fa", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), QCoreApplication.translate("Form", u"\u5bfc\u51fa", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_piano), QCoreApplication.translate("Form", u"Minecraft\u94a2\u7434", None))
        self.label_26.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:700;\">Minecraft \u539f\u751f\u52a8\u753b\u751f\u6210\u5668</span></p><p><span style=\" font-size:14pt;\">Minecraft Vanilla Animation Generator</span></p><p><span style=\" font-size:12pt;\">\u7a0b\u5e8f\u7248\u672c\uff1av1.0.1</span></p><p><span style=\" font-size:12pt;\">\u7a0b\u5e8f\u521b\u5efa\u8005\uff1a</span><span style=\" font-size:12pt; font-weight:700;\">klue007</span></p><p><span style=\" font-size:12pt;\">\u8be5\u7a0b\u5e8f\u7528\u4e8e\u751f\u6210Minecraft\u539f\u7248\u6570\u636e\u5305\uff0c\u4ee5\u5728\u6e38\u620f\u5185</span></p><p><span style=\" font-size:12pt;\">\u5b9e\u73b0\u4f8b\u5982\u94a2\u7434\u6f14\u594f\u7b49\u57fa\u4e8e\u539f\u7248\u6307\u4ee4\u7684\u52a8\u753b\u6548\u679c\u3002</span></p><p><br/></p></body></html>", None))
        self.textBrowser_2.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:700;\">\u66f4\u65b0\u65e5\u5fd7</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span"
                        " style=\" font-size:11pt; font-weight:700;\">v1.0.1</span><span style=\" font-size:11pt;\"> (2026.9.10)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- \u73b0\u5728\u5728\u672a\u542f\u7528\u94a2\u7434\u52a8\u753b\u751f\u6210\u6a21\u5757\u7684\u65b9\u5757\u629b\u5c04\u7ed8\u753b\u529f\u80fd\u65f6\uff0c\u5141\u8bb8\u4e0d\u9009\u62e9.schem\u6587\u4ef6</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- \u73b0\u5728\u5728\u8f93\u5165\u4e86\u542b\u6709\u7a7a\u683c\u6216\u4e2d\u6587\u7684\u6570\u636e\u5305\u540d\u79f0\u540e\u5bfc\u51fa\u4f1a\u63d0\u793a\u9519\u8bef\u5e76\u7ec8\u6b62\u5bfc\u51fa</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- \u73b0\u5728\u5982\u679c\u5bfc\u51fa\u6570\u636e\u5305\u7684\u4f4d\u7f6e\u5df2\u7ecf\u6709\u4e86\u540c\u540d\u79f0\u7684\u6570\u636e"
                        "\u5305\uff0c\u4f1a\u5c06\u5df2\u6709\u7684\u6570\u636e\u5305\u6539\u540d\u4ee5\u9632\u6b62\u6587\u4ef6\u8bfb\u5199\u9519\u8bef</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:700;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:700;\">v1.0.0</span><span style=\" font-size:11pt;\"> (2026.9.10)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- \u6dfb\u52a0\u94a2\u7434\u52a8\u753b\u751f\u6210\u6a21\u5757</p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QCoreApplication.translate("Form", u"\u7248\u672c", None))
    # retranslateUi

