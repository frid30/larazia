
import undetected_chromedriver as uc
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bson import ObjectId
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from configs.bolt import Bolt
from configs.epal import Epal
from configs.icq import Icq
from configs.lyft import Lyft
from configs.yahoo import Yahoo

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
        for ID in [  {'_id': ObjectId('63e10d7c5fdac2fe6245be1b'), 'phone_number': '447413091927', 'first_name': 'Mendez', 'name': 'Micheal', 'password': '9&0E7XkwT@', 'email': 'mendez.micheal1591@uefia.com'}, {'_id': ObjectId('63e10d7d5fdac2fe6245be1c'), 'phone_number': '447412993405', 'first_name': 'Smith', 'name': 'Benjamin', 'password': 'N9+1q6Dwr9', 'email': 'smith.benjamin2961@courriel.fr.nf'}, {'_id': ObjectId('63e10d7d5fdac2fe6245be1d'), 'phone_number': '447413131560', 'first_name': 'Brown', 'name': 'Tonya', 'password': 'G@N1wDfk2u', 'email': 'brown.tonya1112@hunnur.com'}, {'_id': ObjectId('63e10d7d5fdac2fe6245be1e'), 'phone_number': '447413110936', 'first_name': 'Adams', 'name': 'Holly', 'password': '#IP25Qma@m', 'email': 'adams.holly1024@monmail.fr.nf'}, {'_id': ObjectId('63e10d7e5fdac2fe6245be1f'), 'phone_number': '447412990710', 'first_name': 'Smith', 'name': 'Mr.', 'password': '&&779UFjhm', 'email': 'smith.mr.1757@hunnur.com'}, {'_id': ObjectId('63e10d7e5fdac2fe6245be20'), 'phone_number': '447413112677', 'first_name': 'Campbell', 'name': 'Jacob', 'password': '*7XCc&vi@h', 'email': 'campbell.jacob953@mynes.com'}, {'_id': ObjectId('63e10d7f5fdac2fe6245be21'), 'phone_number': '447413129261', 'first_name': 'Adrian', 'name': 'Christopher', 'password': '0^r3Lh4LCv', 'email': 'adrian.christopher473@monemail.fr.nf'}, {'_id': ObjectId('63e10d7f5fdac2fe6245be22'), 'phone_number': '447413123788', 'first_name': 'Raymond', 'name': 'Alexis', 'password': '(X3QPO*xqy', 'email': 'raymond.alexis1464@mynes.com'}]:
            try:
                print(ID)
                # driver = uc.Chrome(service=ChromeService(ChromeDriverManager().install()))


                # Bolt().bolt_in(driver, ID)
                # Icq().icq_in(driver, ID)
                # #  Epal().epal_in(driver, ID)
                # #  Yahoo().yahoo_in(driver, ID)
                # #  Lyft().lyft_up(driver, ID)
                # driver.quit()
            except Exception as e :
                driver.quit()
                print(ID)
                print(e)
if __name__ == '__main__':
    Main().main()
