
import undetected_chromedriver as uc
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from bson import ObjectId
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from sign_up.bolt import Bolt
from sign_up.epal import Epal
from sign_up.icq import Icq
# from sign_up.bumrungrad import Bumrungrad
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
    'mongodb+srv://Walter_McLovin:iammclovin777@cluster0.d7cbbym.mongodb.net/test')
DB = client['ACCOUNTS']
IDs = DB['IDs']
class Main:
    def __init__(self) -> None:
        pass

    def main(self):
        driver = uc.Chrome(service=ChromeService(ChromeDriverManager().install()))
        ID = random.choice(no)
        try:
            for ID in liste:
                    driver = uc.Chrome(service=ChromeService(ChromeDriverManager().install()))

                    print(ID)
                    Bolt().bolt_up(driver,ID)
                    time.sleep(15)
                    Icq().icq_up(driver, ID)
                    # Bumrungrad().bumrungrad_up(driver, ID)
                    # Epal().epal_up(driver, ID)
                    time.sleep(15)

                    # Yahoo().yahoo_up(driver, ID)
                    driver.quit()
        except Exception as e :
                print(e)
                print(ID)
if __name__=='__main__':
    Main().main()
