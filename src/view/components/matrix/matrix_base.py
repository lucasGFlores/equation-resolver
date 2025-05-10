from abc import ABC, abstractmethod
from PySide6.QtWidgets import QWidget, QGridLayout

from ..matrix_label import MatrixLabel


class BaseMatrix(ABC):
    _rows = 1
    _column = 1
    def __init__(self,rows:int =1,column:int =1,parent=None):
        self._rows = rows
        self._column = column
        self.widget = QWidget(parent=parent)
        self.widget.setLayout(QGridLayout())
        self._add_matrices_label(self._rows,self._column)



    @property
    def _layout(self) -> QGridLayout:
        return self.widget.layout()

    def value(self) -> list:
        try:
            matrix = self._create_matrix_position(self._rows,self._rows)
            for index in range(0,self._layout.count()):
               row, column,_,_ = self._layout.getItemPosition(index)
               widget: MatrixLabel = self._layout.itemAt(index).widget()
               matrix[row][column] = widget.value()
        except ValueError:
            print("Deu ruim no value aqui no matrix base")

    def _add_matrices_label(self, rows:int, columns:int):
        for row in range(0,rows):
            for column in range(0,columns):
                self._layout.addWidget(MatrixLabel(),row,column)

    @abstractmethod
    def reduce_size(self) -> None:
        pass

    @abstractmethod
    def increase_size(self) -> None:
        pass

    @staticmethod
    def _create_matrix_position(row: int, columns: int) -> list[tuple[int, int]]:
        return [(row, column) for row in range(0, row) for column in range(0, columns)]