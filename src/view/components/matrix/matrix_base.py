from abc import ABC, abstractmethod
from PySide6.QtWidgets import QWidget, QGridLayout, QSizePolicy

from src.view.components.matrix.label.matrix_label import MatrixLabel
from .label.matrix_value import MatrixValue


class BaseMatrix(ABC):
    _rows = 1
    _column = 1
    def __init__(self,rows:int =1,column:int =1,matrix_label_class: type[MatrixValue] = MatrixLabel,parent=None):
        self._rows = rows
        self._column = column
        self.widget = QWidget(parent=parent)
        self.widget.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        self.widget.setLayout(QGridLayout())
        self._add_matrices_label(self._rows,self._column,matrix_label_class)
        self.widget.setContentsMargins(0, 0, 0, 0)
        self.widget.layout().setSpacing(0)



    @property
    def _layout(self) -> QGridLayout:
        return self.widget.layout()

    def value(self) -> list:
        try:
            matrix = [[None for _ in range(0,self._column)] for _ in range(0,self._rows)]
            for index in range(0,self._layout.count()):
               row, column,_,_ = self._layout.getItemPosition(index)
               widget: MatrixLabel = self._layout.itemAt(index).widget()
               matrix[row][column] = widget.value()
            return matrix
        except ValueError:
            print("Deu ruim no value aqui no matrix base")

    def _add_matrices_label(self, rows:int, columns:int, matrix_label_class : MatrixValue):
        for row in range(0,rows):
            for column in range(0,columns):
                self._layout.addWidget(matrix_label_class(),row,column)

    @abstractmethod
    def reduce_size(self) -> None:
        pass

    @abstractmethod
    def increase_size(self) -> None:
        pass

    @staticmethod
    def _create_matrix_position(row: int, columns: int) -> list[tuple[int, int]]:
        return [(row, column) for row in range(0, row) for column in range(0, columns)]