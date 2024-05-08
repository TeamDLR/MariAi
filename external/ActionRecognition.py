# Common modules
import os

# Useful constants
DB_PATH = "remove if not needed"
MODEL_NAME = "remove if not needed"
VIDEO_PATH = ".." + os.path.sep + "videos"
# ...

def initial_setup(folders=[]):
    for folder in folders:
        if not os.path.exists(folder):
            os.mkdir(folder)

def action_recognition():
    #initial_setup(DB_PATH, VIDEO_PATH)
    # for video in os.listdir(VIDEO_PATH): # or whatever
    #    recognize(video)
    pass


def recognize(video):
    # call library to...
    # do the magic!
    pass
    
