#PYTHON
import sys,os,time

#SELENIUM
import undetected_chromedriver as uc
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
options = Options()
options.headless = False
options.add_argument("--window-size=1920,1080")
options.add_argument("--start-maximized")
options.add_argument("--no-sandbox")
#A NOUS
p_1 = (os.path.dirname(os.path.abspath(__file__)))
p_2 = os.path.dirname(p_1)
sys.path.append(p_2)
from Sms import Larazia,Feed

first_name = Feed().firstname()
name = Feed().name()
number = "447413097673"
email = "muaithai75@gmail.com"


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
    
class Bolt:
    def __init__(self) -> None:
        pass
    def get_code(self,msg):
        code = msg.split(' ')[0]
        return code
    def bolt(self,driver):
        driver.maximize_window()
        driver.get('https://bolt.eu/')
        print('bolt')
        time.sleep(4)
        driver.switch_to.new_window('tab')
#        click_on("/html/body/div[3]/div[1]/div/div/div[1]/div/div[1]/div/div/div/a")
#        click_on("/html/body/div[1]/div[1]/div/div/div/div/button[2]")
#        click_on("/html/body/div[2]/div/div/div[2]/div[2]/div/input[2]")
#        time.sleep(2)
#        fill("/html/body/div[2]/div/div/div[2]/form/div/div/input[2]",number.replace("44",""))
#        time.sleep(2)
#        click_on("/html/body/div[2]/div/div/div[2]/form/button")
#        time.sleep(7)
#        sms_code = self.get_code(Larazia().get_sms(number)["msg"])
#        fill("/html/body/div[2]/div/div/div[2]/form/div/input[1]",sms_code[0])
#        fill("/html/body/div[2]/div/div/div[2]/form/div/input[2]",sms_code[1])
#        fill("/html/body/div[2]/div/div/div[2]/form/div/input[3]",sms_code[2])
#        fill("/html/body/div[2]/div/div/div[2]/form/div/input[4]",sms_code[3])
#        fill("/html/body/div[2]/div/div/div[2]/form/input",email)
#        fill("/html/body/div[2]/div/div/div[2]/form/div[1]/input[1]",first_name)
#        fill("/html/body/div[2]/div/div/div[2]/form/div[1]/input[2]",name)
#        time.sleep(2)
#        click_on("/html/body/div[2]/div/div/div[2]/form/button")
#        click_on("/html/body/div[2]/div/div/div[1]/div[1]/button")
#        click_on("/html/body/div[2]/div/div/div[2]/div[2]/div/div[1]/a[1]")
#        click_on("/html/body/div[2]/div/div[2]/div[2]/form/div[3]/label[2]/span")
#        time.sleep(3000)
#
#if __name__=='__main__':
#    driver = uc.Chrome(service=ChromeService(ChromeDriverManager().install()))
#    Bolt().bolt(driver)