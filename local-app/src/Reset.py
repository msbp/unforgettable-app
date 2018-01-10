# This file should be placed in src/
# It is expected that ../Audio/ exists or program will exit

import os
import shutil

# Add folders to be reset to folders array
folders = ("Greetings/", "Hours/")

def check_path(path):
    return os.path.exists(path)

def reset():
    print("Running reset script.")
    print("This script:")
    print("1. Deletes all audio files within Audio/")
    print("2. Deletes folders withing Audio/")
    print("3. Creates new folders within Audio/\n\n")
    print("Audio file should be downloaded again after reset.\n\n")

    if not check_path("../Audio/"):
        print("An error has occurred:\n../Audio/ does NOT exist.")
        print("Program will exit now.");
        return

    # Remove folders and their content
    for folder in folders:
        if check_path("../Audio/" + folder):
            shutil.rmtree("../Audio/"+ folder)
    # Create empty folders
    for folder in folders:
        if not check_path("../Audio/" + folder):
            os.makedirs("../Audio/" + folder)
            print("Created:"+folder)

if __name__ == "__main__":
    reset();
