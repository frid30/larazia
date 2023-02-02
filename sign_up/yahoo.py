
import sys,os,time
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import os,time,sys,random
import undetected_chromedriver as uc
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

p_1 = (os.path.dirname(os.path.abspath(__file__)))
p_2 = os.path.dirname(p_1)
sys.path.append(p_2)
from Sms import Larazia, Feed

path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(path)


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
first_name = Feed().firstname()
name = Feed().name()
password = Feed().password()

if __name__=='__main__':
    options = Options()
    options.headless = False
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--start-maximized")
    options.add_argument("--no-sandbox")
    driver = uc.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://www.google.com")
    driver.get("https://www.yahoo.com")

    click_on("/html/body/div/div/div/div/form/div[2]/div[2]/button")
    click_on("/html/body/header/div[1]/div/div/div/div/div[2]/div/div[3]/div[1]/div/a")
    click_on("/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/form/div[4]/p/a")
    fill("/html/body/div[1]/div[2]/div[1]/div[2]/form/fieldset[1]/div/div[1]/input",name)
    time.sleep(6)

    fill("/html/body/div[1]/div[2]/div[1]/div[2]/form/fieldset[1]/div/div[2]/input",first_name)
    time.sleep(1)

    fill("/html/body/div[1]/div[2]/div[1]/div[2]/form/fieldset[2]/input",f"{name}.{first_name}{random.randint(4,300)}")
    fill("/html/body/div[1]/div[2]/div[1]/div[2]/form/fieldset[3]/input",password)

    fill("/html/body/div[1]/div[2]/div[1]/div[2]/form/div[4]/fieldset/input",str(random.randint(1960,2000)))
    click_on('/html/body/div[1]/div[2]/div[1]/div[2]/form/div[6]/button')

    fill("/html/body/div[1]/div[2]/div[1]/div[2]/form/fieldset/input",number.replace("44",""))

    click_on("/html/body/div[1]/div[2]/div[1]/div[2]/form/div[3]/button")
    time.sleep(6)
    sms_code = get_code(Larazia().get_sms(number)["msg"])
    fill("/html/body/div[1]/div[2]/div[1]/div[2]/div/form/div[1]/input",sms_code)
    click_on("/html/body/div[1]/div[2]/div[1]/div[2]/div/form/div[2]/button")
    click_on("/html/body/div[1]/div[2]/div[1]/div[2]/form/button")
    click_on("/html/body/div/div/div/div/form/div[2]/div[2]/button")
    click_on("/html/body/div/p/a")
    click_on("/html/body/div[2]/div/main/div[3]/div/div[1]/div/div/div/div/a")
    time.sleep(3000000)