
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import os,time,sys

p_1 = (os.path.dirname(os.path.abspath(__file__)))
p_2 = os.path.dirname(p_1)
sys.path.append(p_2)
import random
import undetected_chromedriver as uc
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from Sms import Larazia, Feed

def click_on( xpath):
    try:
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, xpath).click()
        time.sleep(2)
    except:
        pass
def fill(xpath, value):
    try:
        driver.implicitly_wait(10)
        searchButton = driver.find_element(By.XPATH, xpath)
        searchButton.send_keys(value)
        time.sleep(2)
    except:
        pass
def get_code(msg):
    return msg.split(" ")[0]

number = "447413131560"
first_name = "Michael"
name = "Jeffrey"
if __name__=='__main__':
    options = Options()
    options.headless = False
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--start-maximized")
    options.add_argument("--no-sandbox")
    driver = uc.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://www.google.com")
    driver.get("https://www.yahoo.com")
    time.sleep(6)
    click_on("/html/body/div/div/div/div/form/div[2]/div[2]/button")
    click_on("/html/body/header/div[1]/div/div/div/div/div[2]/div/div[3]/div[1]/div/a")
    fill("/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/form/div[1]/div[3]/input",number.replace("44",""))
    click_on("/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/form/div[2]/input")
    time.sleep(2)
    fill("/html/body/div[1]/div[2]/div[1]/div[2]/div/form/div[1]/div[2]/div[1]/input",first_name)
    fill("/html/body/div[1]/div[2]/div[1]/div[2]/div/form/div[1]/div[2]/div[2]/input",name)
    time.sleep(1)

    click_on("/html/body/div[1]/div[2]/div[1]/div[2]/div/form/div[2]/button")
    time.sleep(random.randint(1,4))
            
    click_on("/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/form/div[2]/button")
    time.sleep(8)

    sms_code = get_code(Larazia().get_sms(number)["msg"])
    fill("/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/form/div[1]/input",sms_code)
    click_on("/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/form/div[2]/button")
    click_on("/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/form/ul/li/div[2]/button")
    click_on("/html/body/header/div[1]/div/div/div/div/div[3]/div/div/ul/li[1]/a")
    click_on("/html/body/div[1]/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div/div[2]/div/div[1]/ul/li[1]/div/a/div[1]/div[2]/span")
    time.sleep(3000000)