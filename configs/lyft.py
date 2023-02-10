#A NOUS


from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
import undetected_chromedriver as uc
import sys,os,time,random
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

class Lyft():
    def __init__(self) -> None:
        pass
    def get_code(self,msg):
        return msg.split(" ")[-1]
    def lyft_up(self,driver,ID):
        number,first_name,name,email = ID['phone_number'],ID['first_name'],ID['name'],ID['email']
        def click_on(xpath):
            try:
                driver.implicitly_wait(10)
                driver.find_element(By.XPATH, xpath).click()
                time.sleep(1)
            except Exception as e :
                print(e,ID)
        def fill(xpath, value):
            try:
                driver.implicitly_wait(10)
                searchButton = driver.find_element(By.XPATH, xpath)
                searchButton.send_keys(value)
                time.sleep(1)
            except Exception as e :
                print(e,ID)
        driver.get("https://ride.lyft.com/")
        click_on("/html/body/div[1]/header/nav/a[2]/span/span")
        click_on(
            "/html/body/div[1]/div/span/main/div/div/div/div/form/div/div[5]/div/div[1]/div/button/div/div")
        click_on(
            "/html/body/div[1]/div/span/main/div/div/div/div/form/div/div[5]/div/div[1]/div/select/option[236]")
        fill('''/html/body/div[1]/div/span/main/div/div/div/div/form/div/div[5]/
             div/div[1]/div/div[2]/div[1]/div[1]/span/input''', number.replace("44", ""))
        click_on(
            "/html/body/div[1]/div/span/main/div/div/div/div/form/div/div[10]/span/button/span/span")
        time.sleep(8)
        sms_code = self.get_code(Larazia().get_sms(number)["msg"])
        fill("/html/body/div[1]/div/span/main/div/div/div/div/form/div/div[5]/div/div[1]/div[1]/span/input", sms_code)
        time.sleep(3)

        fill("/html/body/div[1]/div/span/main/div/div/div/div/form/div/div[5]/div[1]/div[1]/div[1]/span/input", first_name)
        fill('/html/body/div[1]/div/span/main/div/div/div/div/form/div/div[5]/div[3]/div[1]/div[1]/span/input', name)
        fill('/html/body/div[1]/div/span/main/div/div/div/div/form/div/div[7]/div[1]/div[1]/span/input', email)
        click_on("/html/body/div[1]/div/span/main/div/div/div/div/form/div/div[10]/div[1]/span/input")
        click_on("/html/body/div[1]/div/span/main/div/div/div/div/form/div/div[13]/span/button/span")
        click_on("/html/body/div[1]/div[2]/div[1]/span/button")
        # click_on('/html/body/div[1]/header/nav/div[5]/button')
        # section = random.randint(1, 9)
        # click_on(f"/html/body/div[1]/div[1]/div/ul[1]/a[{section}]")
        time.sleep(4)
        driver.switch_to.new_window('tab')
    def lyft_in(self,driver,ID):
        number = ID['number']
        def click_on(xpath):
            try:
                driver.implicitly_wait(10)
                driver.find_element(By.XPATH, xpath).click()
                time.sleep(1)
            except Exception as e :
                print(e,ID)
        def fill(xpath, value):
            try:
                driver.implicitly_wait(10)
                searchButton = driver.find_element(By.XPATH, xpath)
                searchButton.send_keys(value)
                time.sleep(1)
            except Exception as e :
                print(e,ID)
        driver.get("https://ride.lyft.com/")
        click_on("/html/body/div[1]/header/nav/a[2]/span/span")
        click_on(
            "/html/body/div[1]/div/span/main/div/div/div/div/form/div/div[5]/div/div[1]/div/button/div/div")
        click_on(
            "/html/body/div[1]/div/span/main/div/div/div/div/form/div/div[5]/div/div[1]/div/select/option[236]")
        fill('''/html/body/div[1]/div/span/main/div/div/div/div/form/
             div/div[5]/div/div[1]/div/div[2]/div[1]/div[1]/span/input''', number.replace("44", ""))
        click_on("/html/body/div[1]/div/span/main/div/div/div/div/form/div/div[10]/span/button/span/span")
        time.sleep(4)
        sms_code = self.get_code(Larazia().get_sms(number)["msg"])
        fill( "/html/body/div[1]/div/span/main/div/div/div/div/form/div/div[5]/div/div[1]/div[1]/span/input", sms_code)
        click_on("/html/body/div[1]/div/span/main/div/div/div/div/div[3]/div[5]/span[1]/button")
        fill("/html/body/div[1]/div/span/main/div/div/div/div/form/div[5]/div[1]/div[1]/span/input", ID['email'])
        click_on("/html/body/div[1]/div/span/main/div/div/div/div/form/div[9]/span/button")
        section = random.randint(1, 9)
        click_on(f"/html/body/div[1]/div[1]/div/ul[1]/a[{section}]")
        driver.switch_to.new_window('tab')
        time.sleep(2)

#if __name__ == '__main__':
#    driver = uc.Chrome(service=ChromeService(ChromeDriverManager().install()))
#    print('mgl')
    