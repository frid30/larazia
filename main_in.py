
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
from database.data_mongo import Data
no = [{'_id': ObjectId('63e10d775fdac2fe6245be0e'), 'phone_number': '447413124565', 'first_name': 'Ashley', 'name': 'Jason', 'password': '_Q206VaoqA', 'email': 'ashley.jason1694@courriel.fr.nf'}, {'_id': ObjectId('63e10d775fdac2fe6245be0f'), 'phone_number': '447412989223', 'first_name': 'Andrade', 'name': 'Raymond', 'password': '&6ch1bLBz$', 'email': 'andrade.raymond784@mynes.com'}, {'_id': ObjectId('63e10d775fdac2fe6245be10'), 'phone_number': '447413127992', 'first_name': 'Salazar', 'name': 'Margaret', 'password': 'kpT1hDoy&I', 'email': 'salazar.margaret1662@monemail.fr.nf'}, {'_id': ObjectId('63e10d785fdac2fe6245be11'), 'phone_number': '447413107409', 'first_name': 'Grimes', 'name': 'Cindy', 'password': '@85ALf4BO1', 'email': 'grimes.cindy1795@monemail.fr.nf'}, {'_id': ObjectId('63e10d785fdac2fe6245be12'), 'phone_number': '447413083728', 'first_name': 'Ross', 'name': 'Troy', 'password': 'X&d4TfeuMW', 'email': 'ross.troy2442@hunnur.com'}, {'_id': ObjectId('63e10d795fdac2fe6245be13'), 'phone_number': '447412992725', 'first_name': 'Bauer', 'name': 'Douglas', 'password': '*C4Jd+uq*5', 'email': 'bauer.douglas2118@hunnur.com'}, {'_id': ObjectId('63e10d795fdac2fe6245be14'), 'phone_number': '447413097673', 'first_name': 'Wise', 
'name': 'Kimberly', 'password': '*_J&Z5RskQ', 'email': 'wise.kimberly2918@monmail.fr.nf'}, {'_id': ObjectId('63e10d7a5fdac2fe6245be15'), 'phone_number': '447412989377', 'first_name': 'Santiago', 'name': 'Jo', 'password': '!)ENR)4j7O', 'email': 'santiago.jo363@courriel.fr.nf'}, {'_id': ObjectId('63e10d7a5fdac2fe6245be16'), 'phone_number': '447413070926', 'first_name': 'Graham', 'name': 'Glenn', 'password': ')nYhOBNuO0', 'email': 'graham.glenn578@monmail.fr.nf'}, {'_id': ObjectId('63e10d7a5fdac2fe6245be17'), 'phone_number': '447412985739', 'first_name': 'Meyer', 'name': 'Ethan', 'password': 'bJD#9IdcJ(', 'email': 'meyer.ethan1679@hunnur.com'}, {'_id': ObjectId('63e10d7b5fdac2fe6245be18'), 'phone_number': '447412984610', 'first_name': 'Griffith', 'name': 'Mark', 'password': 'nAMpJ8Oak^', 'email': 'griffith.mark309@monmail.fr.nf'}, {'_id': ObjectId('63e10d7b5fdac2fe6245be19'), 'phone_number': '447413127602', 'first_name': 'Olson', 'name': 'Kirk', 'password': 'c4$xxIvo)u', 'email': 'olson.kirk2856@mynes.com'}, {'_id': ObjectId('63e10d7c5fdac2fe6245be1a'), 'phone_number': '447413130988', 'first_name': 'Smith', 'name': 'Melissa', 'password': '(50%DvL!UQ', 'email': 'smith.melissa2471@monmail.fr.nf'}, {'_id': ObjectId('63e10d7c5fdac2fe6245be1b'), 'phone_number': '447413091927', 'first_name': 'Mendez', 'name': 'Micheal', 'password': '9&0E7XkwT@', 'email': 'mendez.micheal1591@uefia.com'}, {'_id': ObjectId('63e10d7d5fdac2fe6245be1c'), 'phone_number': '447412993405', 'first_name': 'Smith', 'name': 'Benjamin', 'password': 'N9+1q6Dwr9', 'email': 'smith.benjamin2961@courriel.fr.nf'}, {'_id': ObjectId('63e10d7d5fdac2fe6245be1d'), 'phone_number': '447413131560', 'first_name': 'Brown', 'name': 'Tonya', 'password': 'G@N1wDfk2u', 'email': 'brown.tonya1112@hunnur.com'}, {'_id': ObjectId('63e10d7d5fdac2fe6245be1e'), 'phone_number': '447413110936', 'first_name': 'Adams', 'name': 'Holly', 'password': '#IP25Qma@m', 'email': 'adams.holly1024@monmail.fr.nf'}, {'_id': ObjectId('63e10d7e5fdac2fe6245be1f'), 'phone_number': '447412990710', 'first_name': 'Smith', 'name': 'Mr.', 'password': '&&779UFjhm', 'email': 'smith.mr.1757@hunnur.com'}, {'_id': ObjectId('63e10d7e5fdac2fe6245be20'), 'phone_number': '447413112677', 'first_name': 'Campbell', 'name': 'Jacob', 'password': '*7XCc&vi@h', 'email': 'campbell.jacob953@mynes.com'}, {'_id': ObjectId('63e10d7f5fdac2fe6245be21'), 'phone_number': '447413129261', 'first_name': 'Adrian', 'name': 'Christopher', 'password': '0^r3Lh4LCv', 'email': 'adrian.christopher473@monemail.fr.nf'}, {'_id': ObjectId('63e10d7f5fdac2fe6245be22'), 'phone_number': '447413123788', 'first_name': 'Raymond', 'name': 'Alexis', 'password': '(X3QPO*xqy', 'email': 'raymond.alexis1464@mynes.com'}]

import os
import shutil
import tempfile

import undetected_chromedriver as webdriver
proxies = ["residential.pingproxies.com:7777:customer-330b0f81CJQKi-sessid-Ldbcg9D0U:Pp1l4hpvzh","residential.pingproxies.com:7777:customer-330b0f81CJQKi-sessid-TVzJeBlwO:Pp1l4hpvzh","residential.pingproxies.com:7777:customer-330b0f81CJQKi-sessid-6N5SFfaEm:Pp1l4hpvzh","residential.pingproxies.com:7777:customer-330b0f81CJQKi-sessid-ZjHx1ZPuh:Pp1l4hpvzh","residential.pingproxies.com:7777:customer-330b0f81CJQKi-sessid-NjhaHU1qP:Pp1l4hpvzh","residential.pingproxies.com:7777:customer-330b0f81CJQKi-sessid-gs06gsx9f:Pp1l4hpvzh","residential.pingproxies.com:7777:customer-330b0f81CJQKi-sessid-0enVokFto:Pp1l4hpvzh","residential.pingproxies.com:7777:customer-330b0f81CJQKi-sessid-fEhKBwBNu:Pp1l4hpvzh","residential.pingproxies.com:7777:customer-330b0f81CJQKi-sessid-uRzA9hMZO:Pp1l4hpvzh","residential.pingproxies.com:7777:customer-330b0f81CJQKi-sessid-oZPXovJ4T:Pp1l4hpvzh","residential.pingproxies.com:7777:customer-330b0f81CJQKi-sessid-n5OtyrtcK:Pp1l4hpvzh","residential.pingproxies.com:7777:customer-330b0f81CJQKi-sessid-IBK1LNWRe:Pp1l4hpvzh","residential.pingproxies.com:7777:customer-330b0f81CJQKi-sessid-ivfMYuLza:Pp1l4hpvzh","residential.pingproxies.com:7777:customer-330b0f81CJQKi-sessid-I6pR9PzEH:Pp1l4hpvzh","residential.pingproxies.com:7777:customer-330b0f81CJQKi-sessid-oeYo7tTHM:Pp1l4hpvzh","residential.pingproxies.com:7777:customer-330b0f81CJQKi-sessid-GobAo71Yz:Pp1l4hpvzh","residential.pingproxies.com:7777:customer-330b0f81CJQKi-sessid-dQvkN91Za:Pp1l4hpvzh","residential.pingproxies.com:7777:customer-330b0f81CJQKi-sessid-exnwFRV5X:Pp1l4hpvzh","residential.pingproxies.com:7777:customer-330b0f81CJQKi-sessid-JL06HR7H7:Pp1l4hpvzh","residential.pingproxies.com:7777:customer-330b0f81CJQKi-sessid-M3WVGkey9:Pp1l4hpvzh","residential.pingproxies.com:7777:customer-330b0f81CJQKi-sessid-tWu6AKO6s:Pp1l4hpvzh","residential.pingproxies.com:7777:customer-330b0f81CJQKi-sessid-oZwOuKjkm:Pp1l4hpvzh","residential.pingproxies.com:7777:customer-330b0f81CJQKi-sessid-W08vhrrZP:Pp1l4hpvzh","residential.pingproxies.com:7777:customer-330b0f81CJQKi-sessid-8vaO3PwkM:Pp1l4hpvzh","residential.pingproxies.com:7777:customer-330b0f81CJQKi-sessid-Ap8t9krHi:Pp1l4hpvzh","residential.pingproxies.com:7777:customer-330b0f81CJQKi-sessid-g7zOesGli:Pp1l4hpvzh","residential.pingproxies.com:7777:customer-330b0f81CJQKi-sessid-TiMvfHhQU:Pp1l4hpvzh","residential.pingproxies.com:7777:customer-330b0f81CJQKi-sessid-rSItEbBnA:Pp1l4hpvzh","residential.pingproxies.com:7777:customer-330b0f81CJQKi-sessid-RIm9tpuHZ:Pp1l4hpvzh","residential.pingproxies.com:7777:customer-330b0f81CJQKi-sessid-UFgVUYmgI:Pp1l4hpvzh","residential.pingproxies.com:7777:customer-330b0f81CJQKi-sessid-Q24DDEqfV:Pp1l4hpvzh"]

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




class Main:
    def __init__(self) -> None:
        pass
    def main(self):
        counter = 0
        for ID in no:
            try:
                leg_proxy = proxies[counter].split(":")
                proxy = (leg_proxy[0],leg_proxy[1], leg_proxy[2], leg_proxy[3])  # your proxy with auth, this one is obviously fake
                proxy_extension = ProxyExtension(*proxy)

                options = webdriver.ChromeOptions()
                options.add_argument(f"--load-extension={proxy_extension.directory}")
                driver = webdriver.Chrome(options=options)



                print(ID)
                Bolt().bolt_in(driver, ID)
                Icq().icq_in(driver, ID)
                Heetch().heetch_in(driver,ID)
                # #  Epal().epal_in(driver, ID)
                # #  Yahoo().yahoo_in(driver, ID)
                # #  Lyft().lyft_up(driver, ID)

                driver.quit()
                counter += 1
            except Exception as e :
                driver.quit()
                print(ID)
                print(e)
if __name__ == '__main__':
    Main().main()