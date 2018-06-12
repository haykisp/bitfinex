import requests
import unittest


class Test(unittest.TestCase):
    def testPutMethod(self):
        response = requests.put("https://api.bitfinex.com/v1/symbols")
        self.assertEqual(404, response.status_code)
        self.assertEqual('',response.text)

    def testDeleteMethod(self):
        response = requests.delete("https://api.bitfinex.com/v1/symbols")
        self.assertEqual(404,response.status_code)
        self.assertEqual('',response.text)



    def testAPI(self):
        response = requests.get("https://api.bitfinex.com/v1/symbols")
        self.assertEqual(200, response.status_code)
        self.assertEqual(204, len(response.json()))


