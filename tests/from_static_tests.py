import unittest
from dtreg.from_static import from_static
class TestFromStatic(unittest.TestCase):

    def test_static(self):
        templ = from_static("https://doi.org/22.B34567/1ea0e148d9bbe08335cd")
        expected = {'PIDINST-SchemaObject': [[{'name': 'PIDINST-SchemaObject',
            'identifier': '21.T11969/1ea0e148d9bbe08335cd',
            'schema_type': 'Object'}],
          []]}
        self.assertEqual(templ, expected)
        
if __name__ == '__main__':
    unittest.main()