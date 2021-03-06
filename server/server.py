import requests
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = '' #Postgres url
db = SQLAlchemy(app)
import dbManager
CORS(app)

# This list is responsible in storing the Messages to be retrieved by the client side
# Format of each Message is:
#   {'body':'', 'day':'', 'hour':0,
#    'minute':0, 'time':'', id:0
#   }

# Routing Functions
@app.route('/')
def index():
    return 'This is the home page.'

@app.route('/log')
def log():
    return 'log page'


@app.route('/addMessage', methods=['POST'])
def addMessage():
    if request.method == 'POST':
        json_dict = request.get_json()
        id = dbManager.add_entry(json_dict)
        return 'id = {}'.format(id)
    else:
        return 'There was an error.'

# Method returns list of messages in json dictionary or nothing if list is empty
@app.route('/getMessages', methods=['GET'])
def getMessages():
    if request.method == 'GET':
        message_list = dbManager.get_all_entries()
        if message_list == None:
            return 'There was an error getting all entries.'
        return jsonify(message_list)
    else:
        return 'There was an error.'

# Method that returns a dictionary with Message data
# It takes in an id as a parameter
@app.route('/getMessageById', methods=['GET'])
def getMessageById():
    if request.method == 'GET':
        id = request.args.get('id', type=int)
        # For now retrieve with id 1
        json_dict = dbManager.get_entry_by_id(id)
        if json_dict == None:
            return 'The id does not exist.'
        return jsonify(json_dict)
    else:
        return 'There was an error.'

# Method that deletes a message from the database by using its id
@app.route('/deleteMessageById', methods=['GET'])
def deleteMessageById():
    if request.method == 'GET':
        id = request.args.get('id', type=int)
        status = dbManager.delete_by_id(id)
        console.log('Status from deleteMessageById: ', status)
        return 'Message deleted called.'

if __name__ == '__main__':
    app.run(debug=True)
