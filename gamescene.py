import pygame
from pygame.locals import *
from player import *

class Gamescene:
    def __init__(self):
        self.player = Player()


    def update(self):
        self.player.tick()
