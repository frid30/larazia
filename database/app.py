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
    R=[]
    for ID in IDs.find():
        del ID['_id']
        R.append(ID)
    return jsonify(R)

    
@app.route('/update', methods=['GET'])
def put():
    data = json.loads(request.data)
    number,service = data['number'],data['service']
    ID = IDs.find_one({'number':number})
    IDs.update_one({'number': number},{'$set': {service: ID['service']+1}})


if __name__=='__main__':
    app.run(host="0.0.0.0", debug=False, port=5000)
