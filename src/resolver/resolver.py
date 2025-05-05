import numpy as np

from src.resolver.model import Matrix, EquationSystem
class Resolver:
    """
    responsibilities:
        - get the equations systems
        - form the value matrix and result matrix
        - calculate the result of the equations
    """
    def __init__(self, equations: list[EquationSystem]):
        self.equations = equations

    def equation_solutions(self) -> dict:
        all_coefficients = self._get_all_coefficients(self.equations)
        value_matrix = Matrix(self._value_matrix(self.equations))
        result_matrix = self._result_matrix(self.equations)
        determinant_value = value_matrix.determinant()
        return {
            coefficients :
                value_matrix.change_column(num,result_matrix).determinant()/determinant_value
          for num, coefficients in enumerate(all_coefficients)}

    @staticmethod
    def _value_matrix(systems: list[EquationSystem]) -> np.array:
        all_coefficient = Resolver._get_all_coefficients(systems)
        matrix = []
        for equations in systems:
            array = equations.to_row()
            rest_coefficients = set(all_coefficient).difference(equations.coefficients())
            for coefficient in rest_coefficients:
                array.insert(all_coefficient.index(coefficient),0)
            matrix.append(array)
        return matrix

    @staticmethod
    def _result_matrix(systems: list[EquationSystem]) -> np.array:
        return [equation.result for equation in systems]

    @staticmethod
    def _get_all_coefficients(equations: list[EquationSystem]) -> list:
        coefficients: set = set().union(*(equation.coefficients() for equation in equations))
        return sorted(coefficients)