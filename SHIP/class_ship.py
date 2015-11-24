__author__ = 'Minkyue'
import random
import math
from pico2d import *
import class_bullet
import class_ship
import main_code

w,a,s,d = False,False,False,False
bullet = None

def getdegree( x1, y1, x2, y2):
    a = x2 - x1
    b= y2 - y1
    c = math.sqrt(a*a + b*b)
    if (b>0):
        temp = math.acos(a / c)
    else :
        temp = 3.14*2-math.acos(a / c)
    print (a, b, c)
    return temp


class Ship:
    image = None
    image_cannon = None
    image_gun = None
    PIXEL_PER_METER = (1000 / 800)           # 10 pixel 30 cm
    RUN_SPEED_KMPH = 64.8                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
                       # m / s^2
    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8
    RADIAN_PER_DGREE = 1/180*3.14



    global a,w,s,d
    global ship


    STAY, SAIL= 0, 1


    def handle_stay(self):
        self.stand_frames +=1

    def handle_Sailing(self):
        if w == True:
            if self.scar < Ship.RUN_SPEED_PPS:
                self.scar += 5
        if d == True:
            self.degree -= 0.005
        if a == True:
            self.degree += 0.005
        if s == True:
            if self.scar > -Ship.RUN_SPEED_PPS:
                self. scar -= 5

    #fill here

    handle_state={

        STAY:handle_stay,
        SAIL: handle_Sailing




    }
    def get_bb(self):
         return self.x - 50, self.y - 50, self.x + 50, self.y + 50

    def update(self,frame_time,x,y):
        self.life_time += frame_time
        self.total_frames += Ship.FRAMES_PER_ACTION * Ship.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 8

       #self.scar = self.scar*frame_time + self.accelation* frame_time * frame_time / 2
        distance = self.scar * frame_time

        self.vecX = math.cos(self.degree)*distance
        self.vecY = math.sin(self.degree)*distance

        self.x += self.vecX
        self.y += self.vecY
        if self.scar > 0:
            self.scar-=0.1
        elif self.scar < 0:
            self.scar+=0.1
        if self.scar <0.1 and self.scar >-0.1:
            self.scar = 0

        self.gun_x = self.x+25*math.cos(self.degree)*Ship.PIXEL_PER_METER
        self.gun_y = self.y+25*math.sin(self.degree)*Ship.PIXEL_PER_METER
        self.cannon_x = self.x-30*math.cos(self.degree)*Ship.PIXEL_PER_METER
        self.cannon_y = self.y-30*math.sin(self.degree)*Ship.PIXEL_PER_METER
        self.degree_cannon = getdegree(self.cannon_x,self.cannon_y,x,y)
        self.degree_gun = getdegree(self.gun_x,self.gun_y,x,y)
        self.handle_state[self.state](self)

       # for class_bullet in bullets:
       #     bullet.update()


    def changestate(self):
        self. state = self.SAIL




    def GetKeyDown(self, key):
        global w,a,d,s
        if key == 'w':
            w = True
        elif key == 'd':
            d = True
        elif key == 's':
            s = True
        elif key == 'a':
            a = True

    def GetKeyUp(self, key):
        global w,a,d,s
        if key == 'w':
            w = False
        elif key == 'd':
            d = False
        elif key == 's':
            s = False
        elif key == 'a':
            a = False







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
        self.accelation = 0
        self.life_time = 0.0
        self.total_frames = 0.0
        self.cannon_degree = None
        self.gun_degree = None
        self.gun_x = self.x+25*math.cos(self.degree)*Ship.PIXEL_PER_METER
        self.gun_y = self.y+25*math.sin(self.degree)*Ship.PIXEL_PER_METER
        self.cannon_x = self.x-30*math.cos(self.degree)*Ship.PIXEL_PER_METER,
        self.cannon_y = self.y-30*math.sin(self.degree)*Ship.PIXEL_PER_METER
        if Ship.image == None:
            Ship.image = load_image('player_ship.png')
            Ship.image_cannon = load_image('player_cannon.png')
            Ship.image_gun =load_image('player_gun.png')

    def draw(self,frame_time):
        #self.image.clip_draw(0, 0, 300, 300, self.x, self.y)
        self.image.rotate_draw(self.degree, self.x,self.y, 100*Ship.PIXEL_PER_METER,100*Ship.PIXEL_PER_METER)
        self.image_cannon.rotate_draw(self.degree_cannon, self.cannon_x,self.cannon_y, 100*Ship.PIXEL_PER_METER,100*Ship.PIXEL_PER_METER)
        self.image_gun.rotate_draw(self.degree_gun, self.gun_x,self.gun_y, 100*Ship.PIXEL_PER_METER,100*Ship.PIXEL_PER_METER)

    def fire(self):
        global bullet
       bullets = [Bullet(self.gun_degree,self.x,self.y)]

class ENEYMEY(Ship):
    pass
