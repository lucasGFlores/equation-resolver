import string
from abc import ABC

from .label.matrix_label_coeficients import MatrixLabelCoefficients
from .label.matrix_value import MatrixValue
from .matrix_base import BaseMatrix
from .label.matrix_label import MatrixLabel


class MatrixCoefficients(BaseMatrix):
    list_of_coefficients = list(string.ascii_lowercase)
    def __init__(self,size=1,parent=None):
        super().__init__(rows=size,column=size,matrix_label_class=MatrixLabelCoefficients,parent=parent)

    @property
    def _matrix_size(self):
        if self._rows != self._column:
            raise ValueError
        return self._rows

    @_matrix_size.setter
    def _matrix_size(self,new_size):
        if new_size <= 0:
            raise ValueError
        self._rows = new_size
        self._column = new_size

    def increase_size(self) -> None:
        actual_positions = self._create_matrix_position(self._rows,self._column)
        self._matrix_size += 1
        all_positions = self._create_matrix_position(self._rows,self._column)

        position_to_add = list(filter(lambda point: point not in actual_positions,
                                     all_positions))
        for position in position_to_add:
            row, column = position
            coefficient = self.list_of_coefficients[column]
            self._layout.addWidget(MatrixLabelCoefficients(coefficient=coefficient,sign=""), row, column)

    def reduce_size(self) -> None:
        actual_positions = self._create_matrix_position(self._rows,self._column)
        self._matrix_size -= 1
        intern_positions = self._create_matrix_position(self._rows,self._column)
        positions_to_remove = filter(lambda point: point not in intern_positions,
                                     actual_positions)
        for position in positions_to_remove:
            widget = self._layout.itemAtPosition(position[0], position[1]).widget()
            widget.setParent(None)
            self._layout.removeWidget(widget)

    def _add_matrices_label(self, rows: int, columns: int, matrix_label_class: type[MatrixLabelCoefficients]):
        # inserir forma mais perfomática
        for row in range(0, rows):
            for column in range(0, columns):
                coefficient = self.list_of_coefficients[column]
                if column == 0:
                    self._layout.addWidget(matrix_label_class(coefficient=coefficient,sign=""), row, column)
                    continue
                self._layout.addWidget(matrix_label_class(coefficient=coefficient), row, column)



