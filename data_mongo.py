from pymongo import MongoClient
from faker import Faker
from Sms import Larazia
client = MongoClient(
    'mongodb+srv://Walter_McLovin:iammclovin777@cluster0.d7cbbym.mongodb.net/test')
DB = client['ACCOUNTS']
IDs = DB['IDs']
for number in Larazia().numbers:
    data = {'phone_number': number,
            'first_name': Faker().name().split(' ')[0],
            'name': Faker().name().split(' ')[1],
            'password': Faker().password(),
            'email': Faker().email()}
    print(data)
    IDs.insert_one(data)
