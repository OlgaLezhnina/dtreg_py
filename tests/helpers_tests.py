import unittest
from dtreg.helpers import format_string, range_split
class TestHelpers(unittest.TestCase):

    def test_format_string(self):
        self.assertEqual(format_string("a-B c"), "a_b_c")
        
    def test_range_split(self):
        self.assertEqual(range_split("0-1"), {'min': '0', 'max': '1'})
        
if __name__ == '__main__':
    unittest.main()
