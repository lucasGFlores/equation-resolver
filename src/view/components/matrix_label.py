from PySide6.QtWidgets import QLineEdit, QSizePolicy
from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtCore import Qt, QRegularExpression


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
        self.setStyleSheet("color: rgb(0, 0, 0);\nbackground-color: rgb(85, 255, 127);")
        self.setMaximumWidth(50)
        self.setMinimumHeight(25)
        self.setSizePolicy(QSizePolicy.Policy.Preferred,QSizePolicy.Policy.Maximum)
        self.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        regex = QRegularExpression(r"\d+([.]\d*)")
        validator = QRegularExpressionValidator(regex, self)
        self.setValidator(validator)