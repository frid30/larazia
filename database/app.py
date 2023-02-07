from flask import Flask, request, jsonify
from pymongo import MongoClient
import json,requests
client = MongoClient('mongodb+srv://Walter_McLovin:iammclovin777@cluster0.d7cbbym.mongodb.net/test')
DB = client['ACCOUNTS']
IDs = DB['IDs']
app = Flask(__name__)
@app.route('/insert',methods=['GET'])
def insert():
    data = json.loads(request.data)
    IDs.insert_one(data)
    return jsonify({'message' : 'document successfully inserted'})
@app.route('/get', methods=['GET'])
def get():
        return jsonify(list(IDs.find()))
@app.route('/update', methods=['GET'])
def put():
    data = json.loads(request.data)
    number,service = data['number'],data['service']
    ID = IDs.find_one({'number':number})
    IDs.update_one({'number': number},{'$set': {service: ID['service']+1}})


