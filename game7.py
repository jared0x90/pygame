import pygame
import random

class Game(object):
    def main(self, screen):
        # Create the clock
        clock = pygame.time.Clock()

        # Load the player sprite
        background = pygame.image.load('images/bg.jpg')
        player = pygame.image.load('images/kain.png')

        player_x = 400
        player_y = 300

        framerate = 30

        jump_rate = 5

        while True:
            # --------------------------------------------------
            # Setup framerate / reduce CPU use
            # --------------------------------------------------

            # Pass the maximum framerate
            clock.tick(framerate)

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
            # Update player location
            # --------------------------------------------------
            # Move the player around the screen
            player_x += random.randint(jump_rate * -1, jump_rate)
            player_y += random.randint(jump_rate * -1, jump_rate)

            # --------------------------------------------------
            # Draw the screen
            # --------------------------------------------------
            # Create a backgound color
            screen.blit(background , (0,0))

            # Draw the player
            screen.blit(player, (player_x, player_y))

            # Render the new screen
            pygame.display.flip()

# Run the game if we are running this file
if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption("Ayrscott Games")
    Game().main(screen)