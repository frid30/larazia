import sys
import os
import time
import random
import requests
import json
from bson import ObjectId
p_1 = (os.path.dirname(os.path.abspath(__file__)))
p_2 = os.path.dirname(p_1)
sys.path.append(p_2)
from Sms import Larazia
from pprint import pprint
from pymongo import MongoClient
from faker import Faker


client = MongoClient(
    'mongodb+srv://Walter_McLovin:iammclovin777@cluster0.d7cbbym.mongodb.net/test')
DB = client['ACCOUNTS']
IDs = DB['IDs']
liste_domain = ["@uefia.com", "@mynes.com", "@hunnur.com",
                "@monemail.fr.nf", "@monmail.fr.nf", "@courriel.fr.nf"]


class Data():
    def __init__(self) -> None:
        pass

    def refill_db(self):
        L = []
        f = open('numbers.txt', 'r')
        for number in f:
            first_name = Faker().name().split(' ')[0]
            last_name = Faker().name().split(' ')[1]
            data = {'number': int(number),
                    'first_name': first_name,
                    'name': last_name,
                    'password': Faker().password(),
                    'email': f"{first_name.lower()}.{last_name.lower()}{random.randint(100,3000)}{random.choice(liste_domain)}"}
            #data |= {s.split('.')[0]: 0 for s in os.listdir('configs')}
            print(data)
            #r = requests.get('https://apidatabase.herokuapp.com/insert',data=data)

    def IDs(self):
        r = json.loads(requests.get(
            'https://apidatabase.herokuapp.com/get').text)
        return r

liste = []
liste20 = []
for x in [  {'_id': ObjectId('63e10d7c5fdac2fe6245be1b'), 'phone_number': '447413091927', 'first_name': 'Mendez', 'name': 'Micheal', 'password': '9&0E7XkwT@', 'email': 'mendez.micheal1591@uefia.com'}, {'_id': ObjectId('63e10d7d5fdac2fe6245be1c'), 'phone_number': '447412993405', 'first_name': 'Smith', 'name': 'Benjamin', 'password': 'N9+1q6Dwr9', 'email': 'smith.benjamin2961@courriel.fr.nf'}, {'_id': ObjectId('63e10d7d5fdac2fe6245be1d'), 'phone_number': '447413131560', 'first_name': 'Brown', 'name': 'Tonya', 'password': 'G@N1wDfk2u', 'email': 'brown.tonya1112@hunnur.com'}, {'_id': ObjectId('63e10d7d5fdac2fe6245be1e'), 'phone_number': '447413110936', 'first_name': 'Adams', 'name': 'Holly', 'password': '#IP25Qma@m', 'email': 'adams.holly1024@monmail.fr.nf'}, {'_id': ObjectId('63e10d7e5fdac2fe6245be1f'), 'phone_number': '447412990710', 'first_name': 'Smith', 'name': 'Mr.', 'password': '&&779UFjhm', 'email': 'smith.mr.1757@hunnur.com'}, {'_id': ObjectId('63e10d7e5fdac2fe6245be20'), 'phone_number': '447413112677', 'first_name': 'Campbell', 'name': 'Jacob', 'password': '7XCc&vi@h', 'email': 'campbell.jacob953@mynes.com'}, {'_id': ObjectId('63e10d7f5fdac2fe6245be21'), 'phone_number': '447413129261', 'first_name': 'Adrian', 'name': 'Christopher', 'password': '0^r3Lh4LCv', 'email': 'adrian.christopher473@monemail.fr.nf'}, {'_id': ObjectId('63e10d7f5fdac2fe6245be22'), 'phone_number': '447413123788', 'first_name': 'Raymond', 'name': 'Alexis', 'password': '(X3QPOxqy', 'email': 'raymond.alexis1464@mynes.com'}]:
    liste20.append(x["phone_number"])
print(liste20)
for x in Data().IDs():
    if x["phone_number"] not in liste20:
        liste.append(x)
print(liste)