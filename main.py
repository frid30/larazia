
import undetected_chromedriver as uc
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from sign_up.bolt import Bolt
import os,sys,time
path = os.path.join(os.path.dirname(
os.path.abspath(__file__)), 'sign_up')
#SELENIUM


def click_on(xpath):
    try:
        driver.implicitly_wait(6)
        driver.find_element(By.XPATH, xpath).click()
        time.sleep(1)
    except:
        pass


def fill(xpath, value):
    try:
        driver.implicitly_wait(6)
        searchButton = driver.find_element(By.XPATH, xpath)
        searchButton.send_keys(value)
        time.sleep(1)
    except:
        pass

if __name__=='__main__':
    options = Options()
    options.headless = False
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--start-maximized")
    options.add_argument("--no-sandbox")
    driver = uc.Chrome(service=ChromeService(ChromeDriverManager().install()))
    Bolt().bolt(driver)