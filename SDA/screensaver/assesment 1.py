import pygame
import sys
from Ball import Ball  # Import the Ball class

# Constants
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FPS = 30

def main():
    """ Main game function. """
    pygame.init()
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("DVD Screensaver")
    clock = pygame.time.Clock()

    # Create Ball object
    oBall = Ball(window, WINDOW_WIDTH, WINDOW_HEIGHT)

    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Update ball position
        oBall.update()

        # Clear screen
        window.fill(BLACK)

        # Draw ball
        oBall.draw()

        # Update display
        pygame.display.update()

        # Control FPS
        clock.tick(FPS)

if __name__ == "__main__":
    main()
