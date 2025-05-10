from abc import ABC

from .matrix_base import BaseMatrix
from ..matrix_label import MatrixLabel


class MatrixResults(BaseMatrix, ABC):
    def __init__(self,parent=None):
        super().__init__(parent=parent)


    @property
    def _rows(self):
        return self._rows

    @_rows.setter
    def _rows(self, new_rows):
        if new_rows <= 0:
            raise ValueError
        self._rows = new_rows

    def reduce_size(self) -> None:
        self._rows -= 1
        widget = self._layout.itemAt(self._rows).widget()
        self._layout.removeWidget(widget)
        widget.setParent(None)

    def increase_size(self) -> None:
        self._layout.addWidget(MatrixLabel(),self._rows,0)
        self._rows += 1


