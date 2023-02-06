#SELENIUM
from Sms import Larazia, Feed
import undetected_chromedriver as uc
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
#A NOUS
import sys
import os
import time
p_1 = (os.path.dirname(os.path.abspath(__file__)))
p_2 = os.path.dirname(p_1)
sys.path.append(p_2)
class Bolt_in():
    def __init__(self) -> None:
        pass
    def get_code(msg):
        code = msg.split(' ')[0]
        return code
    
name = Feed().name()
if __name__ == '__main__':
    