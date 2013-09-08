import pygame
import random

class Player(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super(Player, self).__init__(*groups)
        self.image = pygame.image.load('images/kain.png')
        self.rect = pygame.rect.Rect((400, 300), self.image.get_size())
        self.pixels_per_second = 120

    def update(self, partial_seconds, game):
        # Store our position prior to update in case
        # we need to go back to it
        last_position = self.rect.copy()

        # Process keystrokes
        key = pygame.key.get_pressed()
        move_amount = self.pixels_per_second * partial_seconds
        if key[pygame.K_LEFT]:
            self.rect.x -= move_amount
        if key[pygame.K_RIGHT]:
            self.rect.x += move_amount
        if key[pygame.K_UP]:
            self.rect.y -= move_amount
        if key[pygame.K_DOWN]:
            self.rect.y += move_amount

        # If we have run into a wall use our last position
        for cell in pygame.sprite.spritecollide(self, game.walls, False):
            self.rect = last_position

class Game(object):
    def main(self, screen):
        # Create the clock and set framerate
        clock = pygame.time.Clock()
        framerate = 60

        # Load images
        background = pygame.image.load('images/bg.jpg')

        # Create sprites
        # Main sprite group
        sprites = pygame.sprite.Group()
        # Create player and add to main sprite group
        self.player = Player(sprites)
        # Create a group called walls
        self.walls = pygame.sprite.Group()
        block = pygame.image.load('images/block.png')
        for x in xrange(0, 800, 32):
            for y in xrange(0, 600, 32):
                if x in (0, 800-32) or y in (0, 600-32):
                    wall = pygame.sprite.Sprite(self.walls)
                    wall.image = block
                    wall.rect = pygame.rect.Rect((x, y), block.get_size())
        # Add walls to the main sprite group
        sprites.add(self.walls)

        

        #---------------------------------------------------
        # MAIN LOOP
        #---------------------------------------------------
        while True:
            #---------------------------------------------------
            # Handle events, controls, framerate
            #---------------------------------------------------
            # Setup framerate / reduce CPU use, return time in
            # milliseconds since last tick for sprite movement
            dt = clock.tick(framerate)

            # Check the event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return

            # Update sprites using time since last tick
            sprites.update(dt / 1000.0, self)

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