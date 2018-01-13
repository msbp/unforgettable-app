import requests
import os
from Downloader import Downloader

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
            self.create_audio(message)
            self.messages.append(message)
        return

    # Method remove_by_id. This method removed a dictionary entry, that
    # represents a message, from the list of entries by using the id
    # passed in as a parameter.
    def remove_by_id(self, id):
        return

    # Method create_audio. This method is called when a new message is
    # received by the application. It utilizes the Downloader class to
    # download and create a new audio file.
    def create_audio(self, message):
        if not check_path('../Audio/Messages/'):
            os.makedirs('../Audio/Messages')
        fname = str(message['id'])
        Downloader.download_audio(message['body'])
        Downloader.create_audio('../Audio/Messages/' + fname, Downloader.speech['AudioStream'].read())
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
