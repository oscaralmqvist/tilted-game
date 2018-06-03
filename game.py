# inspired by http://pygametutorials.wikidot.com/tutorials-basic

import pygame
from pygame.locals import *

class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 650, 860

    # initializes all PyGame modules
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True

    # proceeds keypresses, mouse motion
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    # computes changes in the game world
    def on_loop(self):
        global img_pos
        img_pos = pygame.Rect((100,100), (100,100))
        print("asd")

    # prints graphics
    def on_render(self):
        # load images
        __img = pygame.image.load("resources/test_img.png")
        self._display_surf.fill((255,255,255))
        self._display_surf.blit(__img, img_pos)
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
