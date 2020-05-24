import pygame

pygame.init()

pygame.display.set_caption("morpion")
screen = pygame.display.set_mode((450,450))
running = True
background = pygame.image.load("assets/grille.png")
white = ((255,255,255))
screen.fill(white)
pygame.display.flip()

while running:
    #le background
    screen.fill(white)
    screen.blit(background, (25,25))
    #metre a jour l'ecran
    pygame.display.flip()
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
