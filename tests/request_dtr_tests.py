import unittest
from dtreg.request_dtr import request_dtr
class TestRequest(unittest.TestCase):

    def test_obtain(self):
        b2_schema = request_dtr('https://doi.org/21.T11969/6128ce5def6ffac006e0?locatt=view:json')
        self.assertEqual(b2_schema["name"], 'B2INST-Schema')
        
if __name__ == '__main__':
    unittest.main()
