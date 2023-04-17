import os
import shutil,time
import tempfile
from selenium.webdriver.common.keys import Keys

from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
#A NOUS
from selenium.webdriver.common.action_chains import ActionChains

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

def click_on(xpath):
        try:
            driver.implicitly_wait(6)
            driver.find_element(By.XPATH, xpath).click()
            time.sleep(1)
        except Exception as e: 
            print(xpath,e)
def fill(xpath, value):
        try:
            driver.implicitly_wait(6)
            searchButton = driver.find_element(By.XPATH, xpath)
            searchButton.send_keys(value)
            time.sleep(1)
        except Exception as e: 
            print(xpath,e)
def infos():
    data_infos= {"name" :"/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div/div[1]/div[1]/h1",
    "rating_star" :"/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div/div[1]/div[2]/div/div[1]/div[2]/span[1]/span[1]",
    "number ":"/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[9]/div[9]/button/div[1]/div[3]/div[1]",
    "adresse" : "/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[9]/div[3]/button/div[1]/div[3]/div[1]"}
    data_scrapped ={}
    for info,xpath in data_infos.items():
        try:
            info_scrapped = driver.find_element(By.XPATH,xpath).text
            data_scrapped[info] = info_scrapped
        except:
            pass                     
    return data_scrapped
def collect_marchand(url):
    driver.get(url)
    click_on("/html/body/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/div[1]/form[2]/div/div/button/span")
    driver.implicitly_wait(30)
    print(infos())
    return
if __name__ == "__main__":
    # proxy = ("residential.pingproxies.com", 7777, "customer-330b0f81CJQKi-cc-GB-sessid-XA51b6KG", "Pp1l4hpvzh")  # your proxy with auth, this one is obviously fake
    # proxy_extension = ProxyExtension(*proxy)


    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=chrome_options)
    collect_marchand("https://www.google.com/maps/place/Restaurant+K%C3%BAk%C3%BA/data=!4m7!3m6!1s0x47e66f455ed296a5:0xac6247607abbf705!8m2!3d48.872725!4d2.3156315!16s%2Fg%2F11swpgmyb6!19sChIJpZbSXkVv5kcRBfe7emBHYqw?authuser=0&hl=fr&rclk=1")