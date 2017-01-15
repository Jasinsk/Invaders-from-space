# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 21:06:50 2017

@author: jasin
"""

#-----!!!!SPACE INVADERS!!!!-----

import pygame
import random
from pygame.locals import *

pygame.display.set_caption('WHEN ALIENS INVADE')

#----------------------------------------------------------------------

class Ship():

    def __init__(self, screen_rect):

        #self.image = pygame.image.load("spaceship.png")
        self.image = pygame.image.load("ship1.png")
        self.image = pygame.transform.scale(self.image, (50,50))

        self.rect = self.image.get_rect()

        # put ship bottom, center x 
        self.rect.bottom = screen_rect.bottom 
        self.rect.centerx = screen_rect.centerx

        self.move_x = 0

        self.shots = []
        self.shots_count = 0

        self.max_shots = 5
        self.is_alive = True
        self.health=3
    #--------------------

    def event_handler(self, event):

        #print "debug: Ship.event_handler"

        if event.type == KEYDOWN:
            if (event.key == K_LEFT or event.key == K_a):
                self.move_x = -5
            elif (event.key == K_RIGHT or event.key == K_d):
                self.move_x = 5
            elif event.key == K_z or event.key == K_UP or event.key == K_w:
                if len(self.shots) < self.max_shots:
                    self.shots.append(Bullet(self.rect.centerx, self.rect.top))

        if event.type == KEYUP:
            if event.key in (K_LEFT, K_RIGHT):
                self.move_x = 0

    def update(self):

        #print "debug: Ship.update: move_x", self.move_x
        self.rect.x += self.move_x
        if self.rect.x > 700:
            self.rect.x=700
        if self.rect.x < 0:
            self.rect.x=0
        for s in self.shots:
            s.update()

        for i in range(len(self.shots)-1, -1, -1):
            print ("debug: Ship.update: testing bullet ", i)
            if not self.shots[i].is_alive:
                print ("debug: Ship.update: removing bullet ", i)
                del self.shots[i]
    def health_check(self):
        self.health+=-1
        if self.health==2:
            self.image==pygame.image.load("ship2.png")
        if self.health==1:
            self.image==pygame.image.load("ship3.png")
        if self.health==0:
            self.is_alive=False

    #--------------------

    def draw(self, screen):

        screen.blit(self.image, self.rect.topleft)

        for s in self.shots:
            s.draw(screen)

    def bullet_detect_collison(self, enemy_list):

        for s in self.shots:
            for e in enemy_list:
                if pygame.sprite.collide_circle(s, e):
                    s.is_alive = False
                    e.is_alive = False
        

#----------------------------------------------------------------------

class Bullet():

    def __init__(self, x, y):

        self.image = pygame.image.load("ball2.png")
        self.image = pygame.transform.scale(self.image, (5,15))

        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y

        self.is_alive = True

    #--------------------

    def update(self):

        self.rect.y -= 15

        if self.rect.y < 0:
            self.is_alive = False

    #--------------------

    def draw(self, screen):

        screen.blit(self.image, self.rect.topleft)
        
        
#----------------------------------------------------------------------

class Enemy_Bullet():

    def __init__(self, x, y):

        self.image = pygame.image.load("ball1.png")
        self.image = pygame.transform.scale(self.image, (5,15))

        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y

        self.is_alive = True

    #--------------------

    def update(self):

        self.rect.y += 7

        if self.rect.y > -800:
            self.is_alive = False

    #--------------------

    def draw(self, screen):

        screen.blit(self.image, self.rect.topleft)
        
#----------------------------------------------------------------------
class Enemy_Bomb():

    def __init__(self, x, y):

        self.image = pygame.image.load("ball2.png")
        self.image = pygame.transform.scale(self.image, (20,20))

        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y

        self.is_alive = True

    #--------------------

    def update(self):

        self.rect.y += 1

        if self.rect.y > -800:
            self.is_alive = False

    #--------------------

    def draw(self, screen):

        screen.blit(self.image, self.rect.topleft)

#----------------------------------------------------------------------

class Enemy():

    def __init__(self, x, y):

        self.image = pygame.image.load("ball3.png")
        self.image = pygame.transform.scale(self.image, (15,15))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.shots=[]
        self.is_alive = True

    #--------------------

    def update(self):
        a=random.randint(0,800)
        if self.rect.x==750 and self.rect.y % 2==0:
            self.rect.y += 75
        elif self.rect.x==50 and self.rect.y % 2==1:
            self.rect.y += 75
        elif self.rect.y % 2==0:
            self.rect.x +=1
        elif self.rect.y % 2==1:
            self.rect.x+=-1
            
        if a==0:
            self.shots.append(Enemy_Bullet(self.rect.centerx, self.rect.centery))
        for s in self.shots:
            s.update()
    #--------------------

    def draw(self, screen):

        screen.blit(self.image, self.rect.topleft)
        
        for s in self.shots:
            s.draw(screen)
#----------------------------------------------------------------------
class Enemy_2():

    def __init__(self, x, y):

        self.image = pygame.image.load("ball1.png")
        self.image = pygame.transform.scale(self.image, (15,15))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.shots=[]
        self.is_alive = True

    #--------------------

    def update(self):
        a=random.randint(0,400)
        if self.rect.x==750 and self.rect.y % 2==0:
            self.rect.y += 75
        elif self.rect.x==50 and self.rect.y % 2==1:
            self.rect.y += 75
        elif self.rect.y % 2==0:
            self.rect.x +=1
        elif self.rect.y % 2==1:
            self.rect.x+=-1
        #~ if self.rect.y < 0:
            #~ self.is_alive = False
        if a==0:
            self.shots.append(Enemy_Bomb(self.rect.centerx, self.rect.centery))
        for s in self.shots:
            s.update()
    #--------------------

    def draw(self, screen):

        screen.blit(self.image, self.rect.topleft)
        
        for s in self.shots:
            s.draw(screen)
#----------------------------------------------------------------------
class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load('sky.png')
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

#----------------------------------------------------------------------
class Game():

    def __init__(self):

        pygame.init()

        w, h = 800, 700
        self.screen = pygame.display.set_mode((w,h))

        pygame.mouse.set_visible(False)

        self.ship = Ship(self.screen.get_rect())

        self.enemies = []

        for i in range(100, 800, 100):
            self.enemies.append(Enemy(i, 100))
            self.enemies.append(Enemy(i, 175))
            self.enemies.append(Enemy(i, 250))

        font = pygame.font.SysFont("", 72)
        self.text_paused = font.render("PAUSED", True, (255, 0, 0))
        self.text_paused_rect = self.text_paused.get_rect(center=self.screen.get_rect().center)
        
        self.text_intro = font.render("INVADERS FROM SPACE", True, (0, 255, 255))
        self.text_intro_rect = self.text_intro.get_rect(center=self.screen.get_rect().center)
        
        self.text_end = font.render("You Dead", True, (255, 0, 255))
        self.text_end_rect = self.text_end.get_rect(center=self.screen.get_rect().center)
        
        self.text_win = font.render("You WIN", True, (255, 255, 0))
        self.text_win_rect = self.text_end.get_rect(center=self.screen.get_rect().center)

    #-----MAIN GAME LOOP-----

    def run(self):

        clock = pygame.time.Clock()
        
        INTRO = True
        RUNNING = True
        PAUSED = False
        counter=0
        BackGround = Background('sky.png', [0,0])
        while RUNNING:

            clock.tick(30)
            
            if INTRO:
                self.screen.blit(self.text_intro, self.text_intro_rect)
                for event in pygame.event.get():
                    if event.type == KEYDOWN:
                        if event.key == K_SPACE:
                            INTRO = not INTRO
                        if event.key == K_ESCAPE:
                            RUNNING = False
                            break
                self.screen.blit(self.text_intro, self.text_intro_rect)
                pygame.display.update()
            #--- events ---
            elif self.ship.is_alive==True:
                if len(self.enemies)==0:
                    self.screen.blit(self.text_win, self.text_win_rect)
                    for event in pygame.event.get():
                       if event.type == KEYDOWN:
                           if event.key == K_ESCAPE:
                               RUNNING = False
                               break
                           if event.key == K_SPACE:
                               Game().run()
                else:
                    for event in pygame.event.get():
                        
                        if event.type == pygame.QUIT:
                            RUNNING = False
        
                        if event.type == KEYDOWN:
                            if event.key == K_ESCAPE:
                                RUNNING = False
        
                            if event.key == K_p:
                                PAUSED = not PAUSED
        
                        if not PAUSED:
                            self.ship.event_handler(event)
                            
                    if counter==100:
                        a=random.randint(0,2)
                        if a==0:
                            self.enemies.append(Enemy_2(700, 100))
                            counter=0
                        else:
                            self.enemies.append(Enemy(700, 100))
                            counter=0
                    counter +=1
                            
                    #--- changes ---
                    if not PAUSED:
        
                        self.ship.update()
        
                        for e in self.enemies:
                            e.update()
        
                        self.ship.bullet_detect_collison(self.enemies)
                        
                        for i in range(len(self.enemies)-1, -1, -1):
                            print ("debug: Ship.update: testing bullet ", i)
                            if not self.enemies[i].is_alive:
                                print ("debug: Ship.update: removing bullet ", i)
                                del self.enemies[i]
                        if not self.ship.is_alive:
                            del self.ship
                    #--- draws ---
        
                    self.screen.fill([255, 255, 255])
                    self.screen.blit(BackGround.image, BackGround.rect)
                    self.ship.draw(self.screen)
        
                    for e in self.enemies:
                        e.draw(self.screen)
                        for b in e.shots:
                            if pygame.sprite.collide_circle(b, self.ship):
                                self.ship.health_check()
                                b.is_alive=False
                                del b
                    if PAUSED:
                        self.screen.blit(self.text_paused, self.text_paused_rect)
                        
                    pygame.display.update()
            else:
               self.screen.blit(self.text_end, self.text_end_rect)
               for event in pygame.event.get():
                   if event.type == KEYDOWN:
                       if event.key == K_ESCAPE:
                           RUNNING = False
                           break
                       if event.key == K_SPACE:
                           self.ship.is_alive=True 
                           self.ship.health==3
            pygame.display.update() 
              
        #--- quit ---

        pygame.quit()

#---------------------------------------------------------------------
Game().run()