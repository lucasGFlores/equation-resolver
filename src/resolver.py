import numpy as np

from .model import Matrix, EquationSystem
class Resolver:
    """
    responsibilities:
        - get the equations systems
        - form the value matrix and result matrix
        - calculate the result of the equations
    """
    value_matrix = None
    result_matrix = None
    def __init__(self, equations: list[EquationSystem]):
        pass

    def equation_solutions(self):
        pass

    @staticmethod
    def _value_matrix(systems: list[EquationSystem]) -> np.array:

    @staticmethod
    def _result_matrix(systems: list[EquationSystem]) -> np.array:
        pass

    @staticmethod
    def _get_all_coefficients(equations: list[EquationSystem]) -> list:
        coefficients: set = set().union(*(equation.coefficients() for equation in equations))
        return sorted(coefficients)