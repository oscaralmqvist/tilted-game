import pygame
from pygame.locals import *

class Player:
    def __init__(self):
        self.img = pygame.image.load("resources/player_img.png")
        self.alive = True
        self.x_pos = 20
        self.y_pos = 20

    def tick(self):
        self.x_pos = self.x_pos + 1
