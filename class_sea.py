__author__ = 'Minkyue'
import random
import main_code

from pico2d import *

class Sea:
    image = None
    def __init__(self):
        if Sea.image == None:
            self.image = load_image('sea.png')

    def draw(self):
        self.image.draw(400,300)


    # fill here

