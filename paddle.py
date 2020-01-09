import pygame

class Paddle(pygame.sprite.Sprite):

    def __init__(self, main_surface, color, width, height):
        # initialize sprite super class

        # finish setting the class variables to the parameters
        self.main_surface = main_surface

        self.height = height
        self.width = width
        self.color = color
        # Create a surface with the correct height and width
        self.image = pygame.Surface((self.width,self.height))

        # Get the rect coordinates
        self.rect = self.image.get_rect()

        # Fill the surface with the correct color
        self.image.fill(self.color)
    def move(self, pos):
        self.rect.x = pos[0]

