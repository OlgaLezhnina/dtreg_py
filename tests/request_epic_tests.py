# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 16:25:52 2024

@author: LezhninaO
"""
import unittest
class TestRequest(unittest.TestCase):

    def test_obtain(self):
        b2_schema = request_epic('https://doi.org/21.T11969/6128ce5def6ffac006e0?locatt=view:json')
        self.assertEqual(b2_schema["name"], 'B2INST-Schema')
        
if __name__ == '__main__':
    unittest.main()
###
import requests
def request_epic(path):
    r = requests.get(path)
    return r.json()
