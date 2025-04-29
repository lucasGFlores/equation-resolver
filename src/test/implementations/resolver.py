import unittest

from src.model import EquationSystem, Matrix
from src.resolver import Resolver


class TestResolver(unittest.TestCase):
    def setUp(self):
        self.ideal_equation = ["2x+2y+z=6", "3x+y+z=8", "3x+y+4z=32"]
        self.ideal_equation_list = [EquationSystem.from_string(equation) for equation in self.ideal_equation]

        self.non_alphabetic_equation = ["z+2x+2y=6", "y+z+3x=8", "y+4z+3x=32"]
        self.non_alphabetic_equation_list = [EquationSystem.from_string(equation) for equation in self.non_alphabetic_equation]

        self.non_square_equation = ["5x+1y+z=6", "y+2x+z=8", "y+3x+4z=52", "7x+2y+3z = 100"]
        self.non_square_equation_list = [EquationSystem.from_string(equation) for equation in self.non_square_equation]

        self.equation_with_missing_coefficient = ["2x+2y+z=6", "3x+z=15", "3x+y+4z=32"]
        self.equation_with_missing_coefficient_list = [EquationSystem.from_string(equation) for equation in self.equation_with_missing_coefficient]

    def test_get_all_coefficients(self):
        ideal_coefficients = Resolver._get_all_coefficients(self.ideal_equation_list)
        self.assertEqual(ideal_coefficients,["x","y","z"],"have problem in get all coefficients")

        non_alphabetic_coefficients = Resolver._get_all_coefficients(self.non_alphabetic_equation_list)
        self.assertEqual(non_alphabetic_coefficients,["x","y","z"],"The order of coefficients are wrong")

        missing_coefficients  = Resolver._get_all_coefficients(self.equation_with_missing_coefficient_list)
        self.assertEqual(missing_coefficients,["x","y","z"],"The logic to get all the coefficients in the system is with problems")


    def test_value_matrix(self):
        matrix_ideal = Resolver._value_matrix(self.ideal_equation_list)
        self.assertEqual(matrix_ideal, [[2.0,2.0,1.0],[3.0,1.0,1.0],[3.0,1.0,4.0]])

        matrix_non_alphabetic_equation = Resolver._value_matrix(self.non_alphabetic_equation_list)
        self.assertEqual(matrix_non_alphabetic_equation,[[2.0,2.0,1.0],[3.0,1.0,1.0],[3.0,1.0,4.0]], "Problem to convert to matrix in alphabetic order")

        # systems equations with missing coefficient need to be replaced with 0's
        matrix_equation_with_missing_coefficient = Resolver._value_matrix(self.equation_with_missing_coefficient_list)
        self.assertEqual(matrix_equation_with_missing_coefficient,[[2.0,2.0,1.0],[3.0,0,1.0],[3.0,1.0,4.0]], "Problem to convert missing coefficient")

    def test_result_matrix(self):
        matrix_ideal = Resolver._value_matrix(self.ideal_equation_list)
        self.assertEqual(matrix_ideal, [6,8,32])

        matrix_non_alphabetic_equation = Resolver.value_matrix(self.non_alphabetic_equation_list)
        self.assertEqual(matrix_non_alphabetic_equation, [6,8,32],
                         "Problem to convert to matrix in alphabetic order")

        matrix_equation_with_missing_coefficient = Resolver.value_matrix(self.equation_with_missing_coefficient_list)
        self.assertEqual(matrix_equation_with_missing_coefficient, [6,15,32],
                         "Problem to convert to matrix in alphabetic order")
