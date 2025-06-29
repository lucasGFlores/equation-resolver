import math

import numpy as np

from src.resolver.model import Matrix, EquationSystem

class Resolver:
    """
    responsabilidades:
        - obter os sistemas de equações
        - formar a matriz de valores e a matriz de resultados
        - calcular o resultado das equações
    """

    def __init__(self, equations: list[EquationSystem]):
        self.equations = equations

    def equation_solutions(self) -> dict:
        all_coefficients = self._get_all_coefficients(self.equations)
        value_matrix = Matrix(self._value_matrix(self.equations))
        result_matrix = self._result_matrix(self.equations)
        determinant_value = value_matrix.determinant()
        return {
            coefficients: value_matrix.change_column(num, result_matrix).determinant()
            / determinant_value
            for num, coefficients in enumerate(all_coefficients)
        }

    @staticmethod
    def _value_matrix(systems: list[EquationSystem]) -> np.array:
        all_coefficient = Resolver._get_all_coefficients(systems)
        matrix = []
        for equations in systems:
            array = equations.to_row()
            rest_coefficients = set(all_coefficient).difference(
                equations.coefficients()
            )
            for coefficient in rest_coefficients:
                array.insert(all_coefficient.index(coefficient), 0)
            matrix.append(array)
        return matrix

    @staticmethod
    def _result_matrix(systems: list[EquationSystem]) -> np.array:
        return [equation.result for equation in systems]

    @staticmethod
    def _get_all_coefficients(equations: list[EquationSystem]) -> list:
        coefficients: set = set().union(
            *(equation.coefficients() for equation in equations)
        )
        return sorted(coefficients)

    @staticmethod
    def depended_equations(results: dict) -> bool:
        for coe, result in results.items():
            if math.isinf(result):
                return True
        return False

    @staticmethod
    def is_infinity(results: dict):
        """
        Quando o cálculo do determinante gera um 0/0, o sistema float retorna um Nan.
        Um Nan pode ser reconhecido pelo 'diferente', pois nan != nan retornará verdadeiro
        :param results:
        :return:
        """
        value = list(results.values())[0]
        return value != value or value is None
