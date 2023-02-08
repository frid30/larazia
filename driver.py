
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

if __name__=='__main__':
    options = Options()
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--start-maximized")
    options.add_argument("--no-sandbox")
    driver = uc.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://www.finder.com")
    
    click_on("/html/body/header/div/div[2]/div[2]/button")
    click_on("/html/body/div[13]/div/div/div/ul/li[2]/a")
    click_on("/html/body/div[1]/div/div/div/div/div/section/div/div[1]/div[1]/div/div/div[3]/p[2]")
    fill("/html/body/div[1]/div/div/div/div/div/section/div/div[1]/div[1]/div/div/div[4]/input",number)
    click_on("/html/body/div[1]/div/div/div/div/div/section/div/div[1]/div[1]/div/div/div[6]/button")

    time.sleep(3000000)