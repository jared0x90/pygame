import pygame

class Game(object):
    def main(self, screen):

        # Load the player sprite
        player = pygame.image.load('images/kain.png')

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

            # Create a backgound color
            screen.fill((200,200,200))

            # Draw the player
            screen.blit(player, (320, 240))

            # Render the new screen
            pygame.display.flip()

# Run the game if we are running this file
if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((640,480))
    pygame.display.set_caption("Ayrscott Games")
    Game().main(screen)