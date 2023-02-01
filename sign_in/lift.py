import undetected_chromedriver as uc
from selenium.webdriver.chrome.service import Service as ChromeService
import time
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import sys
sys.path.append(r'C:\Users\kamel\Desktop\pumjin')
from getsms import LARAZIA
get_thesms= LARAZIA()


def get_code(msg):
    return msg.split(" ")[-1]

options = Options()
options.headless = False
options.add_argument("--window-size=1920,1080")
options.add_argument("--start-maximized")
options.add_argument("--no-sandbox")

def click_on(xpath):
    driver.implicitly_wait(1000)
    driver.find_element(By.XPATH,xpath).click()
    time.sleep(1)

def fill(xpath, value):
    driver.implicitly_wait(1000)

    searchButton = driver.find_element(By.XPATH, xpath)
    searchButton.send_keys(value)
    time.sleep(1)

number = "447413083728"
print('mario')
if __name__ == '__main__':
    driver = uc.Chrome(service=ChromeService(ChromeDriverManager().install()))
    print('mgl')
    driver.get("https://ride.lyft.com/")
    click_on("/html/body/div[1]/header/nav/a[2]/span/span")
    click_on("/html/body/div[1]/div/span/main/div/div/div/div/form/div/div[5]/div/div[1]/div/button/div/div")

    click_on("/html/body/div[1]/div/span/main/div/div/div/div/form/div/div[5]/div/div[1]/div/select/option[236]")

    fill("/html/body/div[1]/div/span/main/div/div/div/div/form/div/div[5]/div/div[1]/div/div[2]/div[1]/div[1]/span/input",number.replace("44",""))

    click_on("/html/body/div[1]/div/span/main/div/div/div/div/form/div/div[10]/span/button/span/span")
    time.sleep(4)
    smscode = None
    while not smscode :
        smscode = get_code(get_thesms.get_sms(number)["msg"])

    prename = "Ouide"
    name = "Jasoo"
    email = "muaithai75@gmail.com"
    fill("/html/body/div[1]/div/span/main/div/div/div/div/form/div/div[5]/div/div[1]/div[1]/span/input",smscode)
    click_on("/html/body/div[1]/div/span/main/div/div/div/div/div[3]/div[5]/span[1]/button/span/span/span/span")
    fill("/html/body/div[1]/div/span/main/div/div/div/div/form/div/div[5]/div[1]/div[1]/div[1]/span/input",prename)
    fill('/html/body/div[1]/div/span/main/div/div/div/div/form/div/div[5]/div[3]/div[1]/div[1]/span/input',name)
    fill('/html/body/div[1]/div/span/main/div/div/div/div/form/div/div[7]/div[1]/div[1]/span/input',email)
    click_on("/html/body/div[1]/div/span/main/div/div/div/div/form/div/div[10]/div[1]/span/input")
    click_on("/html/body/div[1]/div[1]/div/ul[1]/li/div")

    ### after being logged in
    # click_on("/html/body/div[1]/header/nav/div[5]/button/span")
    
    # "/html/body/div[1]/div[1]/div/ul[1]/li"
    # "/html/body/div[1]/div[1]/div/ul[1]/a[6]"
    time.sleep(3000)
    