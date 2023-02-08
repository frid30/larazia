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
        ID = {'bolt': 0, 'bumrungrad': 0, 'email': 'graham.glenn578@monmail.fr.nf', 'epal': 0, 'first_name': 'Graham', 'icq': 0, 'lyft': 0, 'last_name': 'Glenn', 'password': ')nYhOBNuO0', 'phone_number': '447413070926', 'postmates': 0, 'yahoo': 0}
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
        driver.get("https://airbnb.com/signup_login")

        driver.implicitly_wait(6)

        click_on("/html/body/div[5]/div/div/div[1]/div/div[1]/div[1]/main/div/div/div/div/div/form/div/div[1]/div[1]/div/div[2]/div/svg")
        
        click_on("/html/body/div[5]/div/div/div[1]/div/div[1]/div[1]/main/div/div/div/div/div/form/div/div[1]/div[1]/div/div[2]/label/div[2]/select/option[230]")
        fill("/html/body/div[5]/div/div/div[1]/div/div[1]/div[1]/main/div/div/div/div/div/form/div/div[1]/div[2]/div/div[2]/label/div[2]/div/input",number[2:])
        click_on('/html/body/div[5]/div/div/div[1]/div/div[1]/div[1]/main/div/div/div/div/div/form/div/div[4]/button')
        time.sleep(5)
        try:
            sms_code = self.get_code(Larazia().get_sms(number)['msg'])                        
            print("")
            fill("/html/body/div[5]/div/div/div[1]/div/div[1]/div[1]/main/div/div/div/div/div/div[1]/div[1]/div/label/div/div/input",sms_code)
        except:
            pass

        time.sleep(3000)

if __name__=='__main__':
    Airbnb().airbnb_up()