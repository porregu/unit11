import pygame, sys

from pygame.locals import *

pygame.init()

main_surface = pygame.display.set_mode((500, 500), 0, 32)  # this est the surface of the window

pygame.display.set_caption(" unit 10 project")  # this is the label of the project that appears on top of the window
main_surface.fill((255, 255, 255))  # set the background color of the window
brick_height = 20  # this is the height of the brick that could be changed without affecting the program
space = 2  # space between the bricks
brick_with = (main_surface.get_width() - space * 3) / 4  # is the with of the brick
x_pos = 5  # space on the x axes between bricks
y_pos = 4  # the position of the y
for x in range(10):  # a loop that repeats until it finish the program making 9 bricks
    pygame.draw.rect(main_surface, (255, 0, 0), (x_pos, y_pos, brick_with, brick_height), 0)  # bricks
    x_pos += space + brick_with


y_pos = y_pos-brick_height-space  # y position of all the bricks cna be modified without affecting the program
x_pos = brick_with + space * 2   # x position of the next set of the bricks
for x in range(10):
    pygame.draw.rect(main_surface, (255, 153, 13), (x_pos, y_pos, brick_with, brick_height), 0)
    x_pos += space + brick_with


y_pos = y_pos-brick_height-space
x_pos = brick_with * 2 + space * 3
for x in range(10):
    pygame.draw.rect(main_surface, (255, 255, 0), (x_pos, y_pos, brick_with, brick_height), 0)
    x_pos += space + brick_with


y_pos = y_pos-brick_height-space
x_pos = brick_with * 3 + space * 4
for x in range(10):
    pygame.draw.rect(main_surface, (0, 255, 0), (x_pos, y_pos, brick_with, brick_height), 0)
    x_pos += space + brick_with


y_pos = y_pos-brick_height-space
x_pos = brick_with * 4 + space * 5
for x in range(10):
    pygame.draw.rect(main_surface, (0, 255, 255), (x_pos, y_pos, brick_with, brick_height), 0)
    x_pos += space + brick_with


while True:  # a while true that repeats unitl the user exit the window
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()