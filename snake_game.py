import pygame
import time
import random


# Set up the game window
pygame.init()
window_width = 800
window_height = 600
game_window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Snake Game')


# Create the snake object
snake_block = 10
snake_speed = 15
snake_list = []

def snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(game_window, pygame.Color('blue'), [x[0], x[1], snake_block, snake_block])

# Define the snake's movements
def game_loop():
    game_window.fill((0, 0, 0))
    game_over = False
    game_close = False
    x1 = window_width / 2
    y1 = window_height / 2
    x1_change = 0
    y1_change = 0
    snake_list = []
    length_of_snake = 1
    foodx = round(random.randrange(0, window_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, window_height - snake_block) / 10.0) * 10.0
    clock = pygame.time.Clock()
    score = 0

    while not game_over:
        while game_close:
            # Handle events when the game is over
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

            # Display game over message
            game_window.fill((0, 0, 0))
            font_style = pygame.font.SysFont(None, 35)
            message = font_style.render(f"You Lost! Your score: {score}. Press Q-Quit or C-Play Again", True, (255, 0, 0))
            game_window.blit(message, [window_width / 6, window_height / 3])

            pygame.display.update()
            time.sleep(2)

        # Handle events during the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # Move the snake
        x1 += x1_change
        y1 += y1_change

        if x1 >= window_width or x1 < 0 or y1 >= window_height or y1 < 0:
            game_close = True

        game_window.fill((0, 0, 0))
        pygame.draw.rect(game_window, (255, 0, 0), [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_list.append(snake_Head)

        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_Head:
                game_close = True

        snake(snake_block, snake_list)
        pygame.display.update()

        # Check if the snake has collided with the food
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, window_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, window_height - snake_block) / 10.0) * 10.0
            length_of_snake += 1
            score+= 10 #Increment the score by 10

        # Set the snake's speed
        pygame.display.set_caption("Snake Game   Score: " + str(score))
        pygame.display.update()
        clock.tick(snake_speed)

    # Quit the game
    pygame.quit()
    quit()


# Start the game
game_loop()
