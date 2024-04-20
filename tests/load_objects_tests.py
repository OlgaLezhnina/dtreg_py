import unittest
from dtreg.load_objects import load_objects
class TestLoadObjects(unittest.TestCase):

    def test_load_proxies(self):
        obj = load_objects("https://doi.org/21.T11969/1ea0e148d9bbe08335cd")
        self.assertEqual(next(iter(obj.__dict__)), 'PIDINST-SchemaObject')
        
if __name__ == '__main__':
    unittest.main()