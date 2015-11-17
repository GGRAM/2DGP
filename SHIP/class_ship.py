__author__ = 'Minkyue'
import random
import math
from pico2d import *
import class_bullet
import  class_ship
class Ship:
    image = None

    global a,w,s,d


    STAY, SAIL= 0, 1


    def handle_stay(self):
        self.stand_frames +=1

    def handle_Sailing(self):
        if w == True:
            if self.scar < 20 :
                self.scar += 3
        if d == True:
            self.degree -= 0.09
        if a == True:
            self.degree += 0.09
        if s == True:
            if self.scar > -15 :
                self. scar -= 2

    #fill here

    handle_state={

        STAY:handle_stay,
        SAIL: handle_Sailing




    }
    def get_bb(self):
         return self.x - 50, self.y - 50, self.x + 50, self.y + 50

    def update(self):

        self.frame=(self.frame+1)%8
        self.vecX = math.cos(self.degree)*self.scar
        self.vecY = math.sin(self.degree)*self.scar

        self.x += self.vecX
        self.y += self.vecY
        if self.scar > 0:
            self.scar-=1
        elif self.scar < 0:
            self.scar+=1

        self. handle_state[self.state](self)


    def changestate(self):


        self. state = self.SAIL







    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        self.run_frames = 0
        self.stand_frames = 0
        self.down_frame = 0
        self.jump_frame = 0
        self.state = self.SAIL
        self.vecX = 0
        self.vecY = 0
        self.scar = 0
        self.degree = 0
        self.HP = 100
        if Ship.image == None:
            Ship.image = load_image('ship.png')


    def draw(self):
        self.image.clip_draw(0, 0, 300, 300, self.x, self.y)
        self.image.clip_draw(300, 0, 300, 300, self.x, self.y)
        self.image.clip_draw(600, 0, 300, 300, self.x, self.y)

class ENEYMEY(Ship):
    pass
