
from selenium.webdriver.common.keys import Keys
import sys,os,time,random
p_1 = (os.path.dirname(os.path.abspath(__file__)))
p_2 = os.path.dirname(p_1)
sys.path.append(p_2)
from Sms import Larazia
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
import undetected_chromedriver as uc
options = Options()
options.headless = False
options.add_argument("--window-size=1920,1080")
options.add_argument("--start-maximized")
options.add_argument("--no-sandbox")
options.add_argument('--headless=new')
class Sinch():
    def __init__(self) -> None:
        pass
    def sinch_up(self):
        driver = uc.Chrome(
            service=ChromeService(ChromeDriverManager().install()))
        ID = {'phone_number': '447413091927', 'first_name': 'Mendez',
              'last_name': 'Micheal', 'password': '9&0E7XkwT@', 'email': 'mendez.micheal1591@uefia.com'}
        def click_on(xpath):
            driver.implicitly_wait(1000)
            driver.find_element(By.XPATH, xpath).click()
            time.sleep(1)
        def fill(xpath, value):
            driver.implicitly_wait(1000)
            searchButton = driver.find_element(By.XPATH, xpath)
            searchButton.send_keys(value)
            time.sleep(1)
        driver.maximize_window()
        driver.get("https://www.sinch.com/")
        click_on('//*[@id="onetrust-reject-all-handler"]')
        click_on(
            '//*[@id="block-themekit-content"]/div/article/div/div[1]/div/div/div/div/div[2]/div[1]/div[3]/div/div/div/a')
        fill('//*[@id="app"]/div[2]/div/div/div/div/div/div/div[3]/form/div[1]/div[1]/div[2]/div/input', ID['first_name'])
        fill('//*[@id="app"]/div[2]/div/div/div/div/div/div/div[3]/form/div[1]/div[2]/div[2]/div/input', ID['last_name'])
        fill( '//*[@id="app"]/div[2]/div/div/div/div/div/div/div[3]/form/div[1]/div[3]/div[2]/div/input',ID['email'])
        fill('//*[@id="app"]/div[2]/div/div/div/div/div/div/div[3]/form/div[1]/div[4]/div[2]/div/input',ID['password'])
        click_on(
            '//*[@id="app"]/div[2]/div/div/div/div/div/div/div[3]/form/div[1]/div[5]/div[2]/div/div')
        time.sleep(400)
        fill('//*[@id="app"]/div[2]/div/div/div/div/div/div/div[3]/form/div[1]/div[5]/div[2]/div/div', 'united kingdom'+Keys.RETURN)
        click_on(
            '//*[@id="app"]/div[2]/div/div/div/div/div/div/div[3]/form/div[1]/div[6]/label/span[1]/span[1]/input')
        click_on('//*[@id="app"]/div[2]/div/div/div/div/div/div/div[3]/form/div[1]/div[7]/button')
        time.sleep(3000)
        




if __name__=='__main__':
    Sinch().sinch_up()