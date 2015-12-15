import sys

sys.path.append('../LabsAll/Labs')

import title_state

from class_ship import Ship

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
sea = None
weapon = None
member = None
box = None
Box = None
weapon_image_bullet = None
weapon_image_cannon = None

class Sea:
    image = None
    def __init__(self):
        if Sea.image == None:
            Sea.image = load_image('background.png')
    def draw(self):
        self.image.clip_draw(0,0,800,600,400,300)

class Sight:
    image = None
    def __init__(self):
        if Sight.image == None:
            Sight.image = load_image('sight.png')
        self.x , self.y = 0,0

    def draw(self):
        #self.image.clip_draw(0,0,160,160,self.x,self.y)
        self.image.rotate_draw(0, self.x,self.y, 50,50)
    def update(self):
        global x,y
        self.x=x
        self.y=y
def collide_weapon(a,b):
    x_a, y_a= a.getBB()
    left_b, bottom_b, right_b, top_b = b.getBB()

    if x_a > right_b: return False
    if x_a < left_b: return False
    if y_a < bottom_b: return False
    if y_a > top_b: return False
    return True

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True
class EnemyBox:
    image= None

    def __init__(self):
        if EnemyBox.image == None:
            EnemyBox.image = load_image('box.png')
            print('box get image')
        self.x, self.y = random.randint(50, 750), random.randint(50, 550)

    def draw(self):
        self.image.clip_draw(0,0,50,50,self.x,self.y)
        print('box draw')
    def update(self):
        pass

    def getBB(self):
        return self.x -20, self.y - 20,  self.x + 20, self.y + 20

def create_world():
    global ship, sight, Box , weapon, sea
    global weapon_image_bullet,weapon_image_cannon
    ship = Ship()
    sight = Sight()
    sea = Sea()
    weapon = 1
    Box = [EnemyBox() for i in range(10)]
    weapon_image_bullet = load_image('weapon_select2.png')
    weapon_image_cannon = load_image('weapon_select1.png')





def destroy_world():
    global ship, sight, Box, sea

    del(ship)
    del(sight)
    del(Box)
    del(sea)




def enter():

    open_canvas()
    game_framework.reset_time()
    global weapon
    global member
    global box
    member = 0
    weapon = 0
    box = 0

    create_world()

def exit():
    destroy_world()
    close_canvas()

def handle_events(frame_time):
    global running

    global x,y
    global w,a,s,d
    global ship
    global weapon
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False


        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            exit()


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
        elif event.type == SDL_KEYDOWN and event.key == SDLK_1:
            weapon= 1
        elif event.type == SDL_KEYDOWN and event.key == SDLK_2:
            weapon= 2
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, 600 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            if weapon == 2:
                print ('click')
                ship.fire(2)
            elif weapon == 1:
                ship.fire(1)



def update(frame_time):
    global ship
    global sight
    global player_missile
    global member
    global box
    global Box
    handle_events(frame_time)
    ship.update(frame_time,x,y)
    sight.update()
    for member in ship.player_bullet:
        a, b= member.getBB()
        if a > 800 or a < 0 or b<0 or b>600:
            ship.player_bullet.remove(member)
    for member in ship.player_cannon:
        a, b= member.getBB()
        if a > 800 or a < 0 or b<0 or b>600:
            ship.player_cannon.remove(member)
    print(ship.player_bullet)
    for member in ship.player_cannon:
        for box in Box:
            if collide_weapon(member, box):
                Box.remove(box)
    for member in ship.player_bullet:
        for box in Box:
            if collide_weapon(member, box):
                Box.remove(box)






def draw(frame_time):

    clear_canvas()
    sea.draw()


    for box in Box:
        box.draw()
    ship.draw(frame_time)
    if weapon == 1:
        weapon_image_bullet.clip_draw(0,0,150,80,300-200,40)
        weapon_image_cannon.clip_draw(150,0,150,80,450-200,40)
    else:
        weapon_image_cannon.clip_draw(0,0,150,80,450-200,40)
        weapon_image_bullet.clip_draw(150, 0,150,80,300-200,40)
    sight.draw()



    update_canvas()

