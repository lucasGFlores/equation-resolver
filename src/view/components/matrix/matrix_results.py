from abc import ABC

from .label.matrix_label_coeficients import MatrixLabelCoefficients
from .matrix_base import BaseMatrix
from .label.matrix_label import (MatrixLabel)


class MatrixResults(BaseMatrix, ABC):
    def __init__(self,rows:int =1, parent=None):
        super().__init__(rows=rows,parent=parent)

    def reduce_size(self) -> None:
        self._rows -= 1
        widget = self._layout.itemAt(self._rows).widget()
        self._layout.removeWidget(widget)
        widget.setParent(None)

    def increase_size(self) -> None:
        self._layout.addWidget(MatrixLabelCoefficients(sign="=", coefficient="",sign_style_sheet="font-size: 20px;color:white;"), self._rows, 0,)
        self._rows += 1

    def _add_matrices_label(self, rows: int, columns: int):
        for row in range(0, rows):
            for column in range(0, columns):
                self._layout.addWidget(MatrixLabelCoefficients(sign="=", coefficient="",sign_style_sheet="font-size: 20px;color:white;"), row, column)