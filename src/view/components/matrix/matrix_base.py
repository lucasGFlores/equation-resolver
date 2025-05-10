from abc import ABC, abstractmethod
from PySide6.QtWidgets import QWidget, QGridLayout

from ..matrix_label import MatrixLabel


class BaseMatrix(ABC):
    _rows = 1
    _column = 1
    def __init__(self,parent=None):
        self._widget = QWidget(parent=parent)
        self._widget.setLayout(QGridLayout())


    @property
    def _layout(self) -> QGridLayout:
        return self._widget.layout()

    def value(self) -> list:
        try:
            matrix = self._create_matrix_position(self._rows,self._rows)
            for index in range(0,self._layout.count()):
               row, column,_,_ = self._layout.getItemPosition(index)
               widget: MatrixLabel = self._layout.itemAt(index).widget()
               matrix[row][column] = widget.value()
        except ValueError:
            print("Deu ruim no value aqui no matrix base")

    @abstractmethod
    def reduce_size(self) -> None:
        pass

    @abstractmethod
    def increase_size(self) -> None:
        pass

    @staticmethod
    def _create_matrix_position(row: int, column: int) -> list[tuple[int, int]]:
        return [(row, column) for row in range(0, row) for column in range(0, column)]