from PySide6.QtWidgets import QLineEdit, QSizePolicy
from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtCore import Qt, QRegularExpression

from .matrix_value import MatrixValue


class MatrixLabel(QLineEdit):
    def __init__(self,parent=None):
        super().__init__(parent=parent)
        self._config_style()

    def value(self):
        try:
            return float(self.text())
        except ValueError:
            return 0.0

    def _config_style(self):
        self.setStyleSheet("color: rgb(0, 0, 0);\nbackground-color: rgb(191, 222, 215);border-radius: 5px;")
        self.setMaximumWidth(60)
        self.setMinimumHeight(30)
        self.setSizePolicy(QSizePolicy.Policy.Preferred,QSizePolicy.Policy.Maximum)
        self.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.font().setPointSize(15)
        self.setFont(self.font())
        regex = QRegularExpression(r"-?(?:\d+\.?\d*|\.\d+)")
        validator = QRegularExpressionValidator(regex, self)
        self.setValidator(validator)