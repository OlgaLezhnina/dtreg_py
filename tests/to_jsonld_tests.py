import unittest
from unittest.mock import patch
import pandas as pd
from dtreg.load_datatype import load_datatype
from dtreg.dtr_interface import Epic
from dtreg.helpers import generate_uid
from dtreg.to_jsonld import differ_input, df_structure, to_jsonld, constants, uid


class TestJsonLd(unittest.TestCase):

    def test_input_numeric(self):
        self.assertEqual(differ_input(3), 3)

    def test_input_df(self):
        df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
        new_uid = generate_uid()
        new_constants = Epic().add_df_constants()
        with patch('dtreg.to_jsonld.constants', new_constants):
            with patch('dtreg.to_jsonld.uid', new_uid):
                result = differ_input(df)
                self.assertEqual(result["label"], "Table")

    def test_input_named_df(self):
        df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
        df.name = "my_results"
        new_uid = generate_uid()
        new_constants = Epic().add_df_constants()
        with patch('dtreg.to_jsonld.constants', new_constants):
            with patch('dtreg.to_jsonld.uid', new_uid):
                result = differ_input(df)
                self.assertEqual(result["label"], "my_results")

    def test_missing_df(self):
        df = pd.DataFrame({'A': [None, 2], 'B': [3, 4]})
        new_uid = generate_uid()
        new_constants = Epic().add_df_constants()
        with patch('dtreg.to_jsonld.constants', new_constants):
            with patch('dtreg.to_jsonld.uid', new_uid):
                result = differ_input(df)
                self.assertEqual(result["rows"][0]["cells"][0]["value"], None)


if __name__ == '__main__':
    unittest.main()
