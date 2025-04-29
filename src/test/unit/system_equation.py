import unittest
from src.model.system_equations import EquationSystem

class TestEquationSystem(unittest.TestCase):
    def setUp(self):
        self.ideal_equation = "2x+2y+1z=6"
        self.equation_with_out_number = "2x+y+z=6"
        self.equation_non_alphabetic = "y+0x+z=8"

    def test_equation_order(self):
        eq = EquationSystem.from_string(self.ideal_equation)
        self.assertEqual(eq.coefficients(),["x","y","z"], "the alphabetic is with problem")

        eq2 = EquationSystem.from_string(self.equation_non_alphabetic)
        self.assertEqual(eq2.coefficients(), ["x", "y", "z"], "the alphabetic is with problem")

    def test_row_value(self):
        eq = EquationSystem.from_string(self.ideal_equation)
        self.assertEqual(eq.to_row(),[2,2,1],"This result must return the values in alphabetic order")

        eq2 = EquationSystem.from_string(self.equation_with_out_number)
        self.assertEqual(eq2.to_row(),[2,1,1],"The value can translate coefficients without number")

        eq3 = EquationSystem.from_string(self.equation_non_alphabetic)
        self.assertEqual(eq3.to_row(),[0,1,1],"This need be in alphabetic order and translate for 0")
