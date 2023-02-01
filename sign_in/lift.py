import undetected_chromedriver as uc
from selenium.webdriver.chrome.service import Service as ChromeService
import time
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
options = Options()
options.headless = False
options.add_argument("--window-size=1920,1080")
options.add_argument("--start-maximized")
options.add_argument("--no-sandbox")
def click(n):
    for i in range(n):
        time.sleep(0.5)
        searchButton.click()


def fill(xpath, value):
    searchButton = driver.find_element(By.XPATH, xpath)
    searchButton.send_keys(value)


print('mario')
if __name__ == '__main__':
    driver = uc.Chrome(service=ChromeService(ChromeDriverManager().install()))
    print('mgl')
    driver.get("https://ride.lyft.com/")
    searchButton = driver.find_element(by=By.XPATH, value="/html/body/div[1]/header/nav/a[2]/span/span")

    click(1)
    searchButton = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/span/main/div/div/div/div/form/div/div[5]/div/div[1]/div/button/div/div")
    click(1)

    searchButton = driver.find_element(by=By.XPATH,value="/html/body/div[1]/div/span/main/div/div/div/div/form/div/div[5]/div/div[1]/div/select/option[236]")
    click(1)
    fill("/html/body/div[1]/div/span/main/div/div/div/div/form/div/div[5]/div/div[1]/div/div[2]/div[1]/div[1]/span/input","7413069667")
    searchButton = driver.find_element(by=By.XPATH,value="/html/body/div[1]/div/span/main/div/div/div/div/form/div/div[10]/span/button/span/span")
    click(1)
    smscode = ()
    fill("/html/body/div[1]/div/span/main/div/div/div/div/form/div/div[5]/div/div[1]/div[1]/span/input",smscode)
    searchButton = driver.find_element(by=By.XPATH,value="/html/body/div[1]/div/span/main/div/div/div/div/div[3]/div[5]/span[1]/button/span/span/span/span")
    click(1)
    ### after being logged in
    searchButton = driver.find_element(by=By.XPATH,value="/html/body/div[1]/header/nav/div[5]/button/span")
    click(1)
    "/html/body/div[1]/div[1]/div/ul[1]/li"
    "/html/body/div[1]/div[1]/div/ul[1]/a[6]"
    time.sleep(3000)
    