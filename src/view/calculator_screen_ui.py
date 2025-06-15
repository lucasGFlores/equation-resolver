# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'teste.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.widget_4 = QWidget(self.centralwidget)
        self.widget_4.setObjectName("widget_4")
        sizePolicy1 = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum
        )
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy1)
        self.verticalLayout = QVBoxLayout(self.widget_4)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(-1, -1, -1, 6)
        self.widget_6 = QWidget(self.widget_4)
        self.widget_6.setObjectName("widget_6")
        sizePolicy2 = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum
        )
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy2)
        self.verticalLayout_5 = QVBoxLayout(self.widget_6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.widget_5 = QWidget(self.widget_6)
        self.widget_5.setObjectName("widget_5")
        sizePolicy2.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy2)
        self.verticalLayout_4 = QVBoxLayout(self.widget_5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.equation_field = QWidget(self.widget_5)
        self.equation_field.setObjectName("equation_field")
        sizePolicy3 = QSizePolicy(
            QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum
        )
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(
            self.equation_field.sizePolicy().hasHeightForWidth()
        )
        self.equation_field.setSizePolicy(sizePolicy3)
        self.equation_field.setMaximumSize(QSize(16777215, 8000))
        self.verticalLayout_2 = QVBoxLayout(self.equation_field)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.verticalLayout_4.addWidget(self.equation_field)

        self.widget_2 = QWidget(self.widget_5)
        self.widget_2.setObjectName("widget_2")
        sizePolicy2.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy2)
        self.verticalLayout_3 = QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget = QWidget(self.widget_2)
        self.widget.setObjectName("widget")
        sizePolicy3.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy3)

        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(8)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        button_style = "border-radius: 5px; background-color: rgb(102, 102, 102); color: white; padding: 0 30px;"
        font = QFont()
        font.setPointSize(17)

        self.button_calculate = QPushButton(self.widget)
        self.button_calculate.setObjectName("button_calculate")
        self.button_calculate.setMinimumSize(QSize(100, 50))
        self.button_calculate.setMaximumSize(QSize(400, 16777215))
        self.button_calculate.setStyleSheet(button_style)
        self.button_calculate.setFont(font)

        self.horizontalLayout.addWidget(self.button_calculate)

        self.button_minus = QPushButton(self.widget)
        self.button_minus.setObjectName("button_minus")
        self.button_minus.setSizePolicy(QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum))
        self.button_minus.setStyleSheet(button_style)
        self.button_minus.setFont(font)

        self.horizontalLayout.addWidget(self.button_minus)

        self.button_plus = QPushButton(self.widget)
        self.button_plus.setObjectName("button_plus")
        self.button_plus.setSizePolicy(QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum))
        self.button_plus.setStyleSheet(button_style)
        self.button_plus.setFont(font)

        self.horizontalLayout.addWidget(self.button_plus)

        self.verticalLayout_3.addWidget(self.widget)

        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName("widget_3")
        sizePolicy2.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy2)
        self.horizontalLayout_2 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.verticalLayout_3.addWidget(self.widget_3)

        self.verticalLayout_4.addWidget(self.widget_2)

        self.verticalLayout_5.addWidget(self.widget_5)

        self.label_resposta = QLabel(self.widget_6)
        self.label_resposta.setObjectName("label_resposta")
        font2 = QFont()
        font2.setPointSize(16)
        self.label_resposta.setFont(font2)
        # self.label_resposta.setAlignment(Qt.AlignmentFlag.AlignCenter)

        horizontalLayout = QHBoxLayout()
        horizontalLayout.addStretch()
        horizontalLayout.addWidget(self.label_resposta)
        horizontalLayout.addStretch()

        self.verticalLayout_5.addLayout(horizontalLayout)

        self.verticalLayout.addWidget(self.widget_6)

        self.horizontalLayout_3.addWidget(self.widget_4)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "MainWindow", None)
        )
        self.button_minus.setText(QCoreApplication.translate("MainWindow", "-", None))
        self.button_calculate.setText(
            QCoreApplication.translate("MainWindow", "Calcular", None)
        )
        self.button_plus.setText(QCoreApplication.translate("MainWindow", "+", None))
        self.label_resposta.setText("")

    # retranslateUi
