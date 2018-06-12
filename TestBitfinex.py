import unittest
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from DriverStart import startDriver


class Test(unittest.TestCase):
    def test_UIvsAPI(self):
        """
        getting UI and API values and testing equality
        :return:
        """
        # Start driver
        driver, wait = startDriver("https://www.bitfinex.com/", 10)

        # XPATH of value of BTCUSD
        xpath = "//td[contains(text(),'BTCUSD')]/../td[@class=\"col-currency\"][1]"

        # Waiting to load page(needed element)
        wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))

        # """ Getting value from V1 """
        # response = requests.get("https://api.bitfinex.com/v1/tickers").json()
        # for dict in response:
        #     if dict["pair"] == "BTCUSD":
        #         APIText = dict["last_price"]


        # """ Getting value from V2 """
        # Getting values from API and converting to JSON format
        response = requests.get("https://api.bitfinex.com/v2/ticker/tBTCUSD").json()

        # Getting "last_price" value of BTCUSD from API response
        APIText = float(response[0])

        # Creating element
        BTCUSD = driver.find_element_by_xpath(xpath)

        # Getting value of BTCUSD
        UIText = BTCUSD.text

        # Changing type of value from String to Float
        UIText = float(UIText.replace(",", ""))

        # Comparing API response and UI values
        self.assertEqual(APIText, UIText, "API and UI values are different")
