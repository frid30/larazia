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


class Airbnb:
    def __init__(self) -> None:
        pass

    def get_code(self, msg):
        code = msg.strip('.').split(' ')[-1]
        return code
    
    def airbnb_up(self):

        def click_on(xpath):
            try:
                driver.implicitly_wait(16)
                driver.find_element(By.XPATH, xpath).click()
                time.sleep(1)
            except:
                print(xpath)

        def fill(xpath, value):
            try:
                driver.implicitly_wait(16)
                searchButton = driver.find_element(By.XPATH, xpath)
                searchButton.send_keys(value)
                time.sleep(1)
            except:
                print(xpath)
        ID = {'bolt': 0, 'bumrungrad': 0, 'email': 'wise.kimberly2918@monmail.fr.nf', 'epal': 0, 'first_name': 'Wise', 'icq': 0, 'lyft': 0, 'name': 'Kimberly', 'password': '*_J&Z5RskQ', 'phone_number': '447413097673', 'postmates': 0, 'yahoo': 0}    
        options = Options()
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--start-maximized")
        options.add_argument("--no-sandbox")
        service_args = [    '--proxy=residential.pingproxies.com:7777',    '--proxy-user=customer-330b0f81CJQKi-sessid-swrWOHQoZ',    '--proxy-pass=Pp1l4hpvzh',    '--proxy-type=http',]

        driver = uc.Chrome(options=options, service_args=service_args)
        driver.get("https://airbnb.com/signup_login")
        time.sleep(3000)
        driver.implicitly_wait(6)
        
click_on("/html/body/div[5]/div/div/div[1]/div/div[1]/div[1]/main/div/div/div/div/div/form/div/div[1]/div[1]/div/div[2]/div/svg")
        
        click_on("/html/body/div[5]/div/div/div[1]/div/div[1]/div[1]/main/div/div/div/div/div/form/div/div[1]/div[1]/div/div[2]/label/div[2]/select/option[230]")
        fill("/html/body/div[5]/div/div/div[1]/div/div[1]/div[1]/main/div/div/div/div/div/form/div/div[1]/div[2]/div/div[2]/label/div[2]/div/input",ID["phone_number"][2:])
        click_on('/html/body/div[5]/div/div/div[1]/div/div[1]/div[1]/main/div/div/div/div/div/form/div/div[4]/button')
        time.sleep(5)
        sms_code = self.get_code(Larazia().get_sms(ID["phone_number"])['msg'])
        if sms_code:        
            fill('''/html/body/div[5]/div/div/div[1]/div/div[1]/div[1]/
                                 main/div/div/div/div/div/div[1]/div[1]/div/label/div/div/input''',sms_code)
            time.sleep(2)
            driver.implicitly_wait(500)
        fill('''/html/body/div[11]/section/div/div/div[2]/div/div[2]/div
             /div/form/div[1]/div[1]/div/div[2]/label/div[2]/div/input''',ID["first_name"])
        driver.implicitly_wait(500)
        time.sleep(2)                
        fill('''/html/body/div[13]/section/div/div/div[2]/div/div[2]
     /div/div/form/div[1]/div[2]/div/div[2]/label/div[2]/div/input''',ID["name"])
        time.sleep(2)
        fill("/html/body/div[13]/section/div/div/div[2]/div/div[2]/div/div/form/div[3]/div[1]/div/div/div[2]/label/div[2]/div/input","19012001")
        time.sleep(2)                

        fill("/html/body/div[13]/section/div/div/div[2]/div/div[2]/div/div/form/div[4]/div/div[1]/label/div[2]/div/input",ID["email"])
        time.sleep(2)                
       
        click_on("/html/body/div[13]/section/div/div/div[2]/div/div[2]/div/div/form/div[7]/button")
        time.sleep(3000)

if __name__=='__main__':
    Airbnb().airbnb_up()