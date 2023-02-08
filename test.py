from capmonster_python import RecaptchaV2Task,RecaptchaV3Task

from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import os,time,sys
import undetected_chromedriver as uc
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(path)


def click_on(xpath):
    try:
        driver.implicitly_wait(6)
        driver.find_element(By.XPATH, xpath).click()
        time.sleep(1)
    except:
        pass
def fill( xpath, value):
    try:
        driver.implicitly_wait(6)
        searchButton = driver.find_element(By.XPATH, xpath)
        searchButton.send_keys(value)
        time.sleep(1)
    except:
        pass


# url = "https://login.yahoo.net"
# capmonster = RecaptchaV2Task("5d4fc8d721ca7365258b20e9de8c06fc")
# task_id = capmonster.create_task(
#     url,    "6Ldbp6saAAAAAAwuhsFeAysZKjR319pRcKUitPUO")
# result = capmonster.join_task_result(task_id)
a = "result.get("
print(f"""document.getElementsByClassName('g-recaptcha-response').value = "{a}" """)