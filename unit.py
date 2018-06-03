import pygame
from pygame.locals import *
from random import randint

class Unit:
    def __init__(self, img, x_pos, y_pos, x_velocity, y_velocity):
        self.img = img
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.x_velocity = x_velocity
        self.y_velocity = y_velocity

    def tick(self):
        self.y_pos = self.y_pos - self.y_velocity


class Enemy(Unit):
    def __init__(self):
        Unit.__init__(self, pygame.image.load("resources/enemy_img.png"), randint(10,650), randint(20,800), 0, 0.5)



class Player(Unit):
    def __init__(self):
        Unit.__init__(self, pygame.image.load("resources/player_img.png"), 20, 20, 0, 0)
        self.alive = True

    
