import unittest
class TestRequest(unittest.TestCase):

    def test_obtain(self):
        no_epic = select_dtr("https://doi.org/22.B34567/1ea0e148d9bbe08335cd")
        self.assertEqual(no_epic, None)
        
if __name__ == '__main__':
    unittest.main()