
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
from configs.heetch import Heetch
import time
from database.data_mongo import Data
no = [{'_id': ObjectId('63e10d795fdac2fe6245be14'), 'phone_number': '447413097673', 'first_name': 'Wise', 
'name': 'Kimberly', 'password': '*_J&Z5RskQ', 'email': 'wise.kimberly2918@monmail.fr.nf'}, {'_id': ObjectId('63e10d7a5fdac2fe6245be15'), 'phone_number': '447412989377', 'first_name': 'Santiago', 'name': 'Jo', 'password': '!)ENR)4j7O', 'email': 'santiago.jo363@courriel.fr.nf'}, {'_id': ObjectId('63e10d7a5fdac2fe6245be16'), 'phone_number': '447413070926', 'first_name': 'Graham', 'name': 'Glenn', 'password': ')nYhOBNuO0', 'email': 'graham.glenn578@monmail.fr.nf'}, {'_id': ObjectId('63e10d7a5fdac2fe6245be17'), 'phone_number': '447412985739', 'first_name': 'Meyer', 'name': 'Ethan', 'password': 'bJD#9IdcJ(', 'email': 'meyer.ethan1679@hunnur.com'}, {'_id': ObjectId('63e10d7b5fdac2fe6245be18'), 'phone_number': '447412984610', 'first_name': 'Griffith', 'name': 'Mark', 'password': 'nAMpJ8Oak^', 'email': 'griffith.mark309@monmail.fr.nf'}, {'_id': ObjectId('63e10d7b5fdac2fe6245be19'), 'phone_number': '447413127602', 'first_name': 'Olson', 'name': 'Kirk', 'password': 'c4$xxIvo)u', 'email': 'olson.kirk2856@mynes.com'}, {'_id': ObjectId('63e10d7c5fdac2fe6245be1a'), 'phone_number': '447413130988', 'first_name': 'Smith', 'name': 'Melissa', 'password': '(50%DvL!UQ', 'email': 'smith.melissa2471@monmail.fr.nf'}, {'_id': ObjectId('63e10d7c5fdac2fe6245be1b'), 'phone_number': '447413091927', 'first_name': 'Mendez', 'name': 'Micheal', 'password': '9&0E7XkwT@', 'email': 'mendez.micheal1591@uefia.com'}, {'_id': ObjectId('63e10d7d5fdac2fe6245be1c'), 'phone_number': '447412993405', 'first_name': 'Smith', 'name': 'Benjamin', 'password': 'N9+1q6Dwr9', 'email': 'smith.benjamin2961@courriel.fr.nf'}, {'_id': ObjectId('63e10d7d5fdac2fe6245be1d'), 'phone_number': '447413131560', 'first_name': 'Brown', 'name': 'Tonya', 'password': 'G@N1wDfk2u', 'email': 'brown.tonya1112@hunnur.com'}, {'_id': ObjectId('63e10d7d5fdac2fe6245be1e'), 'phone_number': '447413110936', 'first_name': 'Adams', 'name': 'Holly', 'password': '#IP25Qma@m', 'email': 'adams.holly1024@monmail.fr.nf'}, {'_id': ObjectId('63e10d7e5fdac2fe6245be1f'), 'phone_number': '447412990710', 'first_name': 'Smith', 'name': 'Mr.', 'password': '&&779UFjhm', 'email': 'smith.mr.1757@hunnur.com'}, {'_id': ObjectId('63e10d7e5fdac2fe6245be20'), 'phone_number': '447413112677', 'first_name': 'Campbell', 'name': 'Jacob', 'password': '*7XCc&vi@h', 'email': 'campbell.jacob953@mynes.com'}, {'_id': ObjectId('63e10d7f5fdac2fe6245be21'), 'phone_number': '447413129261', 'first_name': 'Adrian', 'name': 'Christopher', 'password': '0^r3Lh4LCv', 'email': 'adrian.christopher473@monemail.fr.nf'}, {'_id': ObjectId('63e10d7f5fdac2fe6245be22'), 'phone_number': '447413123788', 'first_name': 'Raymond', 'name': 'Alexis', 'password': '(X3QPO*xqy', 'email': 'raymond.alexis1464@mynes.com'}]

import os
import shutil
import tempfile

import undetected_chromedriver as webdriver
proxies = ["89.191.226.156:8080:UKZVI6BE5:uNV56Uw6","77.220.193.125:8080:UKZVI6BE5:uNV56Uw6","213.108.2.143:8080:UKZVI6BE5:uNV56Uw6","45.148.232.77:8080:UKZVI6BE5:uNV56Uw6","193.203.10.86:8080:UKZVI6BE5:uNV56Uw6","193.203.8.230:8080:UKZVI6BE5:uNV56Uw6","212.119.45.13:8080:UKZVI6BE5:uNV56Uw6","212.119.46.109:8080:UKZVI6BE5:uNV56Uw6","93.177.119.75:8080:UKZVI6BE5:uNV56Uw6","45.80.105.72:8080:UKZVI6BE5:uNV56Uw6","193.203.11.156:8080:UKZVI6BE5:uNV56Uw6","83.142.53.132:8080:UKZVI6BE5:uNV56Uw6","89.191.226.169:8080:UKZVI6BE5:uNV56Uw6"]
class ProxyExtension:
    manifest_json = """
    {
        "version": "1.0.0",
        "manifest_version": 2,
        "name": "Chrome Proxy",
        "permissions": [
            "proxy",
            "tabs",
            "unlimitedStorage",
            "storage",
            "<all_urls>",
            "webRequest",
            "webRequestBlocking"
        ],
        "background": {"scripts": ["background.js"]},
        "minimum_chrome_version": "76.0.0"
    }
    """

    background_js = """
    var config = {
        mode: "fixed_servers",
        rules: {
            singleProxy: {
                scheme: "http",
                host: "%s",
                port: %d
            },
            bypassList: ["localhost"]
        }
    };

    chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

    function callbackFn(details) {
        return {
            authCredentials: {
                username: "%s",
                password: "%s"
            }
        };
    }

    chrome.webRequest.onAuthRequired.addListener(
        callbackFn,
        { urls: ["<all_urls>"] },
        ['blocking']
    );
    """

    def __init__(self, host, port, user, password):
        self._dir = os.path.normpath(tempfile.mkdtemp())

        manifest_file = os.path.join(self._dir, "manifest.json")
        with open(manifest_file, mode="w") as f:
            f.write(self.manifest_json)

        background_js = self.background_js % (host, port, user, password)
        background_file = os.path.join(self._dir, "background.js")
        with open(background_file, mode="w") as f:
            f.write(background_js)

    @property
    def directory(self):
        return self._dir

    def __del__(self):
        shutil.rmtree(self._dir)



counter = 0

class Main:
    def __init__(self) -> None:
        pass
    def main(self):
        counter = 0

        for ID in no:
            leg_proxy = proxies[counter].split(":")
            proxy = (leg_proxy[0],int(leg_proxy[1]), leg_proxy[2], leg_proxy[3])  # your proxy with auth, this one is obviously fake
            proxy_extension = ProxyExtension(*proxy)
            options = webdriver.ChromeOptions()
            options.add_argument(f"--load-extension={proxy_extension.directory}")
            driver = webdriver.Chrome(options=options)
            try:                        
                print(ID)
                Bolt().bolt_in(driver, ID)
                Icq().icq_in(driver, ID)
                Heetch().heetch_in(driver,ID)
                # #  Epal().epal_in(driver, ID)
                # #  Yahoo().yahoo_in(driver, ID)
                # #  Lyft().lyft_up(driver, ID)
                driver.quit()
                counter += 1
                # driver.get("https://www.airbnb.com")
                time.sleep(20)
            except Exception as e :
                driver.quit()
                print(ID)
                print(e)
if __name__ == '__main__':
    Main().main()

    