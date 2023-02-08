#PYTHON
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import sys
import os
import time
p_1 = (os.path.dirname(os.path.abspath(__file__)))
p_2 = os.path.dirname(p_1)
sys.path.append(p_2)
from Sms import Larazia


#SELENIUM
import undetected_chromedriver as uc
from selenium.webdriver.chrome.service import Service as ChromeService

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
options = Options()
options.headless = False
options.add_argument("--window-size=1920,1080")
options.add_argument("--start-maximized")
options.add_argument("--no-sandbox")
options.add_argument('--headless=new')


class Airbnb:
    def __init__(self) -> None:
        pass

    def get_code(self, msg):
        code = msg.strip('.').split(' ')[-1]
        return code
    
    def airbnb_up(self):
        driver = uc.Chrome(
            service=ChromeService(ChromeDriverManager().install()))
        ID = {'phone_number': '447412993405', 'last_name': 'Smith',
              'first_name': 'Benjamin', 'password': 'N9+1q6Dwr9', 'email': 'smith.benjamin2961@courriel.fr.nf'}
        number = ID['phone_number']
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
        driver.maximize_window()
        driver.get("https://www.airbnb.co.uk/login")
        click_on('//*[@id="country"]')
        fill('//*[@id="country"]','united kingdom' + Keys.RETURN)
        fill('//*[@id="phoneInputphoneNumber"]',number[2:])
        click_on('//*[@id="FMP-target"]/div/div/div/form/div/div[4]/button/span[1]/span')
        sms_code = self.get_code(Larazia().get_sms(number)['msg'])                        
        print(sms_code)
        time.sleep(3000)


if __name__=='__main__':
    Airbnb().airbnb_up()