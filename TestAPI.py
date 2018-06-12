import requests
import unittest


class Test(unittest.TestCase):
    def testPutMethod(self):
        response = requests.put("https://api.bitfinex.com/v1/symbols")
        self.assertEqual(404, response.status_code)
        self.assertEqual('', response.text)

    def testDeleteMethod(self):
        response = requests.delete("https://api.bitfinex.com/v1/symbols")
        self.assertEqual(404, response.status_code)
        self.assertEqual('', response.text)

    def testAPI(self):
        response = requests.get("https://api.bitfinex.com/v1/symbols")
        self.assertEqual(200, response.status_code)
        self.assertEqual(204, len(response.json()))

    def testLimitError(self):
        responseCode = 200
        count = 0
        while responseCode == 200:
            count += 1
            response = requests.get("https://api.bitfinex.com/v1/symbols")
            responseCode = response.status_code

        print("Requests limit = " + str(count-1))
        self.assertEqual(429, response.status_code)
        self.assertIn("error", response.json())
        self.assertEqual("ERR_RATE_LIMIT", response.json()["error"])


