from PySide6.QtWidgets import QMainWindow, QApplication, QLabel, QLineEdit
from calculator_screen_ui import Ui_MainWindow
from src.resolver.model import EquationSystem
from src.resolver.resolver import Resolver
from src.view.components.equation_widget import EquationWidget
from src.view.components.matrix.matrix_base import BaseMatrix
from src.view.components.matrix import MatrixResults, MatrixCoefficients


class CalculatorScreen(QMainWindow, Ui_MainWindow):

    def __init__(self, matrix_coefficients: BaseMatrix, matrix_result: BaseMatrix):
        super(CalculatorScreen, self).__init__()
        self.setupUi(self)
        self.matrix_coefficients = matrix_coefficients
        self.matrix_result = matrix_result
        self.equation_widget = EquationWidget()
        self.equation_field.layout().addWidget(self.equation_widget)
        self.button_plus.clicked.connect(self.equation_widget.add_matrix_size)
        self.button_minus.clicked.connect(self.equation_widget.reduce_matrix_size)
        self.button_calculate.clicked.connect(self.get_result)


    def get_result(self) -> None:
        equation_list = EquationSystem.from_matrices(self.matrix_coefficients.value(),self.matrix_result.value())
        result = Resolver(equation_list).equation_solutions()
        print(result)
        self.label_resposta.setText(str(result))

    
if __name__ == "__main__":
    app = QApplication()
    screen = CalculatorScreen(MatrixCoefficients(size=2), MatrixResults(rows=2))
    screen.showFullScreen()
    app.exec()
