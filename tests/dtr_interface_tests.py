import unittest
from dtreg.dtr_interface import select_dtr
class TestDataTypeReg(unittest.TestCase):

    def test_no_dtr(self):
        select_dtr("https://doi.org/22.B34567/1ea0e148d9bbe08335cd")
        self.assertRaisesRegex(ValueError, "SystemExit: Please check whether the schema belongs to the ePIC or the ORKG dtr")
        
if __name__ == '__main__':
    unittest.main()