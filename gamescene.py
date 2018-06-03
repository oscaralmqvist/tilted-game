import pygame
from pygame.locals import *
from unit import *


class Gamescene:
    def __init__(self):
        self.player = Player()
        self.units = [self.player]
        self.generate_enemies(15)

    def update(self):
        for u in self.units:
            u.tick()

    def generate_enemies(self,numberOfEnemies):
        for i in range(numberOfEnemies):
            self.units.append(Enemy())
