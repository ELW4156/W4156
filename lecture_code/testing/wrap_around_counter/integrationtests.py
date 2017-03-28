import json

import requests

try:
    import unittest2 as unittest
except ImportError:
    import unittest

class SimpleIntegrationTest(unittest.TestCase):

    def test_pass(self):
        url = 'http://localhost:5000/counter/10'
        res = requests.get(url)
        self.assertEqual(res.status_code, 200)
        jsnres = json.loads(res.text)
        self.assertEqual(jsnres['incremented'], 1)


    def test_malformed(self):
        url = 'http://localhost:5000/counter/foobars'
        res = requests.get(url)
        self.assertEqual(res.status_code, 500)

if __name__ == '__main__':
    unittest.main()

