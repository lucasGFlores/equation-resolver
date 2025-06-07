from abc import ABC

from PySide6.QtGui import QFont
from PySide6.QtWidgets import QWidget, QHBoxLayout, QSizePolicy, QLabel

from .matrix_label import MatrixLabel
from .matrix_value import MatrixValue


class MatrixLabelCoefficients(QWidget):
    def __init__(self,coefficient:str = "x",sign:str="+",sign_style_sheet: str ="color:black;", parent=None):
        super().__init__(parent=parent)
        self._horizont_layout: QHBoxLayout = QHBoxLayout()
        self.setLayout(self._horizont_layout)
        self.setSizePolicy(QSizePolicy.Preferred,QSizePolicy.Preferred)
        self._label: MatrixLabel = MatrixLabel()
        font = QFont()
        font.setPointSize(12)
        sign_label = QLabel()
        sign_label.setText(sign)
        sign_label.setStyleSheet(sign_style_sheet)
        sign_label.setFont(font)

        coefficient_label = QLabel()
        coefficient_label.setText(coefficient)
        coefficient_label.setStyleSheet(sign_style_sheet)
        coefficient_label.setFont(font)
        self.layout().addWidget(sign_label)
        self.layout().addWidget(self._label)
        self.layout().addWidget(coefficient_label)

    def value(self) -> float:
        return  self._label.value()

