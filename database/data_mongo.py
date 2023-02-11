import sys,os,time,random,requests,json,csv
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
        self.proxies = [proxies[0] for proxies in csv.reader(open('proxies.txt','r'))]

    def refill_db(self):
        L = []
        proxies = self.proxies
        f = open('numbers.txt', 'r')
        for number in f:
            first_name = Faker().name().split(' ')[0]
            last_name = Faker().name().split(' ')[1]
            data = {'number': int(number),
                    'first_name': first_name,
                    'name': last_name,
                    'password': Faker().password(),
                    'email': f"{first_name.lower()}.{last_name.lower()}{random.randint(100,3000)}{random.choice(liste_domain)}",
                    "proxy_ID":random.choice(proxies)}
            #data |= {s.split('.')[0]: 0 for s in os.listdir('configs')}
            print(data)
            #r = requests.get('https://apidatabase.herokuapp.com/insert',data=data)

    def IDs(self):
        r = json.loads(requests.get(
            'https://apidatabase.herokuapp.com/get').text)
        return r
L = list(IDs.find())
#for i in range(len(L)):
#    IDs.update_one({'_id':L[i]['_id']},{'$set':{'proxy':Data().proxies[i]}})
for i in IDs.find():
    print(i)