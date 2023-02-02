
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import os,time,sys
import random
import undetected_chromedriver as uc
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(path)


number = "447413097673"

if __name__=='__main__':
    options = Options()
    options.headless = False
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--start-maximized")
    options.add_argument("--no-sandbox")
    driver = uc.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://www.google.com")
    time.sleep(3000000)
    click_on("/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/form/div[4]/p/a")
    fill("/html/body/div[1]/div[2]/div[1]/div[2]/form/fieldset[1]/div/div[1]/input",name)
    fill("/html/body/div[1]/div[2]/div[1]/div[2]/form/fieldset[1]/div/div[2]/input",first_name)
    fill("/html/body/div[1]/div[2]/div[1]/div[2]/form/fieldset[2]/input",f"{name}.{first_name}{random.randint(4,300)}")
    fill("/html/body/div[1]/div[2]/div[1]/div[2]/form/fieldset[3]/input",password)
    fill("/html/body/div[1]/div[2]/div[1]/div[2]/form/div[4]/fieldset/input",str(random.randint(1960,2000)))
    click_on('/html/body/div[1]/div[2]/div[1]/div[2]/form/div[6]/button')
    fill("/html/body/div[1]/div[2]/div[1]/div[2]/form/fieldset/input",number.replace("44",""))
    click_on("/html/body/div[1]/div[2]/div[1]/div[2]/form/div[3]/button")
    sms_code = ()
    fill("/html/body/div[1]/div[2]/div[1]/div[2]/div/form/div[1]/input",sms_code)
    click_on("/html/body/div[1]/div[2]/div[1]/div[2]/div/form/div[2]/button")
    click_on("/html/body/div[1]/div[2]/div[1]/div[2]/form/button")
    click_on("/html/body/div/div/div/div/form/div[2]/div[2]/button")
    click_on("/html/body/div/p/a")
    click_on("/html/body/div[2]/div/main/div[3]/div/div[1]/div/div/div/div/a")
    time.sleep(3000000)