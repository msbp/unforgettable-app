import requests

getUrl = 'http://127.0.0.1:8000/getMessages'

class MessagesList:

    # Constructor initializes list that will hold messages
    def __init__(self):
        messages = []

    # Method add_messages. This method receives a list of dictionary
    # entries, each corresponding to one message, as a parameter.
    # It iterates through the list and adds the messages to the
    # messages list
    def add_messages(self, messages):
        global getUrl
        r = requests.get(getUrl)
        lst = r.json()

        for each in lst:
            message = {}
        return

    # Method exists. This method receives an ID as a parameter and
    # checks the messages list to see if it exists in it already.
    # It returns trues if the message is already is the list, or
    # false if it does not
    def exists(self, id):
        return False
