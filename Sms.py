from bs4 import BeautifulSoup
import requests
import json
import csv
import time
from pprint import pprint
from datetime import datetime, timedelta
from faker import Faker
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService

from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


class Larazia:
    def __init__(self) -> None:
        self.data = {
            'sub': 'reporting',
            'subpage': 'reporting',
            'page': 'reports',
            'detailval': '2',
            'pageview': 'sms',
            'pageviewcnt': '50',
            'pagesearch': '',
            'pageorder': 'cliasc',
            'pageno': '1',
            'noclient': 'all',
            'nobillgroup': 'all',
            'startdate': datetime.now().strftime("%Y-%m-%d 00:00:00"),
            'enddate': datetime.now().strftime("%Y-%m-%d 23:59:59"),
            'reportview': 'summary',
            'search_option': '1',
            'sitetoken': '',
            'action': 'get',
        }
        self.headers = {
            'Accept': 'application/json, text/javascript, /; q=0.01',
            'Accept-Language': 'fr,fr-FR;q=0.9,en-US;q=0.8,en;q=0.7',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # 'Cookie': 'PHPSESSID=3aadshi34ge5hgovaldgkm47s0',
            'Origin': 'http://portal.exampletele.com/',
            'Referer': 'http://portal.exampletele.com/index.php?page=reports&sub=reporting&action=sms',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
        }
        self.numbers = [number[0]
                        for number in csv.reader(open('numbers.txt', 'r'))]

    def divide_chunks(self, l, n):
        for i in range(0, len(l), n):
            yield l[i:i + n]

    def larazia(self):
        L = []
        cookies = {
            'PHPSESSID': '5puq38mjvdc3pkaa4ljkicfvf4',
        }
        while True:
            try:
                data = json.loads(requests.post(
                    'http://portal.exampletele.com/ajax_form_handler.php',
                    cookies=cookies,
                    headers=self.headers,
                    data=self.data,
                    verify=False,
                ).text.replace('\\t', '').replace('\\n', ''))['form']
                soup = BeautifulSoup(data, 'html.parser')
                td = list(self.divide_chunks(list(filter(lambda x: x not in ('', 'Terminate SMS'), [
                    l.text for l in soup.findAll('td', attrs={'class': 'pad15T'})])), 4))
                S = set()
                for l in td:
                    number, date, msg = l[0], l[2], l[3]
                    data = {'number': number, 'date': date, 'msg': msg}
                    L.append(data)
                return L
            except Exception as e:
                print(e)
                time.sleep(3)

    def get_sms(self, number):
        while True:
            try:
                L = self.larazia()
                rec = [data for data in L if data['number']]
                date = [data['date'] for data in rec]
                Rec = dict(zip(date,rec))
                rec = Rec[max(date)]
                print(rec)
                return rec
            except Exception as e:
                print(e)
                print('restart')
                time.sleep(2)


class Feed:
    def __init__(self) -> None:
        pass

    def name(self):
        return Faker().first_name()

    def password(self):
        return Faker().password()

    def firstname(self):
        return Faker().first_name()


class Email:
    def __init__(self) -> None:
        pass

    def get_email(self):
        return


if __name__ == '__main__':
    Larazia().get_sms('447412984610')

# class Navigate():
#    def click_on(self, xpath):
#        try:
#            driver.implicitly_wait(6)
#            driver.find_element(By.XPATH, xpath).click()
#            time.sleep(1)
#        except:
#            pass
#
#    def fill(self, xpath, value):
#        try:
#            driver.implicitly_wait(6)
#            searchButton = driver.find_element(By.XPATH, xpath)
#            searchButton.send_keys(value)
#            time.sleep(1)
#        except:
#            pass
