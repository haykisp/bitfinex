import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options().add_argument("--start-maximized")
driver = webdriver.Chrome(options=chrome_options)

wait = WebDriverWait(driver, 10)

driver.get("https://www.bitfinex.com/")

xpath = "//td[contains(text(),'BTCUSD')]/../td[@class=\"col-currency\"][1]"

wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))

element = driver.find_element_by_xpath(xpath)

UIText = element.text

response = requests.get("https://api.bitfinex.com/v1/tickers").json()

for dict in response:
    if dict["pair"] == "BTCUSD":
        APIText = dict["last_price"]

print("APIText  =  ", APIText)
print("UIText   =  ", UIText)
