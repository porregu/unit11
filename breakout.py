import pygame, sys
from pygame.locals import *
import brick
import paddle
import ball



def main():
    pygame.init()
    # Constants that will be used in the program
    APPLICATION_WIDTH = 400
    APPLICATION_HEIGHT = 600
    PADDLE_Y_OFFSET = 30
    BRICKS_PER_ROW = 10
    BRICK_SEP = 4  # The space between each brick
    BRICK_Y_OFFSET = 70
    BRICK_WIDTH =  (APPLICATION_WIDTH - (BRICKS_PER_ROW -1) * BRICK_SEP) / BRICKS_PER_ROW
    BRICK_HEIGHT = 8
    PADDLE_WIDTH = 60
    PADDLE_HEIGHT = 10
    RADIUS_OF_BALL = 10
    NUM_TURNS = 3

    # Sets up the colors
    RED = (255, 0, 0)
    ORANGE = (255, 165, 0)
    YELLOW = (255, 255, 0)
    GREEN =(0, 255, 0)
    CYAN = (0, 255, 255)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)



    bricks_group = pygame.sprite.Group()

    paddle_group = pygame.sprite.Group()



    main_surface = pygame.display.set_mode((APPLICATION_WIDTH, APPLICATION_HEIGHT), 0, 32)
    main_surface.fill((255, 255, 255))
    pg =pygame.image.load("DKwmO3_VAAAO9E5.jpg")
    main_surface.blit(pg, (0, 0))
    x_pos = BRICK_SEP
    y_pos = BRICK_Y_OFFSET

    my_paddle = paddle.Paddle(main_surface, (ORANGE), (PADDLE_WIDTH), (PADDLE_HEIGHT))
    my_paddle.rect.x = 200
    my_paddle.rect.y = APPLICATION_HEIGHT - PADDLE_Y_OFFSET
    main_surface.blit(my_paddle.image,my_paddle.rect)
    paddle_group.add(my_paddle)


    my_ball = ball.Ball((BLACK), APPLICATION_WIDTH, APPLICATION_HEIGHT, RADIUS_OF_BALL)
    my_ball.rect.x = 200
    my_ball.rect.y = 300
    main_surface.blit(my_ball.image, my_ball.rect)


    for x in range(BRICKS_PER_ROW):
        my_brick = brick.Brick((BRICK_WIDTH), (BRICK_HEIGHT), (RED))
        my_brick.rect.x = x_pos
        my_brick.rect.y = y_pos
        bricks_group.add(my_brick)
        main_surface.blit(my_brick.image,(x_pos, y_pos))
        x_pos = x_pos+BRICK_SEP+BRICK_WIDTH

    x_pos = BRICK_SEP
    y_pos = y_pos + BRICK_HEIGHT + BRICK_SEP
    for y in range(BRICKS_PER_ROW):
        my_brick = brick.Brick((BRICK_WIDTH), (BRICK_HEIGHT), (RED))
        my_brick.rect.x = x_pos
        my_brick.rect.y = y_pos
        bricks_group.add(my_brick)
        main_surface.blit(my_brick.image,(x_pos, y_pos))
        x_pos = x_pos + BRICK_SEP + BRICK_WIDTH

    x_pos = BRICK_SEP
    y_pos = y_pos + BRICK_HEIGHT + BRICK_SEP

    for y in range(BRICKS_PER_ROW):
        my_brick = brick.Brick((BRICK_WIDTH), (BRICK_HEIGHT), (ORANGE))
        my_brick.rect.x = x_pos
        my_brick.rect.y = y_pos
        bricks_group.add(my_brick)
        main_surface.blit(my_brick.image,(x_pos, y_pos))
        x_pos = x_pos + BRICK_SEP + BRICK_WIDTH

    x_pos = BRICK_SEP
    y_pos = y_pos + BRICK_HEIGHT + BRICK_SEP

    for y in range(BRICKS_PER_ROW):
        my_brick = brick.Brick((BRICK_WIDTH), (BRICK_HEIGHT), (ORANGE))
        my_brick.rect.x = x_pos
        my_brick.rect.y = y_pos
        bricks_group.add(my_brick)
        main_surface.blit(my_brick.image,(x_pos, y_pos))
        x_pos = x_pos + BRICK_SEP + BRICK_WIDTH

    x_pos = BRICK_SEP
    y_pos = y_pos + BRICK_HEIGHT + BRICK_SEP

    for y in range(BRICKS_PER_ROW):
        my_brick = brick.Brick((BRICK_WIDTH), (BRICK_HEIGHT), (YELLOW))
        my_brick.rect.x = x_pos
        my_brick.rect.y = y_pos
        bricks_group.add(my_brick)
        main_surface.blit(my_brick.image,(x_pos, y_pos))
        x_pos = x_pos + BRICK_SEP + BRICK_WIDTH

    x_pos = BRICK_SEP
    y_pos = y_pos + BRICK_HEIGHT + BRICK_SEP

    for y in range(BRICKS_PER_ROW):
        my_brick = brick.Brick((BRICK_WIDTH), (BRICK_HEIGHT), (YELLOW))
        my_brick.rect.x = x_pos
        my_brick.rect.y = y_pos
        bricks_group.add(my_brick)
        main_surface.blit(my_brick.image,(x_pos, y_pos))
        x_pos = x_pos + BRICK_SEP + BRICK_WIDTH

    x_pos = BRICK_SEP
    y_pos = y_pos + BRICK_HEIGHT + BRICK_SEP

    for y in range(BRICKS_PER_ROW):
        my_brick = brick.Brick((BRICK_WIDTH), (BRICK_HEIGHT), (GREEN))
        my_brick.rect.x = x_pos
        my_brick.rect.y = y_pos
        bricks_group.add(my_brick)
        main_surface.blit(my_brick.image,(x_pos, y_pos))
        x_pos = x_pos + BRICK_SEP + BRICK_WIDTH

    x_pos = BRICK_SEP
    y_pos = y_pos + BRICK_HEIGHT + BRICK_SEP

    for y in range(BRICKS_PER_ROW):
        my_brick = brick.Brick((BRICK_WIDTH), (BRICK_HEIGHT), (GREEN))
        my_brick.rect.x = x_pos
        my_brick.rect.y = y_pos
        bricks_group.add(my_brick)
        main_surface.blit(my_brick.image,(x_pos, y_pos))
        x_pos = x_pos + BRICK_SEP + BRICK_WIDTH

    x_pos = BRICK_SEP
    y_pos = y_pos + BRICK_HEIGHT + BRICK_SEP

    for y in range(BRICKS_PER_ROW):
        my_brick = brick.Brick((BRICK_WIDTH), (BRICK_HEIGHT), (CYAN))
        my_brick.rect.x = x_pos
        my_brick.rect.y = y_pos
        bricks_group.add(my_brick)
        main_surface.blit(my_brick.image,(x_pos, y_pos))
        x_pos = x_pos + BRICK_SEP + BRICK_WIDTH

    x_pos = BRICK_SEP
    y_pos = y_pos + BRICK_HEIGHT + BRICK_SEP

    for y in range(BRICKS_PER_ROW):
        my_brick = brick.Brick((BRICK_WIDTH), (BRICK_HEIGHT), (CYAN))
        my_brick.rect.x = x_pos
        my_brick.rect.y = y_pos
        bricks_group.add(my_brick)
        main_surface.blit(my_brick.image,(x_pos, y_pos))
        x_pos = x_pos + BRICK_SEP + BRICK_WIDTH
    # Step 1: Use loops to draw the rows of bricks. The top row of bricks should be 70 pixels away from the top of
    # the screen (BRICK_Y_OFFSET)
    while True:
        main_surface.fill(WHITE)
        main_surface.blit(pg, (0, 0))
        for a_brick in bricks_group:
            main_surface.blit(a_brick.image, a_brick.rect)
        my_paddle.move(pygame.mouse.get_pos())
        main_surface.blit(my_paddle.image,my_paddle.rect)
        my_ball.move()
        if my_ball.rect.bottom > APPLICATION_HEIGHT:
            NUM_TURNS -= 1
            my_ball.rect.x = 200
            my_ball.rect.y = 300
            main_surface.blit(my_ball.image, my_ball.rect)
        if NUM_TURNS == 0:
            main_surface.fill(WHITE)
            myFont = pygame.font.SysFont("Helvetica", 50)
            label = myFont.render("GAME OVER", 1, BLACK)
            main_surface.blit(label, (200, 275))
            pygame.display.update()
            pygame.time.wait(100)
            break
        main_surface.blit(my_ball.image, my_ball.rect)
        my_ball.paddle_collide(paddle_group)
        my_ball.brick_collide(bricks_group)
        if bricks_group == 0:
            break
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


main()
