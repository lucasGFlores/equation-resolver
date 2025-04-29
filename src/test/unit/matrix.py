import unittest
from src.model.matrix import Matrix


class TestMatrix(unittest.TestCase):
    def setUp(self):
        self.ideal_equation = ["2x+2y+z=6", "3x+y+z=8", "3x+y+4z=32"]
        self.ideal_matrix = [[2, 2, 1], [3, 1, 1], [3, 1, 4]]
        self.equation_with_missing_coefficient = ["2x+2y+z=6", "3x+z=15", "3x+y+4z=32"]
        self.matrix_with_missing_coefficient = [[2, 2, 1], [3, 0, 1], [3, 1, 4]]

    def test_determinant(self):
        self.assertEqual(Matrix(self.ideal_matrix).determinant(), -12, "the determinant is miss calculated")
        self.assertEqual(Matrix(self.matrix_with_missing_coefficient).determinant(), -17,
                         "the determinant is miss calculated")

    def test_change_column(self):
        new_column = [0,0,0]
        ma = Matrix(self.ideal_matrix)
        ma2 = ma.change_column(1, new_column)
        self.assertTrue((ma2.matrix == [[2,0,1],[3,0,1],[3,0,4]]).all(), "Have a problem in change column system")
