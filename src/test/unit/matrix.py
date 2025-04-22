import unittest

import numpy as np
from numpy.linalg import LinAlgError

from src.model.matrix import Matrix
from src.model.system_equations import EquationSystem


class TestMatrix(unittest.TestCase):
    def setUp(self):
        self.ideal_equation = ["2x+2y+z=6", "3x+y+z=8", "3x+y+4z=32"]
        self.non_alphabetic_equation = ["z+2x+2y=6", "y+z+3x=8", "y+4z+3x=32"]
        self.non_square_equation = ["5x+1y+z=6", "y+2x+z=8", "y+3x+4z=52", "7x+2y+3z = 100"]
        self.equation_with_missing_coefficient = ["2x+2y+z=6", "3x+z=15", "3x+y+4z=32"]

    def test_ideal_equation_coefficients(self):
        equations_list = [EquationSystem.from_string(equation) for equation in self.ideal_equation]
        self.assertEqual(Matrix._all_coefficients_from(equations_list), {"x": 0, "y": 1, "z": 2},
                         "The alphabetic order is wrong")

    def test_missing_coefficients(self):
        equations_list = [EquationSystem.from_string(equation) for equation in self.equation_with_missing_coefficient]
        self.assertEqual(Matrix._all_coefficients_from(equations_list), {"x": 0, "y": 1, "z": 2},
                         "The alphabetic order is wrong")

    def test_non_alphabetic_coefficients(self):
        equations_list = [EquationSystem.from_string(equation) for equation in self.non_alphabetic_equation]
        self.assertEqual(Matrix._all_coefficients_from(equations_list), {"x": 0, "y": 1, "z": 2},
                         "The alphabetic order is wrong")

    def test_construct_missing_coefficient_value_matrix(self):
        """
        Some matrix have equation who don't have all the coefficients of the others equations
        :return: assert if the position with no coefficient is filled with 0.
        """
        equations_list = [EquationSystem.from_string(equation) for equation in self.equation_with_missing_coefficient]
        value_matrix = Matrix._create_value_matrix(equations_list)
        self.assertTrue(np.equal(value_matrix, np.array([[2, 2, 1],[3, 0, 1],[3, 1, 4]])).all(), "The missing coefficient spaces arent filled with 0's")

    def test_result_of_ideal_equation(self):
        m = Matrix(self.ideal_equation)
        self.assertEqual(m.values_coefficients(), {"x": 0.5, "y": -1.5, "z": 8})


