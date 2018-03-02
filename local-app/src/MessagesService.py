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
            # if self.exists(message['id']) == True:
            #     continue
            #self.create_audio(message)
            self.messages.append(message)
        return

    # Method get_next_message. This method will find the message that
    # is next in line. It will return 0 if the messages_list is empty
    # or the next message
    def get_next_message(self):
        if len(self.messages) == 0:
            return 0
        next_message = self.messages[0]
        for el in range(1, len(self.messages)):
            next_message_in_minutes = self.time_to_minutes(next_message['hour'], next_message['minute'])
            curr_message_in_minutes = self.time_to_minutes(el['hour'], el['minute'])
            if (next_message_in_minutes > curr_message_in_minutes):
                next_message = el
        return next_message

    #############################################
    #############################################
    # Method remove_by_id. This method removed a dictionary entry, that
    # represents a message, from the list of entries by using the id
    # passed in as a parameter.
    def remove_by_id(self, id):
        for index, el in enumerate(self.messages):
            if el['id'] == id:
                self.messages.pop(index)
                return True
        return False
    #############################################
    #############################################
    #############################################

    # Method removes all the messages from the messages array.
    # This is called when all the messages have been cleared
    # from the server.
    def remove_all(self):
        self.messages = []

    # Method create_audio. This method is called when a new message is
    # received by the application. It utilizes the Downloader class to
    # download and create a new audio file.
    def create_audio(self, message):
        if not Downloader.check_path('../Audio/Messages/'):
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

    # Method that takes in current time in hours and minutes
    # and returns the time in just minutes
    @staticmethod
    def time_to_minutes(hour, minute):
        curr_hour = hour
        curr_minutes = minute
        minutes = curr_hour * 60
        minutes = minutes + curr_minutes
        return minutes
