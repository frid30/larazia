
import undetected_chromedriver as uc
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from sign_up.bolt import Bolt
from sign_up.epal import Epal
from sign_up.icq import Icq
from sign_up.bumrungrad import Bumrungrad
from sign_up.yahoo import Yahoo
import os,sys,time

#SELENIUM
from Sms import Feed
class Main:
    def __init__(self) -> None:
        pass
    def main(self):
        driver = uc.Chrome(
            service=ChromeService(ChromeDriverManager().install()))
        ID = {'number': '447412993405', 'name': Feed().name(
        ), 'first_name': Feed().firstname(), 'password': Feed().password}
        options = Options()
        options.add_argument('--headless=new')
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--start-maximized")
        options.add_argument("--no-sandbox")
        options.add_argument('--headless=new')
        Bolt().bolt(driver,ID)
        Icq().icq(driver, ID)
        # Bumrungrad().bumrungrad(driver, ID)
        # Epal().epal(driver, ID)
        Yahoo().yahoo(driver, ID)
if __name__=='__main__':
    Main().main()
