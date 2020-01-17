#Guillermo Porres 1/17/2020 the purpose of this program is the midterm project for intro. computer science and learn how to build a breakout gae with all the knoledged learned in the semester.
import pygame, sys
from pygame.locals import *
import brick
import paddle
import ball

def GAME_OVER(main_surface):
    '''
    this will say game over when the user lose the game
    :param main_surface:
    :return:
    '''
    main_surface.fill((0, 0, 0))
    myFont = pygame.font.SysFont("Helvetica", 50)
    label = myFont.render(" GAME OVER ", 1, ((255, 255, 255)))
    main_surface.blit(label, (100, 275))
    pygame.display.flip()
    while True:# this while true will knwo how to quit the game after the messege appears
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


def GAME_WNNER(main_surface):
    '''
    this will say winner when the user win the game
    :param main_surface:
    :return:
    '''
    main_surface.fill((255, 255, 255))
    myFont = pygame.font.SysFont("Helvetica", 50)
    label = myFont.render(" WINNER ", 1, ((0, 0, 0)))
    main_surface.blit(label, (100, 275))
    pygame.display.flip()
    while True: # this while true will knwo how to quit the game after the messege appears
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


def main():
    pygame.init()
    APPLICATION_WIDTH = 400
    APPLICATION_HEIGHT = 600
    PADDLE_Y_OFFSET = 30
    BRICKS_PER_ROW = 10
    BRICK_SEP = 4
    BRICK_Y_OFFSET = 70
    BRICK_WIDTH =  (APPLICATION_WIDTH - (BRICKS_PER_ROW -1) * BRICK_SEP) / BRICKS_PER_ROW
    BRICK_HEIGHT = 8
    PADDLE_WIDTH = 60
    PADDLE_HEIGHT = 10
    RADIUS_OF_BALL = 10
    NUM_TURNS = 3
    RED = (255, 0, 0)
    ORANGE = (255, 165, 0)
    YELLOW = (255, 255, 0)
    GREEN =(0, 255, 0)
    CYAN = (0, 255, 255)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
      #all the above are parameters to complete the game
    bricks_group = pygame.sprite.Group()  #this will put all the rbicks in the same group
    paddle_group = pygame.sprite.Group()  #this put the paddle to a group
    main_surface = pygame.display.set_mode((APPLICATION_WIDTH, APPLICATION_HEIGHT), 0, 32)
    main_surface.fill((255, 255, 255))
    pg = pygame.image.load("0efac0dc8d72e2e170a7f7c991fecbdf.gif")  #this is the image of the background
    main_surface.blit(pg, (0, 0))
    x_pos = BRICK_SEP
    y_pos = BRICK_Y_OFFSET
    my_paddle = paddle.Paddle(main_surface, (ORANGE), (PADDLE_WIDTH), (PADDLE_HEIGHT) )
    my_paddle.rect.x = 200
    my_paddle.rect.y = APPLICATION_HEIGHT - PADDLE_Y_OFFSET
    main_surface.blit(my_paddle.image, my_paddle.rect)
    paddle_group.add(my_paddle)
    my_ball = ball.Ball((255, 20, 147), APPLICATION_WIDTH, APPLICATION_HEIGHT, RADIUS_OF_BALL)
    my_ball.rect.x = 200
    my_ball.rect.y = 300
    main_surface.blit(my_ball.image, my_ball.rect)
    for x in range(BRICKS_PER_ROW):  #this is the a line of bricks
        my_brick = brick.Brick( (BRICK_WIDTH), (BRICK_HEIGHT), (RED) )
        my_brick.rect.x = x_pos
        my_brick.rect.y = y_pos
        bricks_group.add(my_brick)
        main_surface.blit(my_brick.image, (x_pos, y_pos) )
        x_pos = x_pos+BRICK_SEP+BRICK_WIDTH
    x_pos = BRICK_SEP
    y_pos = y_pos + BRICK_HEIGHT + BRICK_SEP
    for y in range(BRICKS_PER_ROW): #this is the a line of bricks
        my_brick = brick.Brick( (BRICK_WIDTH), (BRICK_HEIGHT), (RED) )
        my_brick.rect.x = x_pos
        my_brick.rect.y = y_pos
        bricks_group.add(my_brick)
        main_surface.blit(my_brick.image, (x_pos, y_pos) )
        x_pos = x_pos + BRICK_SEP + BRICK_WIDTH
    x_pos = BRICK_SEP
    y_pos = y_pos + BRICK_HEIGHT + BRICK_SEP
    for y in range(BRICKS_PER_ROW):  #this is the a line of bricks
        my_brick = brick.Brick( (BRICK_WIDTH), (BRICK_HEIGHT), (ORANGE) )
        my_brick.rect.x = x_pos
        my_brick.rect.y = y_pos
        bricks_group.add(my_brick)
        main_surface.blit(my_brick.image, (x_pos, y_pos) )
        x_pos = x_pos + BRICK_SEP + BRICK_WIDTH
    x_pos = BRICK_SEP
    y_pos = y_pos + BRICK_HEIGHT + BRICK_SEP
    for y in range(BRICKS_PER_ROW):  #this is the a line of bricks
        my_brick = brick.Brick( (BRICK_WIDTH), (BRICK_HEIGHT), (ORANGE) )
        my_brick.rect.x = x_pos
        my_brick.rect.y = y_pos
        bricks_group.add(my_brick)
        main_surface.blit(my_brick.image, (x_pos, y_pos))
        x_pos = x_pos + BRICK_SEP + BRICK_WIDTH
    x_pos = BRICK_SEP
    y_pos = y_pos + BRICK_HEIGHT + BRICK_SEP
    for y in range(BRICKS_PER_ROW):  #this is the a line of bricks
        my_brick = brick.Brick((BRICK_WIDTH), (BRICK_HEIGHT), (YELLOW))
        my_brick.rect.x = x_pos
        my_brick.rect.y = y_pos
        bricks_group.add(my_brick)
        main_surface.blit(my_brick.image, (x_pos, y_pos) )
        x_pos = x_pos + BRICK_SEP + BRICK_WIDTH
    x_pos = BRICK_SEP
    y_pos = y_pos + BRICK_HEIGHT + BRICK_SEP
    for y in range(BRICKS_PER_ROW):  #this is the a line of bricks
        my_brick = brick.Brick( (BRICK_WIDTH), (BRICK_HEIGHT), (YELLOW) )
        my_brick.rect.x = x_pos
        my_brick.rect.y = y_pos
        bricks_group.add(my_brick)
        main_surface.blit(my_brick.image, (x_pos, y_pos) )
        x_pos = x_pos + BRICK_SEP + BRICK_WIDTH
    x_pos = BRICK_SEP
    y_pos = y_pos + BRICK_HEIGHT + BRICK_SEP
    for y in range(BRICKS_PER_ROW):  #this is the a line of bricks
        my_brick = brick.Brick( (BRICK_WIDTH), (BRICK_HEIGHT), (GREEN) )
        my_brick.rect.x = x_pos
        my_brick.rect.y = y_pos
        bricks_group.add(my_brick)
        main_surface.blit(my_brick.image, (x_pos, y_pos))
        x_pos = x_pos + BRICK_SEP + BRICK_WIDTH
    x_pos = BRICK_SEP
    y_pos = y_pos + BRICK_HEIGHT + BRICK_SEP
    for y in range(BRICKS_PER_ROW): #this is the a line of bricks
        my_brick = brick.Brick( (BRICK_WIDTH), (BRICK_HEIGHT), (GREEN) )
        my_brick.rect.x = x_pos
        my_brick.rect.y = y_pos
        bricks_group.add(my_brick)
        main_surface.blit(my_brick.image, (x_pos, y_pos) )
        x_pos = x_pos + BRICK_SEP + BRICK_WIDTH
    x_pos = BRICK_SEP
    y_pos = y_pos + BRICK_HEIGHT + BRICK_SEP
    for y in range(BRICKS_PER_ROW):  #this is the a line of bricks
        my_brick = brick.Brick( (BRICK_WIDTH), (BRICK_HEIGHT), (CYAN) )
        my_brick.rect.x = x_pos
        my_brick.rect.y = y_pos
        bricks_group.add(my_brick)
        main_surface.blit(my_brick.image, (x_pos, y_pos) )
        x_pos = x_pos + BRICK_SEP + BRICK_WIDTH
    x_pos = BRICK_SEP
    y_pos = y_pos + BRICK_HEIGHT + BRICK_SEP
    for y in range(BRICKS_PER_ROW):
        my_brick = brick.Brick( (BRICK_WIDTH), (BRICK_HEIGHT), (CYAN) )
        my_brick.rect.x = x_pos
        my_brick.rect.y = y_pos
        bricks_group.add(my_brick)
        main_surface.blit(my_brick.image, (x_pos, y_pos))
        x_pos = x_pos + BRICK_SEP + BRICK_WIDTH
    while True:  #this while true will know what is gonna happend when the ball collides and when the game is over
        main_surface.fill(WHITE)
        main_surface.blit(pg, (0, 0))
        for a_brick in bricks_group:
            main_surface.blit(a_brick.image, a_brick.rect)
        my_paddle.move(pygame.mouse.get_pos())
        main_surface.blit(my_paddle.image, my_paddle.rect)
        my_ball.move()
        if my_ball.rect.bottom > APPLICATION_HEIGHT:  #this will take out "lifes" out of the game
            NUM_TURNS -= 1
            my_ball.rect.x = 200
            my_ball.rect.y = 300
            main_surface.blit(my_ball.image, my_ball.rect)
        if NUM_TURNS == 0:  #when all the lifes are done the program will show GAME OVER
            GAME_OVER(main_surface)
        if len(bricks_group) == 0:  #when is no more bricks in the game the program will show WINNER
            GAME_WNNER(main_surface)
        main_surface.blit(my_ball.image, my_ball.rect)
        my_ball.paddle_collide(paddle_group)
        my_ball.brick_collide(bricks_group)
        if NUM_TURNS == 0:
            break
        if bricks_group == 0:
            break
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


main()
