
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
from pymongo import MongoClient
options = Options()
options.add_argument('--headless=new')
options.add_argument("--window-size=1920,1080")
options.add_argument("--start-maximized")
options.add_argument("--no-sandbox")
options.add_argument('--headless=new')
client = MongoClient(
    'mongodb+srv://Walter_McLovin:iammclovin777@cluster0.dejj1c0.mongodb.net/test')
DB = client['PHONE_NUMBERS']
IDs = DB['IDs']
class Main:
    def __init__(self) -> None:
        pass
    def main(self):
        driver = uc.Chrome(
            service=ChromeService(ChromeDriverManager().install()))
        for ID in IDs.find(): 
            Bolt().bolt_up(driver,ID)
            Icq().icq_up(driver, ID)
            # Bumrungrad().bumrungrad_up(driver, ID)
            # Epal().epal_up(driver, ID)
            Yahoo().yahoo_up(driver, ID)
# if __name__=='__main__':
#     Main().main()
print(IDs)
