import pygame
import random

class Ball:
    def __init__(self, window, windowWidth, windowHeight):
        """ Initialize the ball object. """
        self.window = window
        self.image = pygame.image.load('./images/dvd.png')  # Ensure the correct path
        self.rect = self.image.get_rect()

        # Set movement boundaries
        self.maxWidth = windowWidth - self.rect.width
        self.maxHeight = windowHeight - self.rect.height

        # Random start position
        self.rect.x = random.randint(0, self.maxWidth)
        self.rect.y = random.randint(0, self.maxHeight)

        # Random movement speed (excluding zero)
        speedslist = [-4, -3, -2, -1, 1, 2, 3, 4]
        self.xSpeed = random.choice(speedslist)
        self.ySpeed = random.choice(speedslist)

    def update(self):
        """ Update ball position and bounce on window edges. """
        self.rect.x += self.xSpeed
        self.rect.y += self.ySpeed

        # Bounce off the walls
        if self.rect.x <= 0 or self.rect.x >= self.maxWidth:
            self.xSpeed = -self.xSpeed

        if self.rect.y <= 0 or self.rect.y >= self.maxHeight:
            self.ySpeed = -self.ySpeed

    def draw(self):
        """ Draw the ball in the window. """
        self.window.blit(self.image, self.rect)
