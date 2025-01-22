import unittest
from helpers_mock.mocking import mocked_request_orkg, mocked_request_epic


class TestRequest(unittest.TestCase):

    def test_obtain_epic(self):
        schema = mocked_request_epic(
            'https://doi.org/21.T11969/fb2e379f820c6f8f9e82?locatt=view:json')
        self.assertEqual(schema["name"], 'integer_in_string')

    def test_obtain_orkg(self):
        template_2 = mocked_request_orkg('https://orkg.org/api/templates/R758316')
        self.assertEqual(template_2["label"], 'dtreg_test_template2')


if __name__ == '__main__':
    unittest.main()
