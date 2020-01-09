import pygame

class Brick(pygame.sprite.Sprite):

    def __init__(self, width, height, color):
        # initialize sprite super class

        # finish setting the class variables to the parameters
        self.width = width
        self.heigth = height
        self.color = color
        # Create a surface with the correct height and width
        self.image = pygame.Surface((self.width,self.heigth))

        # Get the rect coordinates
        self.rect = self.image.get_rect()

        # Fill the surface with the correct color
        self.image.fill(self.color)

