import dataclasses
import re
from ast import Param
from typing import Dict

@dataclasses.dataclass
class Coefficient:
    value: float = None
    coefficient = None
    def __init__(self, info: tuple[str,str,str]):
        """
        :param info: [('', '2', 'x'), ('+', '2', 'y')]
        first = signal
        second = value
        coefficient = y
        """
        self.value = float(info[0]+f"{info[1] if info[1] != '' else 1}")
        self.coefficient = info[2]


class EquationSystem:
    _coefficient: dict = None
    result: float = None

    def __init__(self, coefficient, result: float):
        self._coefficient = coefficient
        self.result = result



    def coefficients(self) -> set:
        return set(self._coefficient)

    def to_row(self) -> list[float]:
        return [self._coefficient.get(coefficient) for coefficient in sorted(self._coefficient)]

    @staticmethod
    def from_string(equation_system: str) ->  "EquationSystem":
        """
        This convert a equation in a string
        :param equation_system: 2x+2y=6
        :return: A structure of Equation
        """
        # first part,find the coefficient and their values
        coefficients = EquationSystem._coefficients_from(equation_system)
        coefficients_dict = {coefficient.coefficient: coefficient.value for coefficient in coefficients}

        # get result from the equation
        result = float(equation_system.split("=")[1].strip())
        return EquationSystem(coefficients_dict,result)

    @staticmethod
    def _coefficients_from(equation_system: str) -> [Coefficient]:
        regex = r"([+-]?)(\d*\.?\d*)([a-z])"
        match = re.findall(regex, equation_system)
        return [Coefficient(coefficient) for coefficient in match]



