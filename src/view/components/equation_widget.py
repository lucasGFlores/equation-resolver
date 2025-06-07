from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QHBoxLayout

from src.resolver.model import EquationSystem
from src.view.components.matrix import MatrixCoefficients, MatrixResults


class EquationWidget(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent=parent)
        self._horizont_layout = QHBoxLayout()
        self.setLayout(self._horizont_layout)
        self.layout().setSpacing(0)
        self.layout().setContentsMargins(0, 0, 0, 0)
        self._matrix_coefficients = MatrixCoefficients(size=2)
        self._matrix_results = MatrixResults(rows=2)
        self.layout().setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout().addWidget(self._matrix_coefficients.widget)
        self.layout().addWidget(self._matrix_results.widget)

    def add_matrix_size(self):
        self._matrix_coefficients.increase_size()
        self._matrix_results.increase_size()

    def reduce_matrix_size(self):
        self._matrix_coefficients.reduce_size()
        self._matrix_results.reduce_size()

    def get_equations(self) -> [EquationSystem]:
        return EquationSystem.from_matrices(self._matrix_coefficients.value(), self._matrix_results.value())

