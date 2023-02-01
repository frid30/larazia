from bs4 import BeautifulSoup
import requests
import json
import csv
import time
from pprint import pprint
from datetime import datetime


def divide_chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]


class LARAZIA:
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
            'startdate': f'{datetime.now().strftime("%Y-%m-%d")} 00:00:00',
            'enddate': f'{datetime.now().strftime("%Y-%m-%d")} 23:59:59',
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

    def larazia(self):
        L = []
        cookies = {
            'PHPSESSID': '32vtk8imrab5du57n2sdn93fe5',
        }
        data = json.loads(requests.post(
            'http://portal.exampletele.com/ajax_form_handler.php',
            cookies=cookies,
            headers=self.headers,
            data=self.data,
            verify=False,
        ).text.replace('\\t', '').replace('\\n', ''))['form']
        soup = BeautifulSoup(data, 'html.parser')
        td = list(divide_chunks(list(filter(lambda x: x not in ('', 'Terminate SMS'), [
            l.text for l in soup.findAll('td', attrs={'class': 'pad15T'})])), 4))
        S = set()
        for l in td:
            number, date, msg = l[0], l[2], l[3]
            data = {'number': number, 'date': date, 'msg': msg}
            L.append(data)
        return L

    def get_sms(self, number):
        L = self.larazia()
        while True:
            try:
                data = [data for data in L if data['number'] == number]
                print(data)
                date = max([rec['date'] for rec in data])
                if date:
                    rec = [rec for rec in data if rec['date'] == date][0]
                    return rec
            except:
                print('restart')
                time.sleep(2)


