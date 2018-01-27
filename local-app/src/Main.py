import boto3
import os
import time
import datetime
import requests
from pygame import mixer
from Downloader import Downloader
from Messages import Messages
from MessagesService import MessagesService

get_url = 'https://unforgettable.herokuapp.com/getMessages'

class Main:
    # Initialize audio player
    mixer.init()

    # Creating Messages list manager
    messages_service = MessagesService()

    ####################################################
    # Methods responsible in calling play_audio method #
    ####################################################
    # Method says greetings. 3 Options: Morning, Afternoon, Night
    # AfternoonBeing and AfternoonEnd determine when to switch greetings
    # time is an array in format (HOUR, MINUTE)
    @staticmethod
    def say_greetings():
        curret_time = Main.get_time()
        if current_time[0] < Messages.AfternoonBegin:
            play_audio("Greetings/Morning")
        elif current_time[0] < Messages.AfternoonEnd:
            play_audio("Greetings/Afternoon")
        else:
            play_audio("Greetings/Night")
    # Method says meal warnings. 2 Options: Lunch and Dinner
    # Lunch[0] holds time of lunch and Dinner[0] holds time of dinner
    # time is an array in format (HOUR, MINUTE)
    @staticmethod
    def say_meal_warning(time):
        if time[0] <= Messages.Lunch[0]:
            play_audio("Meals/Lunch")
        elif time[0] <= Messages.Dinner[0]:
            play_audio("Meals/Dinner")
    # Method says the current day of the week
    # Monday = 0 and Sunday = 6
    # day holds the index
    @staticmethod
    def say_weekday(day):
        play_audio("/Days/" + Message.days[0])
        return

    # Method obtains current day of the week from system
    # Returns number of the weekday (Monday = 0 ... Sunday = 6)
    @staticmethod
    def get_weekday():
        return datetime.datetime.today().weekday()

    # Method obtains current time from system
    # Returns (HOUR, MINUTE)
    @staticmethod
    def get_time():
        time_tuple = time.localtime(time.time())
        return (time_tuple[3], time_tuple[4])

    # Method obtains list of messages from server. This is a
    # helper method.
    # Returns a dictionary list with messages
    @staticmethod
    def get_messages():
        global get_url
        r = requests.get(get_url)
        return r.json()

    # Method updates the list of messages in the MessagesList
    # object. This method should be called when the application
    # needs/wants to update the message list
    @staticmethod
    def update_messages():
        r = Main.get_messages()
        if len(r) == 0:
            Main.messages_service.remove_all()
            return True
        # Error catching statements
        if type(r) != list:
            return False
        if type(r[0]) != dict:
            return False
        Main.messages_service.add_messages(r)
        return True

    # Method loads to mixer and plays audio file given a path
    # If audio file does not exist, it returns out of the method
    @staticmethod
    def play_audio(path):
        if not Downloader.check_path("../Audio/" + path + ".ogg"):
            print("There was an error loading and playing the file.\nFile might not exist.")
            return
        mixer.music.load("../Audio/" + path + ".ogg")
        mixer.music.play()
        while mixer.music.get_busy == True:
            pass

    # This method returns how long the timer should sleep for.
    # The return value is sleep time in seconds
    @staticmethod
    def get_sleep_time():
        ####### - Change this after to be retrieved from server
        START_TIME = 10
        END_TIME = 18
        #######
        current_time = Main.get_time()
        if current_time[0] >= END_TIME:
            sleep_time = 24-current_time[0] + START_TIME # Number of hours until START_TIME
            sleep_time = sleep_time * 60 * 60 # Converted to seconds
            sleep_time = sleep_time - curr_time[1] * 60 # Deduct the minutes from the sleep_time
            return sleep_time
        if current_time[0] < START_TIME:
            sleep_time = START_TIME - current_time[0] # Number of hours until START_TIME
            sleep_time = sleep_time * 60 * 60 # Converted to seconds
            sleep_time = sleep_time - current_time[1] * 60 # Deduct the minutes from the sleep_time
            return sleep_time

    # This method is responsible to play a sound based on the current time
    @staticmethod
    def play_scheduled_audio():
        current_time = Main.get_time()
        return

    #Close mixer - App will be running 24/7 there will be no need to close  the mixer


if __name__ == "__main__":
    main = Main()
    messages = main.get_messages()
    print(messages)
