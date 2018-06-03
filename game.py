# inspired by http://pygametutorials.wikidot.com/tutorials-basic

import pygame
from pygame.locals import *
from gamescene import *

class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.gamescene = Gamescene()
        self.size = self.width, self.height = 650, 860

    # initializes all PyGame modules
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True

    # proceeds keypresses, mouse motion
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                self.gamescene.player.x_pos = self.gamescene.player.x_pos + 200
            if event.key == pygame.K_LEFT:
                self.gamescene.player.x_pos = self.gamescene.player.x_pos - 200

    # computes changes in the game world
    def on_loop(self):
        self.gamescene.update()

    # prints graphics
    def on_render(self):
        self._display_surf.fill((255,255,255))
        for u in self.gamescene.units:
            self._display_surf.blit(u.img, (u.x_pos, u.y_pos))

        pygame.display.flip()

    # quits all PyGame modules
    def on_cleanup(self):
        pygame.quit()

    # enters the game loop
    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()

# starts the game
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()
