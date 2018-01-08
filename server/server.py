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

@app.route('/sample', methods=['POST'])
def sample():
    if request.method == 'POST':
        json_dict = request.get_json()
        #print('Heres the dictionary object:', json_dict)
        message_list.append(json_dict)
        print(message_list)
        return jsonify(json_dict)
    else:
        return 'There was an error.'


if __name__ == '__main__':
    app.run
