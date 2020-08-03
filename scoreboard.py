import pygame, sys
from pygame.locals import *

class Scoreboard():

    def __init__(self, settings, displaysurf):
        self.settings = settings
        self.displaysurf = displaysurf
        self.score = 0

        self.font = pygame.font.Font(None, 32)
        self.text_surface = self.font.render(str(self.score), True, 
            settings.WHITE, settings.BLACK)
        self.rect = self.text_surface.get_rect()
        self.rect.midtop

    def draw_score(self):
        self.displaysurf.blit(self.text_surface, self.rect)


    

    