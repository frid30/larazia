from pymongo import MongoClient
from Sms import Larazia
client = MongoClient(
    'mongodb+srv://Walter_McLovin:iammclovin777@cluster0.dejj1c0.mongodb.net/test')
DB=client['PHONE_NUMBERS']

for number in Larazia().numbers:
    DB['phone_numbers'].insert_one({'number' : number, 'services':{}})