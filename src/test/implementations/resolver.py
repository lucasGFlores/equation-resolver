import unittest

from src.model import EquationSystem
from src.resolver import Resolver


class TestResolver(unittest.TestCase):
    def setUp(self):
        self.ideal_equation = ["2x+2y+z=6", "3x+y+z=8", "3x+y+4z=32"]
        self.ideal_equation = [EquationSystem.from_string(equation) for equation in self.ideal_equation]

        self.non_alphabetic_equation = ["z+2x+2y=6", "y+z+3x=8", "y+4z+3x=32"]
        self.non_alphabetic_equation = [EquationSystem.from_string(equation) for equation in self.non_alphabetic_equation]

        self.non_square_equation = ["5x+1y+z=6", "y+2x+z=8", "y+3x+4z=52", "7x+2y+3z = 100"]
        self.non_square_equation = [EquationSystem.from_string(equation) for equation in self.non_square_equation]

        self.equation_with_missing_coefficient = ["2x+2y+z=6", "3x+z=15", "3x+y+4z=32"]
        self.equation_with_missing_coefficient = [EquationSystem.from_string(equation) for equation in self.equation_with_missing_coefficient]

    def test_value_matrix(self):
        matrix_ideal = Resolver.value_matrix(self.ideal_equation)
        self.assertEqual(matrix_ideal, [[2,2,1],[3,1,1],[3,1,4]])

        matrix_non_alphabetic_equation = Resolver.value_matrix(self.non_alphabetic_equation)
        self.assertEqual(matrix_non_alphabetic_equation,[[2,2,1],[3,1,1],[3,1,4]], "Problem to convert to matrix in alphabetic order")

        # systems equations with missing coefficient need to be replaced with 0's
        matrix_equation_with_missing_coefficient = Resolver.value_matrix(self.equation_with_missing_coefficient)
        self.assertEqual(matrix_equation_with_missing_coefficient,[[2,2,1],[3,0,1],[3,1,4]], "Problem to convert missing coefficient")

    def test_result_matrix(self):
        matrix_ideal = Resolver.value_matrix(self.ideal_equation)
        self.assertEqual(matrix_ideal, [6,8,32])

        matrix_non_alphabetic_equation = Resolver.value_matrix(self.non_alphabetic_equation)
        self.assertEqual(matrix_non_alphabetic_equation, [6,8,32],
                         "Problem to convert to matrix in alphabetic order")

        matrix_equation_with_missing_coefficient = Resolver.value_matrix(self.equation_with_missing_coefficient)
        self.assertEqual(matrix_equation_with_missing_coefficient, [6,15,32],
                         "Problem to convert to matrix in alphabetic order")
