import sys
sys.path.append('../LabsAll/Labs')

import random
from pico2d import *

running = None
plykeydown = None
x,y=0,0
w,a,s,d = False,False,False,False

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

class Sight:

    def __init__(self):

        Sight.image = load_image('sight.png')
        self.x , self.y = 0,0

    def draw(self):
        self.image.clip_draw(0,0,160,160,self.x,self.y)
    def update(self):
        global x,y
        self.x=x
        self.y=y

class Ship:
    image = None

    global a,w,s,d


    STAY, SAIL= 0, 1


    def handle_stay(self):
        self.stand_frames +=1

    def handle_Sailing(self):
        if w == True:
            self.scar = math.sqrt(self.vecX *self.vecX + self.vecY *self.vecY)
            if self.scar < 5:
                self.vecX += math.cos(self.degree)
                self.vecY += math.sin(self.degree)



            if self.vecX > 0:
                self.vecX -= 0.5
            elif self.vecX < 0:
                self.vecX +=0.5
            if self.vecY < 0:
                self.vecY -= 0.5
            elif self.vecY < 0:
                self.vecY +=0.5

        if d == True:
            self.degree -= 0.09
        if a == True:
            self.degree += 0.09
        if s == True:
            self.scar = math.sqrt(self.vecX *self.vecX + self.vecY *self.vecY)
            if self.scar < 5:
                self.vecX -= math.cos(self.degree)
                self.vecY -= math.sin(self.degree)
            if self.vecX > 0:
                self.vecX -= 0.5
            elif self.vecX < 0:
                self.vecX +=0.5
            if self.vecY < 0:
                self.vecY -= 0.5
            elif self.vecY < 0:
                self.vecY +=0.5

    #fill here

    handle_state={

        STAY:handle_stay,
        SAIL: handle_Sailing




    }


    def update(self):

        self.frame=(self.frame+1)%8


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
        self.inertiaX = 0
        self.inertiaY = 0
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


def main():

    open_canvas()

    boy = Ship()
    sight = Sight()

    global running
    running = True
    global plykeydown
    plykeydown = 0

    while running:
        handle_events()

        boy.update()
        sight.update()




        clear_canvas()

        boy.draw()
        sight.draw()
        update_canvas()

        delay(0.04)

    close_canvas()


if __name__ == '__main__':
    main()