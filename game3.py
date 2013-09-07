import pygame
import random

class Game(object):
    def main(self, screen):
        while True:
            # --------------------------------------------------
            # Event handling
            # --------------------------------------------------

            # Look through the event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return

            # --------------------------------------------------
            # Draw the screen
            # --------------------------------------------------

            # Fill the screen with a random color
            screen.fill((
                random.randint(0,255),
                random.randint(0,255),
                random.randint(0,255)
            ))

            # Render the new screen
            pygame.display.flip()

# Run the game if we are running this file
if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((640,480))
    pygame.display.set_caption("Ayrscott Games")
    Game().main(screen)