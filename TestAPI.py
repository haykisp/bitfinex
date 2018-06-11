import requests
import unittest


class Test(unittest.TestCase):
    def testWithPutMethod(self):
        response = requests.put("https://api.bitfinex.com/v1/symbols")
        self.assertEqual(404, response.status_code)

    def testAPI(self):
        response = requests.get("https://api.bitfinex.com/v1/symbols")
        self.assertEqual(200, response.status_code)
        self.assertEqual(204, len(response.json()))

    def test(self):
        response = requests.get("https://api.bitfinex.com/v1/symbols")
        print(response.headers)
