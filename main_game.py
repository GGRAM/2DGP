import sys
sys.path.append('../LabsAll/Labs')

import random
from pico2d import *

running = None
plykeydown = None
x,y=0,0
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
    global plykeydown


    LEFT_RUN, RIGHT_RUN, STAY, UP,DOWN,LEFT_UP,LEFT_DOWN,RIGHT_UP,RIGHT_DOWN = 0, 1, 2, 3,4,5,6,7,8


    def handle_stay(self):
        self.stand_frames +=1

    def handle_left_run(self):
        self.vecX -= 3
        self.state = self.STAY

    def handle_right_run(self):
        self.vecX += 3
        self.state = self.STAY

    def handle_up(self):
        self.vecY+=3
        self.state = self.STAY

    def handle_down(self):
        self.vecY-=3
        self.state = self.STAY

    def handle_LU(self):
        self.vecY += 3
        self.vecX -= 3
        self.state = self.STAY
    def handle_LD(self):
        self.vecY -=3
        self.vecX -= 3
        self.state = self.STAY
    def handle_RU(self):
        self.vecY += 3
        self.vecX += 3
        self.state = self.STAY
    def handle_RD(self):
        self.vecY -=3
        self.vecX +=3
        self.state = self.STAY


    #fill here

    handle_state={
        LEFT_RUN: handle_left_run,
        RIGHT_RUN: handle_right_run,
        STAY:handle_stay,
        UP: handle_up,
        DOWN: handle_down,
        LEFT_UP:handle_LU,
        LEFT_DOWN:handle_LD,
        RIGHT_UP:handle_RU,
        RIGHT_DOWN:handle_RD



    }


    def update(self):

        self.frame=(self.frame+1)%8
        self.x += self.vecX
        self.y += self.vecY
        if self.vecX > 0:
            self.vecX-=1
        elif self.vecX < 0:
            self.vecX+=1

        if self.vecY > 0:
            self.vecY-=1
        elif self.vecY < 0:
            self.vecY+=1

        self. handle_state[self.state](self)


    def changestate(self):

        if plykeydown == 1:
            self. state = self.UP
        elif plykeydown == 2:
            self. state = self.DOWN
        elif plykeydown == 3:
            self. state = self.LEFT_RUN
        elif plykeydown == 4:
            self. state = self.RIGHT_RUN
        elif plykeydown == 5:
            self. state = self.LEFT_UP
        elif plykeydown == 6:
            self. state = self.LEFT_DOWN
        elif plykeydown == 7:
            self. state = self.RIGHT_UP
        elif plykeydown == 8:
            self. state = self.RIGHT_DOWN






    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        self.run_frames = 0
        self.stand_frames = 0
        self.down_frame = 0
        self.jump_frame = 0
        self.state = self.STAY
        self.vecX = 0
        self.vecY = 0
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
            if plykeydown == 3:
                plykeydown = 5
            elif plykeydown == 4:
                plykeydown = 7
            else:
                plykeydown = 1
        elif event.type == SDL_KEYDOWN and event.key == SDLK_s:
            if plykeydown == 3:
                plykeydown = 6
            elif plykeydown == 4:
                plykeydown =8
            else:
                plykeydown = 2
        elif event.type == SDL_KEYDOWN and event.key == SDLK_a:
            if plykeydown == 1:
                plykeydown = 5
            elif plykeydown == 2:
                plykeydown = 6
            else:
                plykeydown = 3
        elif event.type == SDL_KEYDOWN and event.key == SDLK_d:
            if plykeydown == 1:
                plykeydown = 7
            elif plykeydown == 2:
                plykeydown =8
            else:
                plykeydown = 4
        elif event.type == SDL_KEYUP and event.key == SDLK_w or event.key == SDLK_s or event.key == SDLK_a or event.key == SDLK_d:
            plykeydown = 0
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
        if plykeydown != 0:
            boy.changestate()


        clear_canvas()

        boy.draw()
        sight.draw()
        update_canvas()

        delay(0.04)

    close_canvas()


if __name__ == '__main__':
    main()