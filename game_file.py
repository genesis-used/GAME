import pygame  # importovaná knižnica pygame
from pygame import mixer   # z knižnice pygame importuj modul mixer
pygame.init()   # inicializácia modulu pygame
mixer.init()   # inicializácia modulu mixer

screen = pygame.display.set_mode((750, 750))   # výška + šírka obrazovky
end = False   # pokial end != True, hra nekončí
image = pygame.image.load(r'Images\LANDSCAPE_FOTKA.jpg')  # načítanie obrázku
screen.blit(image, (0, 0))  # poloha obrázku

color = (255, 0, 0)

while not end:   # kým hra beží
    for event in pygame.event.get():   # pre každý event v hre
        if event.type == pygame.QUIT:  # pokial je koniec hry, program sa vypne
            end = True

    pygame.draw.rect(screen, color, pygame.Rect(200, 200, 150, 150))  # nakreslenie štvorca
    pygame.display.flip()  # aby bola vidiet obrazovka

    pygame.display.set_caption('GENESIS: ARCH OF THE SURVIVOR')  # názov hry
    icon = pygame.image.load(r'Images\BILLIE.jpg')  # ikona hry
    pygame.display.set_icon(icon)  # zobrazenie ikony hry

    is_red = True
    if event.type == pygame.KEYDOWN:  # pokial stlačíme klávesu
        if event.key == pygame.K_SPACE:  # konkrétna klávesa = SPACE
            is_red = not is_red
            if is_red:
                color = (255, 0, 0)   # červena
            else:
                color = (0, 0, 255)   # iná farba
