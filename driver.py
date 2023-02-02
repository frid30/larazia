
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import os,time,sys
import undetected_chromedriver as uc
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(path)

class Navigate:
    def click_on(self, xpath):
        try:
            driver.implicitly_wait(6)
            driver.find_element(By.XPATH, xpath).click()
            time.sleep(1)
        except:
            pass
    def fill(self, xpath, value):
        try:
            driver.implicitly_wait(6)
            searchButton = driver.find_element(By.XPATH, xpath)
            searchButton.send_keys(value)
            time.sleep(1)
        except:
            pass

if __name__=='__main__':
    options = Options()
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--start-maximized")
    options.add_argument("--no-sandbox")
    driver = uc.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://www.google.com")
    time.sleep(3000000)