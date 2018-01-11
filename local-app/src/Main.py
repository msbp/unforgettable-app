import boto3
import os
import time
import datetime
import requests
from pygame import mixer
from Downloader import Downloader
from Messages import Messages

class Main:
    # Initialize audio player
    mixer.init()

    ####################################################
    # Methods responsible in calling play_audio method #
    ####################################################
    # Method says greetings. 3 Options: Morning, Afternoon, Night
    # AfternoonBeing and AfternoonEnd determine when to switch greetings
    # time is an array in format (HOUR, MINUTE)
    @staticmethod
    def say_greetings(time):
        if time[0] < Messages.AfternoonBegin:
            play_audio("Greetings/Morning")
        elif time[0] < Messages.AfternoonEnd:
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

    # Method obtains list of messages from server
    # Returns a dictionary list with messages
    @staticmethod
    def get_messages():
        getUrl = 'http://127.0.0.1:8000/getMessages'
        r = requests.get(getUrl)
        return r.json()

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

    #Close mixer - App will be running 24/7 there will be no need to close  the mixer


if __name__ == "__main__":
    main = Main()
    messages = main.get_messages()
    print(messages)
