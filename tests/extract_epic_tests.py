import unittest
from unittest.mock import patch
from helpers_mock.mocking import mocked_request_epic
from dtreg.extract_epic import extract_epic


@patch("dtreg.extract_epic.request_dtr", mocked_request_epic)
class TestExtractEpic(unittest.TestCase):

    def test_extract_epic(self):
        result = extract_epic("https://doi.org/21.T11969/fb2e379f820c6f8f9e82")
        expected = {'integer_in_string': [[{'dt_name': 'integer_in_string',
                                            'dt_id': 'fb2e379f820c6f8f9e82',
                                            'dt_class': 'String'}],
                                          [{'dtp_name': 'pattern',
                                            'dtp_id': '21.T11969/fb2e379f820c6f8f9e82#pattern',
                                            'dtp_card_min': None,
                                            'dtp_card_max': None,
                                            'dtp_value_type': '^[0-9]+$'}]]}
        self.assertEqual(result, expected)

    def test_extract_epic_props(self):
        schema = extract_epic("https://doi.org/21.T11969/31483624b5c80014b6c7")
        values = schema["matrix_size"][1][0].values()
        expected = "dict_values(['number_of_rows', "\
            "'21.T11969/31483624b5c80014b6c7#number_of_rows', 1, 1, "\
            "'21.T11969/fb2e379f820c6f8f9e82'])"
        self.assertEqual(str(values), expected)


if __name__ == '__main__':
    unittest.main()
