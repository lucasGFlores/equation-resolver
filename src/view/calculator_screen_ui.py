# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'teste.ui'
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
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_3 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.widget_4 = QWidget(self.centralwidget)
        self.widget_4.setObjectName(u"widget_4")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy1)
        self.verticalLayout = QVBoxLayout(self.widget_4)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, -1, -1, 6)
        self.widget_6 = QWidget(self.widget_4)
        self.widget_6.setObjectName(u"widget_6")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy2)
        self.verticalLayout_5 = QVBoxLayout(self.widget_6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.widget_5 = QWidget(self.widget_6)
        self.widget_5.setObjectName(u"widget_5")
        sizePolicy2.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy2)
        self.verticalLayout_4 = QVBoxLayout(self.widget_5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.equation_field = QWidget(self.widget_5)
        self.equation_field.setObjectName(u"equation_field")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.equation_field.sizePolicy().hasHeightForWidth())
        self.equation_field.setSizePolicy(sizePolicy3)
        self.equation_field.setMaximumSize(QSize(16777215, 8000))
        self.equation_field.setStyleSheet(u"color: rgb(77, 69, 120);\n"
"background-color: rgb(33, 33, 98);\n"
"\n"
"\n"
"")
        self.verticalLayout_2 = QVBoxLayout(self.equation_field)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")

        self.verticalLayout_4.addWidget(self.equation_field)

        self.widget_2 = QWidget(self.widget_5)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy2.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy2)
        self.verticalLayout_3 = QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget = QWidget(self.widget_2)
        self.widget.setObjectName(u"widget")
        sizePolicy3.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy3)
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, -1, 0, -1)
        self.button_minus = QPushButton(self.widget)
        self.button_minus.setObjectName(u"button_minus")
        self.button_minus.setMinimumSize(QSize(0, 40))
        self.button_minus.setMaximumSize(QSize(250, 16777215))
        font = QFont()
        font.setPointSize(14)
        self.button_minus.setFont(font)

        self.horizontalLayout.addWidget(self.button_minus)

        self.button_calculate = QPushButton(self.widget)
        self.button_calculate.setObjectName(u"button_calculate")
        self.button_calculate.setMinimumSize(QSize(0, 40))
        self.button_calculate.setMaximumSize(QSize(400, 16777215))
        font1 = QFont()
        font1.setPointSize(11)
        self.button_calculate.setFont(font1)

        self.horizontalLayout.addWidget(self.button_calculate)

        self.button_plus = QPushButton(self.widget)
        self.button_plus.setObjectName(u"button_plus")
        sizePolicy3.setHeightForWidth(self.button_plus.sizePolicy().hasHeightForWidth())
        self.button_plus.setSizePolicy(sizePolicy3)
        self.button_plus.setMinimumSize(QSize(0, 40))
        self.button_plus.setMaximumSize(QSize(250, 16777215))
        self.button_plus.setFont(font)

        self.horizontalLayout.addWidget(self.button_plus)


        self.verticalLayout_3.addWidget(self.widget)

        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy2.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy2)
        self.horizontalLayout_2 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")

        self.verticalLayout_3.addWidget(self.widget_3)


        self.verticalLayout_4.addWidget(self.widget_2)


        self.verticalLayout_5.addWidget(self.widget_5)

        self.label_resposta = QLabel(self.widget_6)
        self.label_resposta.setObjectName(u"label_resposta")
        self.label_resposta.setMaximumSize(QSize(16777215, 85))
        font2 = QFont()
        font2.setPointSize(16)
        self.label_resposta.setFont(font2)
        self.label_resposta.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_resposta)


        self.verticalLayout.addWidget(self.widget_6)


        self.horizontalLayout_3.addWidget(self.widget_4)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.button_minus.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.button_calculate.setText(QCoreApplication.translate("MainWindow", u"Caculate", None))
        self.button_plus.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.label_resposta.setText("")
    # retranslateUi

