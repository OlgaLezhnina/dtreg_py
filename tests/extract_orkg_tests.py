import unittest
from dtreg.extract_orkg import extract_orkg
class TestExtract(unittest.TestCase):

    def test_extract(self):
        result = extract_orkg("https://incubating.orkg.org/template/R937648")
        expected = {'measurement_scale': [[{'dt_name': 'measurement_scale',
            'dt_id': 'R937648',
            'dt_class': 'C75002'}],
          []]}
        self.assertEqual(result, expected)        
if __name__ == '__main__':
    unittest.main()
