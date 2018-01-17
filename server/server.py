import requests
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/template1'
db = SQLAlchemy(app)
import dbManager

# This list is responsible in storing the Messages to be retrieved by the client side
# Format of each Message is:
#   {'body':'', 'day':'', 'hour':0,
#    'minute':0, 'time':'', id:0
#   }


# Routing Functions
@app.route('/')
def index():
    return 'This is the home page.'

@app.route('/addMessage', methods=['POST'])
def addMessage():
    if request.method == 'POST':
        json_dict = request.get_json()
        id = dbManager.add_entry(json_dict)
        return 'id = {}'.format(id)
    else:
        return 'There was an error.'

# Method returns list of messages in json or nothing if list is empty
@app.route('/getMessages', methods=['GET'])
def getMessages():
    if request.method == 'GET':
        # For now retrieve with id 1
        json_dict = dbManager.get_entry(1)
        if json_dict == None:
            return 'There was an error.'
        return jsonify(json_dict)
    else:
        return 'There was an error.'

# Method returns an ID to be used by the mobile application to create
# a message to be sent back to the server
# @app.route('/getId', methods=['GET'])
# def getId():
#     if request.method == 'GET':
#         print('ID passed: ', currId)
#         return jsonify(currId)

if __name__ == '__main__':
    app.run
