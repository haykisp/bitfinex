import unittest

import requests
from DriverStart.DriverStart import Driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class

Driver.startDriver("https://www.bitfinex.com/",10)

xpath = "//td[contains(text(),'BTCUSD')]/../td[@class=\"col-currency\"][1]"

driver = Driver.wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))

element = driver.find_element_by_xpath(xpath)

UIText = element.text

response = requests.get("https://api.bitfinex.com/v1/tickers").json()

for dict in response:
    if dict["pair"] == "BTCUSD":
        APIText = dict["last_price"]

UIText=float(UIText.replace(",",""))
print("APIText  =  ", APIText)
print("UIText   =  ", UIText)

unittest.TestCase().assertEqual(APIText,UIText,"API and UI values are different")