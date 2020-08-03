import pygame, sys
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Hello world!")

WHITE = (255, 255, 255)
GREEN = ( 0, 255, 0)
BLUE = ( 0, 0, 255)

score = 0

font_name = pygame.font.match_font('arial')
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, GREEN)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

while True:
    DISPLAYSURF.fill(WHITE)
    draw_text(DISPLAYSURF, str(score), 40, 30,30)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.exit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                score += 5

    pygame.display.update()