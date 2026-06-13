import pygame as pg   
from random import randint
class Pipe:
    def __init__(self,move_speed):
        self.img_up= pg.image.load("ASSETS/up.png").convert_alpha()
        self.img_down= pg.image.load("ASSETS/down.png").convert_alpha()
        self.rect_up= self.img_up.get_rect()
        self.rect_down= self.img_down.get_rect()
        self.pipeD=140
        self.rect_up.y=randint(250,520)
        self.rect_up.x=600
        self.rect_down.y=self.rect_up.y-self.pipeD-self.rect_up.height
        self.rect_down.x=600
        self.move_speed=move_speed
    def P_update(self,dt):
        self.rect_up.x-=int(self.move_speed*dt)
        self.rect_down.x -=int(self.move_speed*dt)
    def DrawPipe(self,win):
        win.blit(self.img_up,self.rect_up)
        win.blit(self.img_down,self.rect_down)



