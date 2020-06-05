import pygame

def initConsole():
    font = pygame.font.Font(None, 24)
    text = font.render("Initialization OK",1,(0,0,0))
    return text

def writeText(texte):
    if(len(texte) > 13):
        del(texte[0])
    tabText = []
    for t in texte:
        font = pygame.font.Font(None, 24)
        text = font.render(t,1,(0,0,0))
        tabText.append(text)
    return tabText
