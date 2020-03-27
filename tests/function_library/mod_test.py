
# Excel reference: https://support.office.com/en-us/article/MOD-function-9b6cd169-b6ee-406a-a97b-edf2a9dc24f3

import unittest

import pandas as pd

from koala_xlcalculator.function_library import Mod
from koala_xlcalculator.exceptions import ExcelError
from koala_xlcalculator import ModelCompiler
from koala_xlcalculator import Evaluator


class TestMod(unittest.TestCase):

    def setUp(self):
        compiler = ModelCompiler()
        self.model = compiler.read_and_parse_archive(r"./tests/resources/MOD.xlsx")
        self.model.build_code()
        self.evaluator = Evaluator(self.model)


    def test_first_argument_validity(self):
        with self.assertRaises(ExcelError):
            Mod.mod(2.2, 1)


    def test_second_argument_validity(self):
        with self.assertRaises(ExcelError):
            Mod.mod(2, 1.1)


    def test_output_value(self):
        self.assertEqual(Mod.mod(10, 4), 2)


    def test_evaluation_A1(self):
        excel_value = self.evaluator.get_cell_value('Sheet1!A1')
        value = self.evaluator.evaluate('Sheet1!A1')
        self.assertEqual( excel_value, value )


    @unittest.skip('Problem evalling: #VALUE! for Sheet1!A2, Mod.mod(Evaluator.apply_one("minus", 3, None, None),2)')
    def test_evaluation_A2(self):
        excel_value = self.evaluator.get_cell_value('Sheet1!A2')
        value = self.evaluator.evaluate('Sheet1!A2')
        self.assertEqual( excel_value, value )


    @unittest.skip('Problem evalling: #VALUE! for Sheet1!A3, Mod.mod(3,Evaluator.apply_one("minus", 2, None, None))')
    def test_evaluation_A3(self):
        excel_value = self.evaluator.get_cell_value('Sheet1!A3')
        value = self.evaluator.evaluate('Sheet1!A3')
        self.assertEqual( excel_value, value )

    @unittest.skip('Problem evalling: mod() missing 1 required positional argument: "q" for Sheet1!A4, Mod.mod(Evaluator.apply_one("minus", 3, None, None))')
    def test_evaluation_A4(self):
        excel_value = self.evaluator.get_cell_value('Sheet1!A4')
        value = self.evaluator.evaluate('Sheet1!A4')
        self.assertEqual( excel_value, value )
