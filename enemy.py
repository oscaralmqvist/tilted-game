import pygame
from pygame.locals import *
from player import *

class Enemy:
    def __init__(self):
        self.img = pygame.image.load("resources/enemy_img.png")
        self.x_pos = 20
        self.y_pos = 20;
