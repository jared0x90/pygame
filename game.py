import pygame
import random

class Player(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super(Player, self).__init__(*groups)
        self.image = pygame.image.load('images/kain.png')
        self.rect = pygame.rect.Rect((400, 300), self.image.get_size())
        self.move_speed = 5

    def update(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.rect.x -= self.move_speed
        if key[pygame.K_RIGHT]:
            self.rect.x += self.move_speed
        if key[pygame.K_UP]:
            self.rect.y -= self.move_speed
        if key[pygame.K_DOWN]:
            self.rect.y += self.move_speed

class Game(object):
    def main(self, screen):
        # Create the clock
        clock = pygame.time.Clock()

        # Load images
        background = pygame.image.load('images/bg.jpg')

        # Create sprites
        sprites = pygame.sprite.Group()
        self.player = Player(sprites)

        framerate = 30

        #---------------------------------------------------
        # MAIN LOOP
        #---------------------------------------------------
        while True:
            #---------------------------------------------------
            # Handle events, controls, framerate
            #---------------------------------------------------
            # Setup framerate / reduce CPU use
            clock.tick(framerate)

            # Check the event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return

            # Update sprites
            sprites.update()

            #---------------------------------------------------
            # Draw the screen
            #---------------------------------------------------
            # Render the background
            screen.blit(background , (0,0))

            # Draw the sprites
            sprites.draw(screen)

            # Display the new screen
            pygame.display.flip()

# Run the game if we are running this file
if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption("Ayrscott Games")
    Game().main(screen)