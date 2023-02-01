
import sys
import undetected_chromedriver as uc
from selenium.webdriver.chrome.service import Service as ChromeService
import time
from selenium.webdriver.common.by import By
sys.path.append(r'C:\Users\boufe\OneDrive\Documents\ACCOUNTS\larazia')
from getsms import LARAZIA
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
options = Options()
options.headless = False
options.add_argument("--window-size=1920,1080")
options.add_argument("--start-maximized")
options.add_argument("--no-sandbox")
Getsms=LARAZIA()

def click(n):
    for i in range(n):
        time.sleep(0.5)
        searchButton.click()


def fill(xpath, value):
    driver.implicitly_wait(1000)
    searchButton = driver.find_element(By.XPATH, xpath)
    searchButton.send_keys(value)
    time.sleep(1)


def click_on(xpath):
    driver.implicitly_wait(1000)
    driver.find_element_by_xpath(xpath).click()
    time.sleep(1)

def get_code(msg):
    code = msg.split('.')[0].split(' : ')[1]
    return code


if __name__ == '__main__':
    driver = uc.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://postmates.com/")
    click_on('//*[@id="wrapper"]/header/div/div/div/div/a[3]')
    number = '447413124565'
    fill('//*[@id="PHONE_NUMBER"]', number[2:])
    click_on('//*[@id="wrapper"]/div[1]/div/section[2]/button[1]/div/div[2]')
    msg = Getsms.get_sms(number)['msg']
    code = get_code(msg)
    print(code)