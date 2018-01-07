import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return 'This is the home page.'

@app.route('/sample', methods=['POST'])
def sample():
    if request.method == 'POST':
        json_dict = request.get_json()
        print('Heres the dictionary object:')
        print(json_dict)
        return jsonify(json_dict)
    else:
        return 'There was an error.'


if __name__ == '__main__':
    app.run
