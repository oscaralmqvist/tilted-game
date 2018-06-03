import pygame
from pygame.locals import *
from unit import *


class Gamescene:
    def __init__(self):
        self.player = Player()
        self.enemy = Enemy()
        self.units = []
        self.units.append(self.player)
        self.units.append(self.enemy)


    def update(self):
        for u in self.units:
            u.tick()

    #def render(self)
