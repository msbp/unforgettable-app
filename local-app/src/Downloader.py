import requests
import os
import boto3
from Messages import Messages      # This file includes messages to be used

class Downloader:
    # Set these variables accordingly
    ###
    VOICE = "Ricardo"
    MAX_NUMBER_DOWNLOADS = 10       # This is to avoid error downloads
    REQUEST_COUNTER = 0             # This is to keep track of the number of request made
    ###

    polly = boto3.client("polly")
    speech = None

    def __init__(self):
        return
        # Constructor

    # Method downloads and creates daily greetings audio files if files do no exist
    # Greetings mapping:
    # Morning   -> Greetings/Morning.ogg
    # Afternoon -> Greetings/Afternoon.ogg
    # Night     -> Greetings/Night.ogg
    @staticmethod
    def create_greetings():
        if not check_path("../Audio/Greetings/"):
            os.makedirs("../Audio/Greetings/")
        if not check_path("../Audio/Greetings/Morning.ogg"):
            download_audio(Messages.Morning)
            create_audio("../Audio/Greetings/Morning", speech["AudioStream"].read())
        if not check_path("../Audio/Greetings/Afternoon.ogg"):
            download_audio(Messages.Afternoon)
            create_audio("../Audio/Greetings/Afternoon", speech["AudioStream"].read())
        if not check_path("../Audio/Greetings/Night.ogg"):
            download_audio(Messages.Night)
            create_audio("../Audio/Greetings/Night", speech["AudioStream"].read())

    # Method downloads and creates hour audio files if they do not exist
    # Hours mapping:
    # Hour -> Hours/Hour.ogg
    # intro_hour is an array of 2 elements and hour goes in between them
    @staticmethod
    def create_hours():
        if not check_path("../Audio/Hours/"):
            os.makedirs("../Audio/Hours/")
        for hour in Messages.hours:
            if not check_path("../Audio/Hours/" + hour + ".ogg"):
                download_audio(Messages.intro_hour[0] + hour + Messages.intro_hour[1])
                create_audio("../Audio/Hours/" + hour, speech["AudioStream"].read())

    # Method downloads and creates meal reminders audio files if they do not exist
    # Meals mapping:
    # Lunch -> Meals/Lunch.ogg
    # Dinner -> Meals/Dinner.ogg
    # Lunch and Dinner are arrays in the format [MEALTIME, MESSAGE]
    @staticmethod
    def create_meal_reminders():
        if not check_path("../Audio/Meals/"):
            os.makedirs("../Audio/Meals/")
        if not check_path("../Audio/Meals/Lunch.ogg"):
            download_audio(Messages.Lunch[1])
            create_audio("../Audio/Meals/Lunch", speech["AudioStream"].read())
        if not check_path("../Audio/Meals/Dinner.ogg"):
            download_audio(Messages.Dinner[1])
            create_audio("../Audio/Meals/Dinner", speech["AudioStream"].read())

    # Method download and creates day audio files if they do not exist
    # Days mapping:
    # Monday -> Days/Monday.ogg
    # Tuesday -> Days/Tuesday.ogg
    # Wednesday -> Days/Wednesday.ogg
    # Thursday -> Days/Thursday.ogg
    # Friday -> Days/Friday.ogg
    # Saturday -> Days/Saturday.ogg
    # Sunday -> Days/Sunday.ogg
    # intro_day is an array of 2 elements and day goes in between them
    @staticmethod
    def create_days():
        if not check_path("../Audio/Days/"):
            os.makedirs("../Audio/Days/")
        for day in Message.days:
            if not check_path("../Audio/Days/" + day + ".ogg"):
                download_audio(Messages.intro_day[0] + day + Messages.intro_day[1])
                create_audio("../Audio/Days/" + day, speech["AudioStream"].read())

    # Method synthesizes(downloads) audio file containing message
    # It is returned in the speech variable
    @staticmethod
    def download_audio(message):
        if REQUEST_COUNTER > MAX_NUMBER_DOWNLOADS:
            print("Maximum number of downloads -> " + REQUEST_COUNTER + " reached.")
            return
        speech = polly.synthesize_speech(Text = message, OutputFormat = "ogg_vorbis", VoiceId = VOICE)
        REQUEST_COUNTER += 1;

    # Method creates audio file using data passed in
    # file_name contains path within Audio folder
    @staticmethod
    def create_audio(file_name, data):
        with open(file_name + ".ogg", "wb") as f:
            f.write(data)
            f.close()

    # Method checks to see if a file already exists
    @staticmethod
    def check_path(path):
        return os.path.exists(path)
