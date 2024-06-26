import unittest
from dtreg.from_static import from_static
class TestFromStatic(unittest.TestCase):
    
    def test_no_static(self):
        no_static = from_static("https://doi.org/21.T11969/111")        
        self.assertEqual(no_static, None)

    def test_static(self):
        templ = from_static("https://doi.org/21.T11969/1ea0e148d9bbe08335cd")
        expected = {'PIDINST-SchemaObject': [[{'dt_name': 'PIDINST-SchemaObject',
            'dt_id': '21.T11969/1ea0e148d9bbe08335cd',
            'dt_class': 'Object'}],
          []]}
        self.assertEqual(templ, expected)
        
if __name__ == '__main__':
    unittest.main()