__author__ = 'Minkyue'
import random
import math
import class_bullet
import class_ship
from class_ship import Ship
from pico2d import *

class Bullet:
    image=None
    def __init__(self,degree,x,y):
        self.scar = 50
        self.degree = degree
        self.x , self.y = x,y
        self.vecX, self.vecY=0,0
        if Bullet.image == None:
            Bullet.image = load_image('bullet.png')

    def draw(self):
        self.image.rotate_draw(self.degree, self.x,self.y, 100*Ship.PIXEL_PER_METER,100*Ship.PIXEL_PER_METER)

    def update(self):

        self.vecX = math.cos(self.degree)*self.scar
        self.vecY = math.sin(self.degree)*self.scar

        self.x += self.vecX
        self.y += self.vecY
