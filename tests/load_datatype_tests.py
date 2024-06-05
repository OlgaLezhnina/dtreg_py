import unittest
from dtreg.load_datatype import load_datatype
class TestLoadObjects(unittest.TestCase):

    def test_load_proxies(self):
        obj = load_datatype("https://doi.org/21.T11969/1ea0e148d9bbe08335cd")
        self.assertEqual(next(iter(obj.__dict__)), 'pidinst_schemaobject')
        
if __name__ == '__main__':
    unittest.main()