import sys, pygame
from pygame.locals import *
from settings import Settings
from snake import Snake
from food import Food
from scoreboard import Scoreboard

pygame.init()
st = Settings()

fpsClock = pygame.time.Clock()

displaysurf = pygame.display.set_mode((st.WINDOWWIDTH,
    st.WINDOWHEGHT))
pygame.display.set_caption("Snake Game")

def run_game():

    # make food
    food = Food(st, displaysurf)
    food.set_random_location()  
    # Make snake
    snake = Snake(st, displaysurf)
    snake_direction = st.snake_right
    change = snake_direction
    snake_pos = snake.get_snake_pos()
    snake_body = snake.get_snake_body()

    # make scoreboard
    scoreboard = Scoreboard(st, displaysurf)
    
    
    band = True
    while band:

        scoreboard.draw_score()
        displaysurf.fill(st.BLACK)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    change = st.snake_right
                if event.key == pygame.K_LEFT:
                    change = st.snake_left
                if event.key == pygame.K_UP:
                    change = st.snake_up
                if event.key == pygame.K_DOWN:
                    change = st.snake_down

        if change == st.snake_right and snake_direction != st.snake_left:
            snake_direction = st.snake_right
        if change == st.snake_left and snake_direction != st.snake_right:
            snake_direction = st.snake_left
        if change == st.snake_up and snake_direction != st.snake_down:
            snake_direction = st.snake_up
        if change == st.snake_down and snake_direction != st.snake_up:
            snake_direction = st.snake_down  

        # Snake move
        if snake_direction == st.snake_right:
            snake.move_right()      
        if snake_direction == st.snake_left:
            snake.move_left()
        if snake_direction == st.snake_up:
            snake.move_up()
        if snake_direction == st.snake_down:
            snake.move_down()

        
        snake_body.insert(0, list(snake_pos))
        if snake_pos[0] == food.rect.x and snake_pos[1] == food.rect.y:
            food.set_random_location()
            scoreboard.score += 5
            print(scoreboard.score)
        else:
            snake_body.pop()

        #displaysurf.fill(st.BLACK)
        snake.draw_snake()
        food.draw_food()

        if snake_pos[0] >= 700 or snake_pos[0] <= 0:
            band = False
        if snake_pos[1] >= 500 or snake_pos[1] <=0:
            band = False
        
        if snake_pos in snake_body[1:]:
            band = False

        pygame.display.flip()
        #pygame.display.blit()
        fpsClock.tick(st.FPS)




run_game()