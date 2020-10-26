import pygame

pygame.init()

screen = pygame.display.set_mode((750,750))

end = False

while not end:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end = True

    pygame.draw.rect(screen, (0, 128, 50), pygame.Rect(0, 0, 220, 220))

    pygame.display.flip()

    pygame.display.set_caption('GENESIS: ARCH OF THE SURVIVOR')
    icon = pygame.image.load('Images\BILLIE.jpg')
    pygame.display.set_icon(icon)

