
import sys
import undetected_chromedriver as uc
from selenium.webdriver.chrome.service import Service as ChromeService
import time
from selenium.webdriver.common.by import By
sys.path.append(r'C:\Users\kamel\Desktop\pumjin')
from get_infos import Feed
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
options = Options()
options.headless = False
options.add_argument("--window-size=1920,1080")
options.add_argument("--start-maximized")
options.add_argument("--no-sandbox")




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


if __name__ == '__main__':
    driver = uc.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    url = "https://accounts.zoho.com/register?mode=01&servicename=AaaServer&serviceurl=https%3A%2F%2Faccounts.zoho.com%2Foauth%2Fv2%2Fauth%3Fresponse_type%3Dcode%26client_id%3D1000.IEWS07JRYV5H025097LOCFU0XVAF2W%26scope%3Demail%252CAAAServer.profile.READ%26redirect_uri%3Dhttps%253A%252F%252Faccounts.zohoportal.com%252Faccounts%252Fextoauth%252Fclientcallback%26state%3D10000009116.OP-opZzgXxWGntHERY23zSuh2HoX"
    driver.get(url)