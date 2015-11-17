__author__ = 'Minkyue'
import random
import math
import class_bullet
import  class_ship
from pico2d import *

class Bullet:
    def __init__(self):

        self.dgree
        self.x , self.y = 0,0
        self.vecX, self.vecY=0,0

    def draw(self):
        pass

    def update(self):

        self.vecX = math.cos(self.degree)*self.scar
        self.vecY = math.sin(self.degree)*self.scar

        self.x += self.vecX
        self.y += self.vecY
