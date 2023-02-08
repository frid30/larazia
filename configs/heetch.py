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
class Heetch:
    def __init__(self) -> None:
        pass
    def get_code(self, msg):
        code = msg.split(' ')[4]
        return code
    def heetch_up(self,driver,ID):
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
        number, first_name, last_name, email = ID['phone_number'], ID['first_name'], ID['last_name'], ID['email']
        driver.maximize_window()
        driver.get(
            "https://auth.heetch.com/?client_id=driver-portal&redirect_uri=https%3A%2F%2Fdriver.heetch.com%2Fauth_callback")
        click_on('//*[@id="axeptio_btn_acceptAll"]')
        click_on(
            '/html/body/div[1]/div/div/div[2]/div[2]/form/div[1]/div/div/div[2]/div/div/div')
        click_on(
            '/html/body/div[1]/div/div/div[2]/div[2]/form/div[1]/div/div/div[2]/ul/li[202]')
        fill('/html/body/div[1]/div/div/div[2]/div[2]/form/div[1]/div/div/input',number[2:])
        click_on('/html/body/div[1]/div/div/div[2]/div[2]/form/button')
        time.sleep(10)
        sms_code = self.get_code(Larazia().get_sms(number)['msg'])
        print(sms_code)
        fill('/html/body/div[1]/div/div/div[2]/div[2]/form/div[1]/div/div/div/input[1]',sms_code[0])
        fill('/html/body/div[1]/div/div/div[2]/div[2]/form/div[1]/div/div/div/input[2]',sms_code[1])
        fill('/html/body/div[1]/div/div/div[2]/div[2]/form/div[1]/div/div/div/input[3]',sms_code[2])
        fill('/html/body/div[1]/div/div/div[2]/div[2]/form/div[1]/div/div/div/input[4]',sms_code[3])
        driver.switch_to.new_window('tab')
        time.sleep(2)
if __name__=='__main__':
    Heetch().heetch_up()