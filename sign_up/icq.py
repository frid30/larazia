
import sys
import undetected_chromedriver as uc
from selenium.webdriver.chrome.service import Service as ChromeService
import time
from selenium.webdriver.common.by import By
sys.path.append(r'C:\Users\kamel\Desktop\pumjin')
from getsms import LARAZIA
from get_infos import Feed
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
options = Options()
options.headless = False
options.add_argument("--window-size=1920,1080")
options.add_argument("--start-maximized")
options.add_argument("--no-sandbox")
Getsms=LARAZIA()



def click_on(xpath):
    try:
        driver.implicitly_wait(6)
        driver.find_element(By.XPATH,xpath).click()
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

def get_code(msg):
    code = msg.split(' ')[2]
    return code
number = "447413097673"
first_name = Feed().firstname()
name = Feed().name()
if __name__ == '__main__':
    driver = uc.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://www.icq.com/")
    click_on("/html/body/div/header/div/ul/li[2]/a")
    click_on("/html/body/div[2]/div/div/div[1]/div/div/div[2]/div/button")
    click_on("/html/body/div[2]/div/div[1]/div/form/div/div")
    click_on("/html/body/div[3]/div/div/div/div[2]/div/div[2]/div[2]/div/div[1]/div/div[219]")
    fill("/html/body/div[2]/div/div[1]/div/form/div/input",number.replace("44",""))
    click_on("/html/body/div[2]/div/div[1]/div/form/button")
    time.sleep(7)
    
    sms_code = get_code(Getsms.get_sms(number)["msg"])
    fill("/html/body/div[2]/div/div[1]/div/form/input[1]",sms_code)
    fill("/html/body/div[2]/div[2]/div/div/div/input[1]",first_name)
    fill("/html/body/div[2]/div[2]/div/div/div/input[2]",name)
    click_on("/html/body/div[2]/div[2]/div/div/div/button")
    click_on("/html/body/div[2]/div[3]/div/div[1]/span/div/div[1]")
    click_on("/html/body/div[3]/div/div[1]/div/div/div/div[4]")
    time.sleep(30000)
