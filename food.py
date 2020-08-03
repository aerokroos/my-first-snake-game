import pygame, sys, random

class Food():

    def __init__(self, settings, displaysurf):
        self.settings = settings
        self.displaysurf = displaysurf
        self.cell = 10
        self.color = settings.RED

        self.rect = pygame.Rect(0,0,self.cell,self.cell)

    def set_random_location(self):
        self.rect.x = random.randint(0,68)*10 
        self.rect.y = random.randint(0,48)*10
        
    def draw_food(self):
        pygame.draw.rect(self.displaysurf, self.color, self.rect)