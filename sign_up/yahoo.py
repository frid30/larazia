
import sys,os,time,random
p_1 = (os.path.dirname(os.path.abspath(__file__)))
p_2 = os.path.dirname(p_1)
sys.path.append(p_2)
from Sms import Larazia, Feed
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
import undetected_chromedriver as uc
#SELENIUM
options = Options()
options.headless = False
options.add_argument("--window-size=1920,1080")
options.add_argument("--start-maximized")
options.add_argument("--no-sandbox")

first_name = Feed().firstname()
name = Feed().name()
password = Feed().password()

email = "muaithai75@gmail.com"


class Yahoo():
    def __init__(self) -> None:
        pass
    def get_code(self,msg):
        return msg.split(" ")[0]
    def yahoo(self,driver,ID):
        def click_on(xpath):
            try:
                driver.implicitly_wait(10)
                driver.find_element(By.XPATH, xpath).click()
                time.sleep(2)
            except:
                pass
        def fill(xpath, value):
            try:
                driver.implicitly_wait(10)
                searchButton = driver.find_element(By.XPATH, xpath)
                searchButton.send_keys(value)
                time.sleep(2)
            except:
                pass
        number,name,first_name,password = ID['number'],ID['name'],ID['first_name'],ID['password']
        print('yahoo')
        driver.maximize_window()
        driver.get("https://www.yahoo.com")
        time.sleep(2)
        click_on("/html/body/div/div/div/div/form/div[2]/div[2]/button")
        click_on(
            "/html/body/header/div[1]/div/div/div/div/div[2]/div/div[3]/div[1]/div/a")
        click_on("/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/form/div[4]/p/a")
        fill(
            "/html/body/div[1]/div[2]/div[1]/div[2]/form/fieldset[1]/div/div[1]/input", name)
        time.sleep(2)
        fill(
            "/html/body/div[1]/div[2]/div[1]/div[2]/form/fieldset[1]/div/div[2]/input", first_name)
        time.sleep(1)
        fill("/html/body/div[1]/div[2]/div[1]/div[2]/form/fieldset[2]/input",
            f"{name}.{first_name}{random.randint(10000,458400000)}")
        fill(
            "/html/body/div[1]/div[2]/div[1]/div[2]/form/fieldset[3]/input", "Monsoleil1")
        fill("/html/body/div[1]/div[2]/div[1]/div[2]/form/div[4]/fieldset/input",
            str(random.randint(1960, 2000)))
        click_on('/html/body/div[1]/div[2]/div[1]/div[2]/form/div[6]/button')
        time.sleep(3)
        fill("/html/body/div[1]/div[2]/div[1]/div[2]/form/fieldset/input",
            number.replace("44", ""))
        time.sleep(5)
        click_on("/html/body/div[1]/div[2]/div[1]/div[2]/form/div[3]/button")

        time.sleep(10)
        sms_code = self.get_code(Larazia().get_sms(number)["msg"])
        fill(
            "/html/body/div[1]/div[2]/div[1]/div[2]/div/form/div[1]/input", sms_code)
        click_on("/html/body/div[1]/div[2]/div[1]/div[2]/div/form/div[2]/button")
        click_on("/html/body/div[1]/div[2]/div[1]/div[2]/form/button")
        click_on("/html/body/div/div/div/div/form/div[2]/div[2]/button")
        click_on("/html/body/div/p/a")
        click_on("/html/body/div[2]/div/main/div[3]/div/div[1]/div/div/div/div/a")
        driver.switch_to.new_window('tab')
        time.sleep(5)
#if __name__=='__main__':
#    driver = uc.Chrome(service=ChromeService(ChromeDriverManager().install()))
#
#    
#