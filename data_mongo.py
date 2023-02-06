from pymongo import MongoClient
from faker import Faker
from Sms import Larazia
import random
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

    def get_numbers(self):
        liste = []
        for id in IDs.find():
            liste.append(id["phone_number"])
        return liste

    def refill_db(self):
        L = []
        numbers_already_registered = self.get_numbers()
        with open('IDs.txt', 'w') as f:
            for number in Larazia().numbers:
                name, firstname = Faker().name().split(
                    ' ')[0], Faker().name().split(' ')[1]
                data = {'phone_number': number,
                        'first_name': firstname,
                        'name': name,
                        'password': Faker().password(),
                        'email': f"{firstname.lower()}.{name.lower()}{random.randint(100,3000)}{random.choice(liste_domain)}"}
                f.write(str(data)+'\n')

    def ID s(self):
        self.refill_db()
        L = []
        with open('IDs.txt', 'r') as f:
            f = f.read()
            L = f.split('\n')
            return L
