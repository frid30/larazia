# import module
import time
import undetected_chromedriver as uc
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

if __name__=='__main__':

        # Create object
    driver = uc.Chrome(service=ChromeService(ChromeDriverManager().install()))

    # Assign URL
    url = "https://www.geeksforgeeks.org/"

    # New Url
    new_url = "https://www.facebook.com/"

    # Opening first url
    driver.get(url)

    # Open a new window
    driver.execute_script("window.open('');")
    print('opened')
    time.sleep(10)
    # Switch to the new window and open new URL
    driver.switch_to.window(driver.window_handles[1])
    driver.get(new_url)
