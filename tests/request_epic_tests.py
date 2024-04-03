import unittest
class TestRequest(unittest.TestCase):

    def test_obtain(self):
        b2_schema = request_epic('https://doi.org/21.T11969/6128ce5def6ffac006e0')
        self.assertEqual(b2_schema["name"], 'B2INST-Schema')
        
if __name__ == '__main__':
    unittest.main()
