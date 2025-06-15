from abc import ABC, abstractmethod
from typing import Protocol

from PySide6.QtWidgets import QWidget

class MatrixValue(Protocol):
    def value(self) -> float:
        pass
