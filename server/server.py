import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# This list is responsible in storing the Messages to be retrieved by the client side
# Format of each Message is:
#   {'body':'', 'day':'', 'hour':0,
#    'minute':0, 'time':''
#   }
message_list = []

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


if __name__ == '__main__':
    app.run
