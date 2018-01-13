import requests

#getUrl = 'http://127.0.0.1:8000/getMessages'

class MessagesService:

    # Constructor initializes list that will hold messages
    def __init__(self):
        self.messages = []

    # Method add_messages. This method receives a list of dictionary
    # entries, each corresponding to one message, as a parameter.
    # It iterates through the list and adds the messages to the
    # messages list
    def add_messages(self, message_list):
        for message in message_list:
            if self.exists(message['id']) == True:
                continue
            self.messages.append(message)
        return

    # Method remove_by_id. This method removed a dictionary entry, that
    # represents a message, from the list of entries by using the id
    # passed in as a parameter.
    def remove_by_id(self, id):
        return

    # Method exists. This method receives an ID as a parameter and
    # checks the messages list to see if it exists in it already.
    # It returns trues if the message is already is the list, or
    # false if it does not
    def exists(self, id):
        for message in self.messages:
            if message['id'] == id:
                return True
        return False
