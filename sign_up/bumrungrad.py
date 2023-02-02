
import sys
import undetected_chromedriver as uc
from selenium.webdriver.chrome.service import Service as ChromeService
import time
from selenium.webdriver.common.by import By
sys.path.append(r'C:\Users\kamel\Desktop\pumjin')
from LARAZIA import LARAZIA
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
    code = msg.split(' ')[0]
    return code
number = "447413097673"

if __name__ == '__main__':
    driver = uc.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://www.bumrungrad.com/")
    time.sleep(30000)
    click_on("/html/body/form/div[5]/div/div[1]/div[3]/div/ul/li[1]/a")
    click_on("/html/body/form/div[5]/div/div[1]/div[3]/div/ul/li[1]/div/a[2]")
    click_on("/html/body/form/div[9]/div/div/div[2]/div[3]/div/a[2]")
    
    click_on("/html/body/div[3]/div[2]/div/div/div[2]/form/div[5]/ul/li/div/div[2]/ul/li[1]/div/div[2]/div/div")
    click_on("/html/body/div[3]/div[2]/div/div/div[2]/form/div[5]/ul/li/div/div[2]/ul/li[1]/div/div[2]/div/ul/li[230]/span[1]")
    fill("/html/body/div[3]/div[2]/div/div/div[2]/form/div[5]/ul/li/div/div[2]/ul/li[1]/div/div[2]/input",number.replace("44",""))
    click_on("/html/body/div[3]/div[2]/div/div/div[2]/form/div[5]/ul/li/div/div[2]/div[4]/button[1]")
    time.sleep(4)
    sms_code = get_code(Getsms.get_sms(number)["msg"])
    fill("/html/body/div[3]/div[2]/div/div/div[2]/form/div[5]/ul/li/div/div[2]/ul/li[2]/div/input",sms_code)
    click_on("/html/body/div[3]/div[2]/div/div/div[2]/form/div[5]/ul/li/div/div[2]/div[4]/button[2]")
    click_on("/html/body/form/div[5]/div/div[2]/div/nav/div/div[1]/div/ul/li[6]/a")

    # time.sleep(30000)