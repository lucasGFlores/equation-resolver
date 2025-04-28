import unittest
from src.model.system_equations import EquationSystem

class TestEquationSystem(unittest.TestCase):
    def setUp(self):
        self.ideal_equation = "2x+2y+z=6"
        self.equation_with_out_number = "2x+y+z=6"
        self.equation_non_alphabetic = "y+0x+z=8"

    def test_equation_order(self):
        eq = EquationSystem.from_string(self.ideal_equation)
        self.assertEqual(eq.coefficients(),["x","y","z"], "the alphabetic is with problem")

        eq2 = EquationSystem.from_string(self.equation_non_alphabetic)
        self.assertEqual(eq2.coefficients(), ["x", "y", "z"], "the alphabetic is with problem")