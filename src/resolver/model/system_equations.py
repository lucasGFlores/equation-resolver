import dataclasses
import re
import string
from ast import Param
from typing import Dict


@dataclasses.dataclass
class Coefficient:
    def __init__(self, info: tuple[str, str, str]):
        """
        :param info: [('', '2', 'x'), ('+', '2', 'y')]
        primeiro = sinal
        segundo = valor
        terceiro = coeficiente
        """
        self.value = float(info[0] + f"{info[1] if info[1] != '' else 1}")
        self.coefficient = info[2]


class EquationSystem:
    def __init__(self, coefficient, result: float):
        self._coefficient = coefficient
        self.result = result

    def coefficients(self) -> set:
        return set(self._coefficient)

    def to_row(self) -> list[float]:
        return [
            self._coefficient.get(coefficient)
            for coefficient in sorted(self._coefficient)
        ]

    @staticmethod
    def from_matrices(matrix_value, matrix_result) -> list["EquationSystem"]:
        equations = []
        number_of_coefficients = len(matrix_result)
        coefficients = EquationSystem._possible_coefficients_list(
            number_of_coefficients
        )
        for value_row, result in zip(matrix_value, matrix_result):
            equation_value = [
                f"{value:+}{coefficient}"
                for coefficient, value in zip(coefficients, value_row)
            ]
            equation = f"{''.join(equation_value)}={result[0]}"
            equations.append(EquationSystem.from_string(equation))
        return equations

    @staticmethod
    def from_string(equation_system: str) -> "EquationSystem":
        """
        Converte uma equação em uma string
        :param equation_system: 2x+2y=6
        :return: Uma estrutura de Equation
        """
        # primeira parte, encontra os coeficientes e seus valores
        coefficients = EquationSystem._coefficients_from(equation_system)
        coefficients_dict = {
            coefficient.coefficient: coefficient.value for coefficient in coefficients
        }

        # obtém o resultado da equação
        result = float(equation_system.split("=")[1].strip())
        return EquationSystem(coefficients_dict, result)

    @staticmethod
    def _coefficients_from(equation_system: str) -> [Coefficient]:
        regex = r"([+-]?)(\d*\.?\d*)([a-z])"
        match = re.findall(regex, equation_system)
        return [Coefficient(coefficient) for coefficient in match]

    @staticmethod
    def _possible_coefficients_list(number_of_coefficients: int) -> list:
        all_coefficients = list(string.ascii_lowercase)
        return all_coefficients[: number_of_coefficients + 1]
