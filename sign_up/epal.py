
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



class Epal():
    def __init__(self) -> None:
        pass
    def get_code(self,msg):
        code = msg.split(" ")[5].replace(",","")
        return code
    def epal(self,driver,ID):
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
        print('epal')
        number = ID['number']
        driver.get('https://www.epal.gg/')
        click_on(
            "/html/body/div[1]/div[1]/div[1]/div/div[2]/div[4]/div/div/button[2]")
        click_on(
            "/html/body/div[1]/div[1]/div[1]/div[2]/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div/div[1]/div[1]/div/div[2]/div")
        click_on('''/html/body/div[1]/div[1]/div[1]/div[2]/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div/div[2]/
                 div/div[2]/div[1]/form/div[1]/div/div[2]/div/div/div/div[1]/div[1]/div/span[1]''')
        click_on("/html/body/div[1]/div[1]/div[2]/div/button")
        click_on('''/html/body/div[1]/div[1]/div[1]/div[2]/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div/
                 div[2]/div[1]/form/div[1]/div[1]/div[2]/div[1]/div/div/div[1]/div[2]/div/div/div/div[2]/div/div/div/div[230]/div''')
        fill('''/html/body/div[1]/div[1]/div[1]/div[2]/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div/div
             [2]/div/div[2]/div[1]/form/div[1]/div[1]/div[2]/div[1]/div/div/div[2]/span/input''', number.replace("44", ""))
        fill('''/html/body/div[1]/div[1]/div[1]/div[2]/div/div[2]/div[2]/div/div[2]/div/div[2]
             /div/div/div[2]/div/div[2]/div[1]/form/div[2]/div/div[2]/div/div/div/span/input''', ID['password'])
        click_on(
            "/html/body/div[1]/div[1]/div[1]/div[2]/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[2]/label/span[1]/input")
        click_on(
            "/html/body/div[1]/div[1]/div[1]/div[2]/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div/button/span")
        click_on(
            "/html/body/div[4]/div/div[2]/div/div[2]/div/div/div[2]/button[2]")
        sms_code = ()
        fill(
            "/html/body/div[1]/div[1]/div/div[2]/div/div[2]/form/div/div/div/div/div/div/div[1]/input", sms_code[0])
        fill(
            "/html/body/div[1]/div[1]/div/div[2]/div/div[2]/form/div/div/div/div/div/div/div[2]/input", sms_code[1])
        fill(
            "/html/body/div[1]/div[1]/div/div[2]/div/div[2]/form/div/div/div/div/div/div/div[3]/input", sms_code[2])
        fill(
            "/html/body/div[1]/div[1]/div/div[2]/div/div[2]/form/div/div/div/div/div/div/div[4]/input", sms_code[3])
        fill(
            "/html/body/div[1]/div[1]/div/div[2]/div/div[2]/form/div/div/div/div/div/div/div[5]/input", sms_code[4])
        fill(
            "/html/body/div[1]/div[1]/div/div[2]/div/div[2]/form/div/div/div/div/div/div/div[6]/input", sms_code[5])
        click_on(
            "/html/body/div[1]/div[1]/div/div[2]/div/div[2]/div[3]/div/button[2]")
        fill("/html/body/div[1]/div[1]/div/div[2]/div/div[2]/div[3]/div/button[2]",
             ID['first_name']+ID['name']+str(random.randint(30, 40000)))
        click_on(
            "/html/body/div[1]/div[1]/div/div[2]/div[2]/div[2]/form/div[2]/div/div[2]/div/div/div/div[1]/div/span[1]/input")
        click_on(
            "/html/body/div[1]/div[1]/div/div[2]/div[2]/div[2]/form/div[2]/div/div[2]/div/div/div/div[2]/div/div/div/div[1]/div[2]")
        click_on(
            "/html/body/div[1]/div[1]/div/div[2]/div[2]/div[2]/form/div[3]/div/div[2]/div/div/div/div[2]/div[1]/div/span[2]")
        click_on(
            f'''/html/body/div[1]/div[1]/div/div[2]/div[2]/div[2]/form/div[3]/div/
            div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div[{random.randint(2,29)}]''')
        click_on(
            "/html/body/div[1]/div[1]/div/div[2]/div[2]/div[2]/form/div[3]/div/div[2]/div/div/div/div[1]/div[1]/div/span[1]/input")
        click_on(
            f'''/html/body/div[1]/div[1]/div/div[2]/div[2]/div[2]/form/div[3]/div/div[2]
            /div/div/div/div[1]/div[2]/div/div/div/div[2]/div/div/div/div[{random.randint(2,12)}]''')
        click_on(
            f'''/html/body/div[1]/div[1]/div/div[2]/div[2]/div[2]/form/div[3]/div/div[2]
            /div/div/div/div[3]/div[2]/div/div/div/div[2]/div/div/div/div[{random.randint(40,51)}]''')
        click_on("/html/body/div[1]/div[1]/div/div[2]/div[2]/div[3]/button")
        click_on("/html/body/div[6]/div/div[3]/div/div/div[2]/div/button")
        click_on("/html/body/div[1]/div[1]/div[1]/div/div[2]/div[1]/button")
        driver.switch_to.new_window('tab')
        time.sleep(4)


if __name__ == '__main__':
    driver = uc.Chrome(service=ChromeService(ChromeDriverManager().install()))
    Epal().epal(driver)
