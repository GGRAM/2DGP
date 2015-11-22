import sys

sys.path.append('../LabsAll/Labs')

import title_state
import class_bullet
from  class_ship import Ship
from class_bullet import Bullet
import random
import class_ship
from pico2d import *
import game_framework

name = "main_code"
running = None
plykeydown = None
x,y=0,0
w,a,s,d = False,False,False,False
ship = None
sight = None

class Sight:
    image = None
    def __init__(self):
        if Sight.image == None:
            Sight.image = load_image('sight.png')
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


def create_world():
    global ship, sight

    ship = Ship()
    sight = Sight()





def destroy_world():
    global ship, sight

    del(ship)
    del(sight)




def enter():
    open_canvas()
    game_framework.reset_time()

    create_world()

def exit():
    destroy_world()
    close_canvas()

def handle_events(frame_time):
    global running
    global plykeydown
    global x,y
    global w,a,s,d
    global ship
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False


        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            exit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            plykeydown = 0

        # 움직임
        elif event.type == SDL_KEYDOWN and event.key == SDLK_w:
            ship.GetKeyDown('w')
        elif event.type == SDL_KEYDOWN and event.key == SDLK_s:
            ship.GetKeyDown('s')
        elif event.type == SDL_KEYDOWN and event.key == SDLK_a:
            ship.GetKeyDown('a')
        elif event.type == SDL_KEYDOWN and event.key == SDLK_d:
            ship.GetKeyDown('d')
        elif event.type == SDL_KEYUP and event.key == SDLK_w :
            ship.GetKeyUp('w')
        elif event.type == SDL_KEYUP and event.key == SDLK_s :
            ship.GetKeyUp('s')
        elif event.type == SDL_KEYUP and event.key == SDLK_a :
            ship.GetKeyUp('a')
        elif event.type == SDL_KEYUP and event.key == SDLK_d :
            ship.GetKeyUp('d')
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, 600 - event.y



def update(frame_time):
    global ship
    global sight
    handle_events(frame_time)
    ship.update(frame_time)
    sight.update()


def draw(frame_time):

    clear_canvas()
    ship.draw(frame_time)
    sight.draw()
    update_canvas()

