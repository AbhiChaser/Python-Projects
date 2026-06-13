from typing import Any
import pygame as pg

class Bird(pg.sprite.Sprite):
    def __init__(self):
        super(Bird,self).__init__()
        self.img_list = [pg.image.load("ASSETS/birdup.png").convert_alpha(), pg.image.load("ASSETS/birddown.png").convert_alpha()]
        self.image_index=0
        self.image=self.img_list[self.image_index]
        self.rect=self.image.get_rect(center=(100,100))
        self.y_velocity=0
        self.gravity=10
        self.flap_speed=250
        self.amin_counter=0
        self.UO=False
    def update(self,dt):
        if self.UO==True:
            self.PlayAnimation()
            self.Applygravity(dt)
            if self.rect.y<=0 and self.flap_speed==250:
                self.rect.y=0
                self.flap_speed=0
                self.y_velocity=0
            elif self.rect.y>0 and self.flap_speed==0:
                self.flap_speed=250
    def Applygravity(self,dt):
        self.y_velocity+=self.gravity*dt
        self.rect.y+=self.y_velocity
    def flap(self,dt):
        self.y_velocity =-self.flap_speed*dt
    def PlayAnimation(self):
        if self.amin_counter==5:
            self.image=self.img_list[self.image_index]
            if self.image_index==0:
                self.image_index=1
            else:self.image_index=0
            self.amin_counter=0
        self.amin_counter+=1
        self.y_velocity+=0.05
    def Reset_Bird(self):
        self.rect.center=(100,100)
        self.y_velocity=0
        self.amin_counter=0

