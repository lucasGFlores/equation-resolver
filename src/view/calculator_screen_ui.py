# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calculator.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
                               QPushButton, QScrollArea, QSizePolicy, QStatusBar,
                               QVBoxLayout, QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(12)


        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 174, 34))
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy2)
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setSpacing(30)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 80))
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_2)




        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(3)
        sizePolicy3.setVerticalStretch(3)
        sizePolicy3.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy3)
        self.widget.setStyleSheet(u"background-color: rgb(255, 85, 0);")
        self.verticalLayout_4 = QVBoxLayout(self.widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.widget_6 = QWidget(self.widget)
        self.widget_6.setObjectName(u"widget_6")
        sizePolicy2.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy2)
        self.verticalLayout_5 = QVBoxLayout(self.widget_6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.equation_field = QWidget(self.widget_6)
        self.equation_field.setObjectName(u"equation_field")
        sizePolicy2.setHeightForWidth(self.equation_field.sizePolicy().hasHeightForWidth())
        self.equation_field.setSizePolicy(sizePolicy2)
        self.equation_field.setMinimumSize(QSize(0, 30))
        self.equation_field.setStyleSheet(u"background-color: rgb(255, 255, 127);")
        self.horizontalLayout_3 = QHBoxLayout(self.equation_field)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")

        self.verticalLayout_5.addWidget(self.equation_field)

        self.widget_3 = QWidget(self.widget_6)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(0, 30))
        self.horizontalLayout_2 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.button_minus = QPushButton(self.widget_3)
        self.button_minus.setObjectName(u"button_minus")

        self.horizontalLayout_2.addWidget(self.button_minus)

        self.button_plus = QPushButton(self.widget_3)
        self.button_plus.setObjectName(u"button_plus")

        self.horizontalLayout_2.addWidget(self.button_plus)

        self.verticalLayout_5.addWidget(self.widget_3)

        self.button_calculate = QPushButton(self.widget_6)
        self.button_calculate.setObjectName(u"button_calculate")

        self.verticalLayout_5.addWidget(self.button_calculate)

        self.label_resposta = QLabel(self.widget_6)
        self.label_resposta.setObjectName(u"label_resposta")
        self.label_resposta.setStyleSheet("""
    font-size: 18px;
    
""")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_resposta.sizePolicy().hasHeightForWidth())
        self.label_resposta.setSizePolicy(sizePolicy4)
        self.label_resposta.setMinimumSize(QSize(0, 80))
        self.label_resposta.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_resposta)

        self.verticalLayout_4.addWidget(self.widget_6)

        self.horizontalLayout.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"TESTE", None))
        self.button_minus.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.button_plus.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.button_calculate.setText(QCoreApplication.translate("MainWindow", u"CALCULAR", None))
    # retranslateUi
