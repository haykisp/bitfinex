from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait


def startDriver(URL, waittime):
    """
    Starting chrome webdriver
    :param URL: URL to open
    :param waittime: Time for wait
    :return: driver and wait
    """
    chrome_options = Options().add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(URL)
    wait = WebDriverWait(driver, waittime)

    return driver, wait
