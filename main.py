import pygame
import console
import random

# fill board with 1 or 2 given key and who
def playToken(board,key, who, texte):
    if key == pygame.K_KP1:
        if board[2][0] == 0:
            board[2][0] = who
            return True
    if key == pygame.K_KP2:
        if board[2][1] == 0:
            board[2][1] = who
            return True
    if key == pygame.K_KP3:
        if board[2][2]==0:
            board[2][2] = who
            return True
    if key == pygame.K_KP4:
        if board [1][0]==0:
            board[1][0] = who
            return True
    if key == pygame.K_KP5:
        if board[1][1]==0:
            board[1][1] = who
            return True
    if key == pygame.K_KP6:
        if board[1][2]==0:
            board[1][2] = who
            return True
    if key == pygame.K_KP7:
        if board[0][0]==0:
            board[0][0] = who
            return True
    if key == pygame.K_KP8:
        if board[0][1]==0:
            board[0][1] = who
            return True
    if key == pygame.K_KP9:
        if board[0][2]==0:
            board[0][2] = who
            return True
    return False

def updateDisplay(board, rond, croix):
    #dispaly board, easy to improve in a simpler function and for loop
    if board[2][0] == 1:
        screen.blit(rond, (0,300))
    if board[2][1] == 1:
        screen.blit(rond, (150,300))
    if board[2][2] == 1:
        screen.blit(rond, (300,300))
    if board[1][0] == 1:
        screen.blit(rond, (0,150))
    if board[1][1] == 1:
        screen.blit(rond, (150,150))
    if board[1][2] == 1:
        screen.blit(rond, (300,150))
    if board[0][0] == 1:
        screen.blit(rond, (0,0))
    if board[0][1] == 1:
        screen.blit(rond, (150,0))
    if board[0][2] == 1:
        screen.blit(rond, (300,0))
    if board[2][0] == 2:
        screen.blit(croix, (0,300))
    if board[2][1] == 2:
        screen.blit(croix, (150,300))
    if board[2][2] == 2:
        screen.blit(croix, (300,300))
    if board[1][0] == 2:
        screen.blit(croix, (0,150))
    if board[1][1] == 2:
        screen.blit(croix, (150,150))
    if board[1][2] == 2:
        screen.blit(croix, (300,150))
    if board[0][0] == 2:
        screen.blit(croix, (0,0))
    if board[0][1] == 2:
        screen.blit(croix, (150,0))
    if board[0][2] == 2:
        screen.blit(croix, (300,0))

# board is a table of 3 tables
board=[[0,0,0], [0,0,0], [0,0,0]]

pygame.init()

pygame.display.set_caption("morpion")
screen = pygame.display.set_mode((800,400))
running = True
background = pygame.image.load("assets/grille.png")
rond= pygame.image.load("assets/O.png")
croix= pygame.image.load("assets/X.png")
white = ((255,255,255))
screen.fill(white)
pygame.display.flip()
texte = ["Initialization OK!"]
# who start
player = random.randint(1,2)
texte.append("Turn player " + str(player))

runAccueil = True
accueil = pygame.image.load("assets/accueil.png").convert()

while runAccueil:
    screen.blit(accueil, (0,0))
    pygame.display.flip()
    pygame.time.Clock().tick(30)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_KP1:
            runAccueil = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()

while running:
    #le background
    screen.fill(white)
    screen.blit(background, (0,0))

    textTab = console.writeText(texte)
    for i in range(len(textTab)):
        screen.blit(textTab[i], (430, 20 * (i + 1)))
    # display updated board
    updateDisplay(board, rond, croix)


    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            key = event.key
            result = playToken(board,key, player, texte)
            if result:
                if player == 1:
                    player = 2
                else:
                    player= 1
                texte.append("Turn player " + str(player))
            else:
                texte.append("Already occupied!")


    #metre a jour l'ecran
    pygame.display.flip()
