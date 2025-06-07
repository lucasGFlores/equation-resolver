from PySide6.QtWidgets import QApplication

from src.view.calculator_screen import CalculatorScreen
from src.view.components.matrix import MatrixResults, MatrixCoefficients


def main():
    app = QApplication()
    calculator = CalculatorScreen(MatrixCoefficients(size=2), MatrixResults(rows=2))
    calculator.showFullScreen()
    app.exec()
if __name__ == "__main__":
    main()