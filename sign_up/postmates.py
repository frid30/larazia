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
    driver.implicitly_wait(1000)
    searchButton = driver.find_element(By.XPATH, xpath)
    searchButton.send_keys(value)
    time.sleep(1)


def click_on(xpath):
    driver.implicitly_wait(1000)
    driver.find_element_by_xpath(xpath).click()
    time.sleep(1)


#if __name__ == '__main__':
#    driver = uc.Chrome(service=ChromeService(ChromeDriverManager().install()))
#    driver.maximize_window()
#    driver.get("https://auth.uber.com/v2/?breeze_local_zone=dca22&inAuthSessionID=3bf414e2-9af0-4575-923c-2cf63f21056b&next_url=https%3A%2F%2Fpostmates.com%2Flogin-redirect%2F%3Fapp_clip%3Dfalse%26campaign%3Dsignin_universal_link%26guest_mode%3Dfalse%26marketing_vistor_id%3D1c3e23e9-cc0e-4a99-92b4-587097bb3505%26redirect%3D%252F&state=aRc_vmxpQO8GvYrqel-Rb1ddP2LvA75m1-5wmTv6_k4%3D&x-uber-app-variant=postmates&x-uber-client-name=postmates-web")
#    click_on('//*[@id="wrapper"]/header/div/div/div/div/a[3]')
#    time.sleep(10000)
#    # click_on('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]')
#    # click_on('//*[@id="wrapper"]/header/div/div/div/div/a[3]')
file = 