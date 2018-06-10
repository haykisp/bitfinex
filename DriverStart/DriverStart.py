from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait


class Driver():
    def __init__(self):
        self.chrome_options = Options().add_argument("--start-maximized")
        # driver = webdriver.Chrome(options=chrome_options)
        self.driver = webdriver.Chrome('C:/chromedriver/chromedriver.exe')

    def startDriver(self,URL,waittime):
        self.wait = WebDriverWait(self.driver, waittime)
        self.driver.get(URL)
        return self.driver

    def waitToVisible(self):