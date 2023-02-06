from pymongo import MongoClient
from faker import Faker
from Sms import Larazia
import random
client = MongoClient(
    'mongodb+srv://Walter_McLovin:iammclovin777@cluster0.d7cbbym.mongodb.net/test')
DB = client['ACCOUNTS']
IDs = DB['IDs']
liste_domain = ["@uefia.com","@mynes.com","@hunnur.com","@monemail.fr.nf","@monmail.fr.nf","@courriel.fr.nf"]

def get_numbers():
    liste = []
    for id in IDs.find():
        liste.append(id["phone_number"])
    return liste

def refill_db():
    numbers_already_registered = get_numbers()
    for number in Larazia().numbers:
       if number not in numbers_already_registered:
        name , firstname = Faker().name().split(' ')[0],Faker().name().split(' ')[1]
        data = {'phone_number' : number,
                'first_name' :firstname ,
                'name': name,
                'password' : Faker().password(),
                'email' : f"{firstname.lower()}.{name.lower()}{random.randint(100,3000)}{random.choice(liste_domain)}"}
        print(data)

        IDs.insert_one(data)
refill_db()
