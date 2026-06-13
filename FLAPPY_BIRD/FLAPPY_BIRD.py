import pygame as pg  
import sys  
import time as t
from BIRD import Bird
from pi import Pipe 
pg.init()

class Game:
    def __init__(self):
        self.width = 400
        self.height = 711
        self.win = pg.display.set_mode((self.width, self.height))
        self.clock = pg.time.Clock()
        self.move_speed = 250
        self.Bird = Bird()
        self.Pause=False


        self.score=0
        self.font=pg.font.Font("ASSETS/SCORE_F.TTF",24)
        self.fontR=pg.font.Font("ASSETS/SCORE_F.TTF",50)
        self.FontPause=pg.font.Font("ASSETS/SCORE_F.ttf",70)

        self.score_T=self.font.render("SCORE: 0",True,(0,0,255))
        self.score_T_rect=self.score_T.get_rect(center=(50,30))

        self.Restart_T=self.fontR.render("Restart",True,(255,255,255))
        self.Restart_T_rect=self.Restart_T.get_rect(center=(190,340))

        self.FontPause=self.FontPause.render("PAUSED",True,(255,0,0,255))
        self.FontPause_rect=self.FontPause.get_rect(center=(200,320))

        self.ismove=True
        self.isEnterPressed = False
        self.isGame_Started=True
        self.Pipes = []
        self.pipe_generate_Co = 71
    

    
        self.setupbg_gr()
        self.StartM=False
        self.gameloop()


    def gameloop(self):
        self.i=1
        last_time = t.time()
        while True:
            new_time = t.time()
            dt = new_time - last_time
            last_time = new_time
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.Last=self.score
                    with open("score.txt", "a") as s:
                        s.write(f"\nTIMELINE {t.asctime()}  : SCORE {self.Last}")
                    pg.quit()
                    sys.exit()
                if event.type == pg.KEYDOWN and self.isGame_Started==True:
                    if event.key == pg.K_RETURN:
                        self.isEnterPressed = True
                        self.Bird.UO=True 
                    if event.key == pg.K_SPACE and self.isEnterPressed:
                        self.Bird.flap(dt)
                if event.type==pg.MOUSEBUTTONUP:
                    if self.Restart_T_rect.collidepoint(pg.mouse.get_pos()):
                        self.RestartGame()
                if event.type == pg.KEYDOWN and self.isGame_Started==False:
                    if event.key == pg.K_RETURN:
                        self.RestartGame()
                if event.type==pg.KEYDOWN:
                    if event.key==pg.K_s:
                        self.G_Pause()
                    if event.key==event.key==pg.K_r:
                        self.GPE()


            self.updateEveryThing(dt)
            self.CheckCol()
            self.DrawEveryThing()
            pg.display.update()
            self.clock.tick(60)
            self.Check_Score()
    
    def RestartGame(self):
        self.Last=self.score
        with open("score.txt", "a") as s:
            s.write(f"\nTIMELINE {t.asctime()}  : SCORE {self.Last}")
        self.score=0
        self.score_T=self.font.render("SCORE: 0",True,(0,0,255))
        self.isEnterPressed=False
        self.isGame_Started=True
        self.Bird.Reset_Bird()
        self.Pipes.clear()
        self.pipe_generate_Co=71
        self.Bird.UO=False


    def Check_Score(self):
        if len(self.Pipes)>0:
            if (self.Bird.rect.left>self.Pipes[0].rect_down.left and self.Bird.rect.right<self.Pipes[0].rect_down.right and not self.StartM):
                self.StartM=True
            if self.Bird.rect.left>self.Pipes[0].rect_down.right and self.StartM==True:
                self.StartM=False
                self.score +=1
                self.score_T=self.font.render(f"SCORE: {self.score}",True,(0,0,0))


    def CheckCol(self):
        if len(self.Pipes):
            if (self.Bird.rect.bottom>=568):
                self.Bird.UO=False
                self.isEnterPressed=False
                self.isGame_Started=False
            elif(self.Bird.rect.colliderect(self.Pipes[0].rect_down) or self.Bird.rect.colliderect(self.Pipes[0].rect_up)):
                self.isEnterPressed=False
                self.isGame_Started=False

                # time.sleep(0.3)
                # self.Bird.rect.bottom=568
    def updateEveryThing(self, dt):
        if self.isEnterPressed and self.ismove:
            self.ground1_rect.x -= self.move_speed * dt
            self.ground2_rect.x -= self.move_speed * dt
            if self.ground1_rect.right < 0:
                self.ground1_rect.x = int(self.ground2_rect.right)
            if self.ground2_rect.right < 0:
                self.ground2_rect.x = int(self.ground1_rect.right)
            if self.pipe_generate_Co > 70:
                self.generatePipe()
                self.pipe_generate_Co = 0
            self.pipe_generate_Co += 1

            for pipe in self.Pipes:
                if self.ismove==True:
                    pipe.P_update(dt)
                    if  len(self.Pipes)!=0:
                        if self.Pipes[0].rect_up.right<0:
                            self.Pipes.pop(0)
        self.Bird.update(dt)


    def DrawEveryThing(self):
        self.win.blit(self.back, (0, 0))
        for pipe in self.Pipes:
            pipe.DrawPipe(self.win)
        self.win.blit(self.ground1, self.ground1_rect)
        self.win.blit(self.ground2, self.ground2_rect)
        self.win.blit(self.Bird.image, self.Bird.rect)
        self.win.blit(self.score_T, self.score_T_rect)
        if self.isGame_Started==False:
            self.win.blit(self.Restart_T,self.Restart_T_rect)
        if self.Pause==True:
            self.win.blit(self.FontPause,self.FontPause_rect)

    def setupbg_gr(self):
#UPPER GROUND 
        self.back = pg.image.load("ASSETS/back.png").convert_alpha()
        self.ground1 = pg.image.load("ASSETS/ground.png").convert_alpha()
        self.ground2 = pg.image.load("ASSETS/ground.png").convert_alpha()
        self.ground1_rect = self.ground1.get_rect()
        self.ground2_rect = self.ground2.get_rect()
        self.ground1_rect.x = 0
        self.ground2_rect.x = self.ground1_rect.right
        self.ground1_rect.y = 568
        self.ground2_rect.y = 568


    def generatePipe(self):
        # Adjust the initial x-coordinate to ensure pipes appear on-screen
        pipe = Pipe(self.move_speed)
        pipe.rect_up.x = self.width
        pipe.rect_down.x = self.width
        self.Pipes.append(pipe)
    def G_Pause(self):
        self.Bird.UO=False
        self.ismove=False
        self.Pause=True
       
    def GPE(self):
        self.Bird.UO=True
        self.ismove=True
        self.Pause=False

g = Game()
