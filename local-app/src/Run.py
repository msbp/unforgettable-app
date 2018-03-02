from Main import *

if __name__ == '__main__':
    localApp = Main()
    #mixer.init()
    sleep_time = 60 * 60

    while (True):
        sleep_time = Main.get_sleep_time() # Sleep time in seconds
        Main.play_scheduled_audio()
        time.sleep(sleep_time)
        pass
        ###########


    # Close mixer at the end
