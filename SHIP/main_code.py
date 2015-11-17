import sys

sys.path.append('../LabsAll/Labs')

import title_state
import class_bullet
from  class_ship import Ship
from class_bullet import Bullet
import random
from pico2d import *

name = "main_code"
running = None
plykeydown = None
x,y=0,0
w,a,s,d = False,False,False,False
boy = None
sight = None
class Sight:
    image = None
    def __init__(self):
        if sight.image == None:
            sight.image = load_image('sight.png')
            self.x , self.y = 0,0

    def draw(self):
        self.image.clip_draw(0,0,160,160,self.x,self.y)
    def update(self):
        global x,y
        self.x=x
        self.y=y

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True

def handle_events():
    global running
    global plykeydown
    global x,y
    global w,a,s,d
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False


        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            plykeydown = 0

        # 위 1 아래 2 왼쪽 3 오른쪽 4 좌상 5 좌하 6 우상 7 우하 8
        elif event.type == SDL_KEYDOWN and event.key == SDLK_w:
            w = True
        elif event.type == SDL_KEYDOWN and event.key == SDLK_s:
            s = True
        elif event.type == SDL_KEYDOWN and event.key == SDLK_a:
            a = True
        elif event.type == SDL_KEYDOWN and event.key == SDLK_d:
            d = True
        elif event.type == SDL_KEYUP and event.key == SDLK_w :
            w = False
        elif event.type == SDL_KEYUP and event.key == SDLK_s :
            s = False
        elif event.type == SDL_KEYUP and event.key == SDLK_a :
            a = False
        elif event.type == SDL_KEYUP and event.key == SDLK_d :
            d = False
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, 600 - event.y

def enter():
    global boy
    global sight
    boy = Ship()
    sight = Sight()
    open_canvas()

def update():
    handle_events()

    boy.update()
    sight.update()




    clear_canvas()

    boy.draw()
    sight.draw()
    update_canvas()

    delay(0.04)
