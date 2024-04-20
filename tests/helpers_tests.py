import unittest
from dtreg.helpers import format_string
class TestHelpers(unittest.TestCase):

    def test_format_string(self):
        self.assertEqual(format_string("a-B c"), "a_b_c")
        
if __name__ == '__main__':
    unittest.main()
