import unittest
from dtreg.extract_epic import extract_epic
class TestExtract(unittest.TestCase):

    def test_extract(self):
        result = extract_epic("https://doi.org/21.T11969/1ea0e148d9bbe08335cd")
        expected = {'PIDINST-SchemaObject': [[{'dt_name': 'PIDINST-SchemaObject',
            'dt_id': '21.T11969/1ea0e148d9bbe08335cd',
            'dt_class': 'Object'}],
          []]}
        self.assertEqual(result, expected)        
if __name__ == '__main__':
    unittest.main()
