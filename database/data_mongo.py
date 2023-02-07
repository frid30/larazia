from pymongo import MongoClient
from faker import Faker  
import sys,os,time,random,requests
p_1 = (os.path.dirname(os.path.abspath(__file__)))
p_2 = os.path.dirname(p_1)
sys.path.append(p_2)
from Sms import Larazia
import json
from pprint import pprint
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
        f = open('numbers.txt','r')
        for number in f:
            first_name = Faker().name().split(' ')[0]
            last_name = Faker().name().split(' ')[1]
            data = {'number': int(number),
                    'first_name': first_name,
                    'name': last_name,
                    'password': Faker().password(),
                    'email': f"{first_name.lower()}.{last_name.lower()}{random.randint(100,3000)}{random.choice(liste_domain)}"}
            r = requests.get('https://apidatabase.herokuapp.com/insert',data=data)
    #f.write(str(data)+'\n')

    def IDs(self):
        self.refill_db()
        L = []
        with open('IDs.txt', 'r') as f:
            f = f.read()
            L = f.split('\n')
            for x in L:
                print(self.str_to_dict(x))


Data().refill_db()
