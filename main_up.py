
import undetected_chromedriver as uc
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from sign_up.bolt import Bolt
from sign_up.epal import Epal
from sign_up.icq import Icq
from bson import ObjectId
# from sign_up.bumrungrad import Bumrungrad
from sign_up.yahoo import Yahoo
import os,sys,time,random,json
from pymongo import MongoClient
options = Options()
options.add_argument('--headless=new')
options.add_argument("--window-size=1920,1080")
options.add_argument("--start-maximized")
options.add_argument("--no-sandbox")
options.add_argument('--headless=new')
# # client = MongoClient('mongodb+srv://Walter_McLovin:iammclovin777@cluster0.d7cbbym.mongodb.net/test')
# DB = client['ACCOUNTS']
# IDs = DB['IDs']

no = [{'_id': ObjectId('63e10d755fdac2fe6245be0a'), 'phone_number': '447412999637', 'first_name': 'Reed', 'name': 'Matthew', 'password': ')+78FaeeWC', 'email': 'reed.matthew1600@courriel.fr.nf'}, {'_id': ObjectId('63e10d755fdac2fe6245be0b'), 'phone_number': '447413069667', 'first_name': 'Campbell', 'name': 'Jamie', 'password': 'W6WelcNr)0', 'email': 'campbell.jamie890@hunnur.com'}, {'_id': ObjectId('63e10d765fdac2fe6245be0c'), 'phone_number': '447413133524', 'first_name': 'Adams', 'name': 'Crystal', 'password': 'a@E74Nq3!O', 'email': 'adams.crystal2336@monemail.fr.nf'}, {'_id': ObjectId('63e10d765fdac2fe6245be0d'), 'phone_number': '447413133905', 'first_name': 'Davis', 'name': 'Kayla', 'password': '@8wXlz7qrV', 'email': 'davis.kayla1253@uefia.com'}, {'_id': ObjectId('63e10d775fdac2fe6245be0e'), 'phone_number': '447413124565', 'first_name': 'Ashley', 'name': 'Jason', 'password': '_Q206VaoqA', 'email': 'ashley.jason1694@courriel.fr.nf'}, {'_id': ObjectId('63e10d775fdac2fe6245be0f'), 'phone_number': '447412989223', 'first_name': 'Andrade', 'name': 'Raymond', 'password': '&6ch1bLBz$', 'email': 'andrade.raymond784@mynes.com'}, {'_id': ObjectId('63e10d775fdac2fe6245be10'), 'phone_number': '447413127992', 'first_name': 'Salazar', 'name': 'Margaret', 'password': 'kpT1hDoy&I', 'email': 'salazar.margaret1662@monemail.fr.nf'}, {'_id': ObjectId('63e10d785fdac2fe6245be11'), 'phone_number': '447413107409', 'first_name': 'Grimes', 'name': 'Cindy', 'password': '@85ALf4BO1', 'email': 'grimes.cindy1795@monemail.fr.nf'}, {'_id': ObjectId('63e10d785fdac2fe6245be12'), 'phone_number': '447413083728', 'first_name': 'Ross', 'name': 'Troy', 'password': 'X&d4TfeuMW', 'email': 'ross.troy2442@hunnur.com'}, {'_id': ObjectId('63e10d795fdac2fe6245be13'), 'phone_number': '447412992725', 'first_name': 'Bauer', 'name': 'Douglas', 'password': '*C4Jd+uq*5', 'email': 'bauer.douglas2118@hunnur.com'}, {'_id': ObjectId('63e10d795fdac2fe6245be14'), 'phone_number': '447413097673', 'first_name': 'Wise', 
'name': 'Kimberly', 'password': '*_J&Z5RskQ', 'email': 'wise.kimberly2918@monmail.fr.nf'}, {'_id': ObjectId('63e10d7a5fdac2fe6245be15'), 'phone_number': '447412989377', 'first_name': 'Santiago', 'name': 'Jo', 'password': '!)ENR)4j7O', 'email': 'santiago.jo363@courriel.fr.nf'}, {'_id': ObjectId('63e10d7a5fdac2fe6245be16'), 'phone_number': '447413070926', 'first_name': 'Graham', 'name': 'Glenn', 'password': ')nYhOBNuO0', 'email': 'graham.glenn578@monmail.fr.nf'}, {'_id': ObjectId('63e10d7a5fdac2fe6245be17'), 'phone_number': '447412985739', 'first_name': 'Meyer', 'name': 'Ethan', 'password': 'bJD#9IdcJ(', 'email': 'meyer.ethan1679@hunnur.com'}, {'_id': ObjectId('63e10d7b5fdac2fe6245be18'), 'phone_number': '447412984610', 'first_name': 'Griffith', 'name': 'Mark', 'password': 'nAMpJ8Oak^', 'email': 'griffith.mark309@monmail.fr.nf'}, {'_id': ObjectId('63e10d7b5fdac2fe6245be19'), 'phone_number': '447413127602', 'first_name': 'Olson', 'name': 'Kirk', 'password': 'c4$xxIvo)u', 'email': 'olson.kirk2856@mynes.com'}, {'_id': ObjectId('63e10d7c5fdac2fe6245be1a'), 'phone_number': '447413130988', 'first_name': 'Smith', 'name': 'Melissa', 'password': '(50%DvL!UQ', 'email': 'smith.melissa2471@monmail.fr.nf'}, {'_id': ObjectId('63e10d7c5fdac2fe6245be1b'), 'phone_number': '447413091927', 'first_name': 'Mendez', 'name': 'Micheal', 'password': '9&0E7XkwT@', 'email': 'mendez.micheal1591@uefia.com'}, {'_id': ObjectId('63e10d7d5fdac2fe6245be1c'), 'phone_number': '447412993405', 'first_name': 'Smith', 'name': 'Benjamin', 'password': 'N9+1q6Dwr9', 'email': 'smith.benjamin2961@courriel.fr.nf'}, {'_id': ObjectId('63e10d7d5fdac2fe6245be1d'), 'phone_number': '447413131560', 'first_name': 'Brown', 'name': 'Tonya', 'password': 'G@N1wDfk2u', 'email': 'brown.tonya1112@hunnur.com'}, {'_id': ObjectId('63e10d7d5fdac2fe6245be1e'), 'phone_number': '447413110936', 'first_name': 'Adams', 'name': 'Holly', 'password': '#IP25Qma@m', 'email': 'adams.holly1024@monmail.fr.nf'}, {'_id': ObjectId('63e10d7e5fdac2fe6245be1f'), 'phone_number': '447412990710', 'first_name': 'Smith', 'name': 'Mr.', 'password': '&&779UFjhm', 'email': 'smith.mr.1757@hunnur.com'}, {'_id': ObjectId('63e10d7e5fdac2fe6245be20'), 'phone_number': '447413112677', 'first_name': 'Campbell', 'name': 'Jacob', 'password': '*7XCc&vi@h', 'email': 'campbell.jacob953@mynes.com'}, {'_id': ObjectId('63e10d7f5fdac2fe6245be21'), 'phone_number': '447413129261', 'first_name': 'Adrian', 'name': 'Christopher', 'password': '0^r3Lh4LCv', 'email': 'adrian.christopher473@monemail.fr.nf'}, {'_id': ObjectId('63e10d7f5fdac2fe6245be22'), 'phone_number': '447413123788', 'first_name': 'Raymond', 'name': 'Alexis', 'password': '(X3QPO*xqy', 'email': 'raymond.alexis1464@mynes.com'}]
class Main:
    def __init__(self) -> None:
        pass
    def main(self):
        driver = uc.Chrome(service=ChromeService(ChromeDriverManager().install()))
        ID = random.choice(no)
        try:
            print(ID)
            # Bolt().bolt_up(driver,ID)
            # Icq().icq_up(driver, ID)
            # Epal().epal_up(driver, ID)
            Yahoo().yahoo_up(driver, ID)
            time.sleep(30)
        except Exception as e:
            print(e)
            print(ID)
if __name__=='__main__':
    Main().main()
