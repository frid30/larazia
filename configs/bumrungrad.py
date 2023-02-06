#A NOUS
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
import undetected_chromedriver as uc
import sys,os,time
p_1 = (os.path.dirname(os.path.abspath(__file__)))
p_2 = os.path.dirname(p_1)
sys.path.append(p_2)
from Sms import Larazia
#SELENIUM
options = Options()
options.headless = False
options.add_argument("--window-size=1920,1080")
options.add_argument("--start-maximized")
options.add_argument("--no-sandbox")
options.add_argument('--headless=new')



class Bumrungrad():
    def __init__(self) -> None:
        pass
    def get_code(self,msg):
        code = msg.split(' ')[0]
        return code
    def bumrungrad_up(self,driver,ID):
        def click_on(xpath):
            try:
                driver.implicitly_wait(6)
                driver.find_element(By.XPATH, xpath).click()
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
        print('bumrungrad')
        number = ID['phone_number']
        driver.get('https://www.bumrungrad.com/')
        time.sleep(4)
        click_on("/html/body/form/div[5]/div/div[1]/div[3]/div/ul/li[1]/a")
        click_on("/html/body/form/div[5]/div/div[1]/div[3]/div/ul/li[1]/div/a[2]")
        click_on("/html/body/form/div[9]/div/div/div[2]/div[3]/div/a[2]")
        click_on("/html/body/div[3]/div[2]/div/div/div[2]/form/div[5]/ul/li/div/div[2]/ul/li[1]/div/div[2]/div/div")
        click_on("/html/body/div[3]/div[2]/div/div/div[2]/form/div[5]/ul/li/div/div[2]/ul/li[1]/div/div[2]/div/ul/li[230]/span[1]")
        fill("/html/body/div[3]/div[2]/div/div/div[2]/form/div[5]/ul/li/div/div[2]/ul/li[1]/div/div[2]/input",number.replace("44",""))
        click_on("/html/body/div[3]/div[2]/div/div/div[2]/form/div[5]/ul/li/div/div[2]/div[4]/button[1]")
        time.sleep(10)
        sms_code = self.get_code(Larazia().get_sms(number)["msg"])
        fill("/html/body/div[3]/div[2]/div/div/div[2]/form/div[5]/ul/li/div/div[2]/ul/li[2]/div/input",sms_code)
        click_on("/html/body/div[3]/div[2]/div/div/div[2]/form/div[5]/ul/li/div/div[2]/div[4]/button[2]")
        click_on("/html/body/form/div[5]/div/div[2]/div/nav/div/div[1]/div/ul/li[6]/a")
        driver.switch_to.new_window('tab')
        time.sleep(4)
    def bumrungrad_in(self,driver,ID):
        number = ID['number']
        def click_on(xpath):
            try:
                driver.implicitly_wait(6)
                driver.find_element(By.XPATH, xpath).click()
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
        driver.maximize_window()
        driver.get("https://www.bumrungrad.com/")
        click_on("/html/body/form/div[5]/div/div[1]/div[3]/div/ul/li[1]/a")
        click_on("/html/body/form/div[5]/div/div[1]/div[3]/div/ul/li[1]/div/a[1]")
        click_on("/html/body/form/div[8]/div/div/div[2]/div[3]/div/a[2]")
        click_on(
            "/html/body/div[3]/div[2]/div/div/div[2]/form/div[5]/ul/li/div/div[2]/ul/li[1]/div/div[2]/div/div")
        click_on(
            "/html/body/div[3]/div[2]/div/div/div[2]/form/div[5]/ul/li/div/div[2]/ul/li[1]/div/div[2]/div/ul/li[230]/span[1]")
        fill("/html/body/div[3]/div[2]/div/div/div[2]/form/div[5]/ul/li/div/div[2]/ul/li[1]/div/div[2]/input",
            number.replace("44", ""))
        click_on(
            "/html/body/div[3]/div[2]/div/div/div[2]/form/div[5]/ul/li/div/div[2]/div[4]/button[1]")
        time.sleep(10)
        sms_code = self.get_code(Larazia().get_sms(number)["msg"])
        fill(
            "/html/body/div[3]/div[2]/div/div/div[2]/form/div[5]/ul/li/div/div[2]/ul/li[2]/div/input", sms_code)
        click_on(
            "/html/body/div[3]/div[2]/div/div/div[2]/form/div[5]/ul/li/div/div[2]/div[4]/button[2]")
        click_on(
            "/html/body/form/div[5]/div/div[2]/div/nav/div/div[1]/div/ul/li[6]/a")


if __name__ == '__main__':
   driver = uc.Chrome(service=ChromeService(ChromeDriverManager().install()))
   Bumrungrad().bumrungrad(driver,ID)