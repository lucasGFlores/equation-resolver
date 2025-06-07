from PySide6.QtWidgets import QMainWindow, QApplication, QLabel, QLineEdit
from .calculator_screen_ui import Ui_MainWindow
from ..resolver.resolver import Resolver
from .components.equation_widget import EquationWidget
from .components.matrix.matrix_base import BaseMatrix


class CalculatorScreen(QMainWindow, Ui_MainWindow):

    def __init__(self, matrix_coefficients: BaseMatrix, matrix_result: BaseMatrix):
        super(CalculatorScreen, self).__init__()
        self.setupUi(self)
        self.equation_widget = EquationWidget()
        self.equation_field.layout().addWidget(self.equation_widget)
        self.button_plus.clicked.connect(self.equation_widget.add_matrix_size)
        self.button_minus.clicked.connect(self.equation_widget.reduce_matrix_size)
        self.button_calculate.clicked.connect(self.get_result)

    @staticmethod
    def _organize_results(results: dict) -> str:
        print(results)
        return "\n".join([f"{coefficient}: {result}" for coefficient,result in results.items()])
    def get_result(self) -> None:
        equation_list = self.equation_widget.get_equations()
        result = Resolver(equation_list).equation_solutions()
        if Resolver.depended_equations(result):
            self.label_resposta.setText("No solution exist")
        elif Resolver.is_infinity(result):
            self.label_resposta.setText("Have infinity solutions")
        else:
            self.label_resposta.setText(self._organize_results(result))

