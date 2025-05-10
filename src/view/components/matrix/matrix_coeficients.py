from abc import ABC

from .matrix_base import BaseMatrix
from ..matrix_label import MatrixLabel


class MatrixCoefficients(BaseMatrix, ABC):
    def __init__(self,parent=None):
        super().__init__(parent=parent)

    @property
    def _matrix_size(self):
        if self._rows != self._column:
            raise ValueError
        return self._rows

    @_matrix_size.setter
    def _matrix_size(self,new_size):
        if new_size <= 0:
            raise ValueError
        self._rows, self._column = new_size

    def increase_size(self) -> None:
        self._matrix_size += 1
        all_positions = self._create_matrix_position(self._rows,self._column)
        position_to_add = filter(lambda point: point[0] != self._rows and point[1] != self._column,
                                     all_positions)
        for position in position_to_add:
            label = MatrixLabel()
            self._layout.addWidget(label, position[0], position[1])

    def reduce_size(self) -> None:
        layer_to_remove = self._matrix_size - 1
        matrix_position = self._create_matrix_position(self._rows,self._column)
        positions_to_remove = filter(lambda point: point[0] == layer_to_remove or point[1] == layer_to_remove,
                                     matrix_position)
        for position in positions_to_remove:
            widget = self._layout.itemAtPosition(position[0], position[1]).widget()
            widget.setParent(None)
            self._layout.removeWidget(widget)



