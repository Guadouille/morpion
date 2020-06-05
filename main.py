import pygame

# fill board with 1 or 2 given key and who
def playToken(board,key, who):
    print(key)
    if key == pygame.K_KP1:
        board[2][0] = who
    if key == pygame.K_KP2:
        board[2][1] = who
    if key == pygame.K_KP3:
        board[2][2] = who
    if key == pygame.K_KP4:
        board[1][0] = who
    if key == pygame.K_KP5:
        board[1][1] = who
    if key == pygame.K_KP6:
        board[1][2] = who
    if key == pygame.K_KP7:
        board[0][0] = who
    if key == pygame.K_KP8:
        board[0][1] = who
    if key == pygame.K_KP9:
        board[0][2] = who
    print(board)

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
screen = pygame.display.set_mode((400,400))
running = True
background = pygame.image.load("assets/grille.png")
rond= pygame.image.load("assets/O.png")
croix= pygame.image.load("assets/X.png")
white = ((255,255,255))
screen.fill(white)
pygame.display.flip()

while running:
    #le background
    screen.fill(white)
    screen.blit(background, (0,0))
    # display updated board
    updateDisplay(board, rond, croix)


    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            key = event.key
            playToken(board,key, 1)

    #metre a jour l'ecran
    pygame.display.flip()
