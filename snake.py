import pygame

class Snake():

    def __init__(self, settings, displaysurf):
        self.settings = settings
        self.displaysurf = displaysurf
        self.cell = 10
        self.height = 10
        self.pos = [100,50]
        self.body = [[100,50], [90,50], [80,50], [70,50], [60,50]]
    
    def move_right(self):
        self.pos[0] += 10
    
    def move_left(self):
        self.pos[0] -= 10
    
    def move_up(self):
        self.pos[1] -= 10

    def move_down(self):
        self.pos[1] += 10

    def get_snake_body(self):
        return self.body

    def get_snake_pos(self):
        return self.pos

    def draw_snake(self):
        for pos in self.body:
            pygame.draw.rect(self.displaysurf, self.settings.GREEN,
                pygame.Rect(pos[0], pos[1], self.height, self.height))
    
    