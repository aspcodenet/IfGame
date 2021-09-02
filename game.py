import pygame

pygame.init()

screen = pygame.display.set_mode((800,600))
# Title
pygame.display.set_caption("Python Västerås - the game")
isRunning = True

#Loading image
player = pygame.image.load('athlete.png')

#Specifying the X and Y Coordinate

playerX = 375
playerY = 500
Xchange = 0
Ychange = 0

while(isRunning ==True):
    screen.fill((167,145,55))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                Ychange-=0.5
            if(event.key == pygame.K_DOWN):
                Ychange+=0.5
            if event.key == pygame.K_LEFT:
                Xchange-=0.5
            if event.key == pygame.K_RIGHT:
                Xchange+=0.5
        if event.type == pygame.KEYUP:
# To stop the increase in X change and Ychange
            Ychange=0
            Xchange=0
    playerX+=Xchange
    playerY+=Ychange
    screen.blit(player,(playerX, playerY))
    pygame.display.update()