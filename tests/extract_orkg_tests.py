import unittest
from dtreg.extract_orkg import extract_orkg


class TestExtractOrkg(unittest.TestCase):

    def test_extract_orkg(self):
        result = extract_orkg("https://incubating.orkg.org/template/R937648")
        expected = {'measurement_scale': [[{'dt_name': 'measurement_scale',
                                            'dt_id': 'R937648',
                                            'dt_class': 'C75002'}],
                                          []]}
        self.assertEqual(result, expected)

    def test_extract_orkg_props(self):
        schema = extract_orkg("https://incubating.orkg.org/template/R855534")
        values = schema["inferential_test_output"][1][0].values()
        expected = "dict_values(['has_format', 'P114000', 1, None, 'Table'])"
        self.assertEqual(str(values), expected)


if __name__ == '__main__':
    unittest.main()
