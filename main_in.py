
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
import os
import sys
import time
from pymongo import MongoClient
options = Options()
options.add_argument('--headless=new')
options.add_argument("--window-size=1920,1080")
options.add_argument("--start-maximized")
options.add_argument("--no-sandbox")
options.add_argument('--headless=new')
client = MongoClient(
    'mongodb+srv://Walter_McLovin:iammclovin777@cluster0.d7cbbym.mongodb.net/test')
DB = client['ACCOUNTS']
IDs = DB['IDs']


class Main:
    def __init__(self) -> None:
        pass

    def main(self):
        driver = uc.Chrome(
            service=ChromeService(ChromeDriverManager().install()))
        #    Bolt().bolt_in(driver, ID)
        #    Icq().icq_in(driver, ID)
        #    Bumrungrad().bumrungrad_in(driver, ID)
        #    Epal().epal_in(driver, ID)
        #    Yahoo().yahoo_in(driver, ID)


if __name__ == '__main__':
    Main().main()
