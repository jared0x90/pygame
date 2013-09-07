import pygame

# This must be first
pygame.init()

# Create a window of the specified resolution
screen = pygame.display.set_mode((640,480))

# Give our window a title
pygame.display.set_caption("Ayrscott Games")

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            run = False
