import pygame
import random
import settings

class Player(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super(Player, self).__init__(*groups)
        self.image = pygame.image.load('images/kain.png')
        self.rect = pygame.rect.Rect((settings.SCREEN_WIDTH / 2, settings.SCREEN_HEIGHT / 2), self.image.get_size())
        self.pixels_per_second = 200
        self.resting = False
        self.dy = 0

    def update(self, dt, game):
        # Store our position prior to update in case
        # we need to go back to it
        last = self.rect.copy()

        # Process keystrokes
        key = pygame.key.get_pressed()
        move_amount = int(self.pixels_per_second * dt)
        if key[pygame.K_LEFT]:
            self.rect.x -= move_amount
        if key[pygame.K_RIGHT]:
            self.rect.x += move_amount

        # Jump / gravity
        if self.resting and key[pygame.K_SPACE]:
            self.dy = settings.JUMP_POWER
        self.dy = min(settings.MAX_FALL_SPEED, self.dy + settings.GRAVITY_RATE)

        self.rect.y += self.dy * dt



        # Check if we ran into a wall
        new = self.rect
        self.resting = False
        for cell in pygame.sprite.spritecollide(self, game.walls, False):
            cell = cell.rect
            if last.right <= cell.left and new.right > cell.left:
                new.right = cell.left
            if last.left >= cell.right and new.left < cell.right:
                new.left = cell.right
            if last.bottom <= cell.top and new.bottom > cell.top:
                # We hit or are on the floor. Therefore we are resting
                self.resting = True
                new.bottom = cell.top
                self.dy = 0
            if last.top >= cell.bottom and new.top < cell.bottom:
                # We hit the ceiling.
                new.top = cell.bottom            
                self.dy = 0

class Game(object):
    def main(self, screen):
        # Create the clock
        clock = pygame.time.Clock()

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
        for x in xrange(0, settings.SCREEN_WIDTH, 32):
            for y in xrange(0, settings.SCREEN_HEIGHT, 32):
                if x in (0, settings.SCREEN_WIDTH-32) or y in (0, settings.SCREEN_HEIGHT-32):
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
            dt = clock.tick(settings.FRAMERATE)

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
    screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
    pygame.display.set_caption("Ayrscott Games")
    Game().main(screen)