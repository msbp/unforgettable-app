import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# This list is responsible in storing the Messages to be retrieved by the client side
# Format of each Message is:
#   {'body':'', 'day':'', 'hour':0,
#    'minute':0, 'time':'', id:0
#   }
message_list = []
currId = 0

# Routing Functions
@app.route('/')
def index():
    return 'This is the home page.'

@app.route('/addMessage', methods=['POST'])
def addMessage():
    if request.method == 'POST':
        json_dict = request.get_json()
        #print('Heres the dictionary object:', json_dict)
        message_list.append(json_dict)
        print(message_list)
        global currId
        currId = currId + 1
        if (currId > 1000):
            currId = 0
        return jsonify(json_dict)
    else:
        return 'There was an error.'

# Method returns list of messages in json or nothing if list is empty
@app.route('/getMessages', methods=['GET'])
def getMessages():
    if request.method == 'GET':
        if len(message_list) > 0:
            return jsonify(message_list)
        else:
            return

# Method returns an ID to be used by the mobile application to create
# a message to be sent back to the server
@app.route('/getId', methods=['GET'])
def getId():
    if request.method == 'GET':
        print('ID passed: ', currId)
        return jsonify(currId)

if __name__ == '__main__':
    app.run
