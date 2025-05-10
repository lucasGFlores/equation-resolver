from abc import ABC

from .matrix_base import BaseMatrix
from ..matrix_label import MatrixLabel


class MatrixResults(BaseMatrix, ABC):
    def __init__(self,rows:int =1, parent=None):
        super().__init__(rows=rows,parent=parent)

    def reduce_size(self) -> None:
        self._rows -= 1
        widget = self._layout.itemAt(self._rows).widget()
        self._layout.removeWidget(widget)
        widget.setParent(None)

    def increase_size(self) -> None:
        self._layout.addWidget(MatrixLabel(), self._rows, 0)
        self._rows += 1
