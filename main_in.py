
import undetected_chromedriver as uc
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from configs.bolt import Bolt
from configs.epal import Epal
from configs.icq import Icq
from configs.lyft import Lyft
from configs.yahoo import Yahoo
from database.data_mongo import Data

options = Options()
options.add_argument('--headless=new')
options.add_argument("--window-size=1920,1080")
options.add_argument("--start-maximized")
options.add_argument("--no-sandbox")
options.add_argument('--headless=new')

class Main:
    def __init__(self) -> None:
        pass
    def main(self):
        driver = uc.Chrome(
            service=ChromeService(ChromeDriverManager().install()))
        for ID in Data().IDs():
            for i in range(3):
                try:
                    Bolt().bolt_in(driver, ID)
                    Icq().icq_in(driver, ID)
                    Epal().epal_in(driver, ID)
                    Yahoo().yahoo_in(driver, ID)
                    Lyft().lyft_in(driver, ID)
                except Exception as e:
                    print(e)
if __name__ == '__main__':
    Main().main()
