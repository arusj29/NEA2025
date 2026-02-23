import pygame
from gameInstance import game as gameVar 
import cell


def characterMovement(event,gameVar):
    
    if gameVar.autoSolve:
        return
    
    if event.type == pygame.KEYDOWN:
        if not gameVar.timerStarted:
            gameVar.startTime = pygame.time.get_ticks()
            gameVar.timerStarted = True
        
        currentX = gameVar.characterX
        currentY = gameVar.characterY
        
        #Changes the direction of the character based on the user input
        if event.key == pygame.K_LEFT:
            if validMove(-1,0):
                gameVar.characterX = currentX - gameVar.cellSize
                     
        elif event.key == pygame.K_RIGHT:
            if validMove(1,0):
                gameVar.characterX = currentX + gameVar.cellSize
        
        elif event.key == pygame.K_UP:
            if validMove(0,-1):
                gameVar.characterY = currentY - gameVar.cellSize
        
        elif event.key == pygame.K_DOWN:
            if validMove(0,1):
                gameVar.characterY = currentY + gameVar.cellSize
    #Keyup
    if event.type == pygame.KEYUP:
        #Stops the character from continuting to move once the key is no longer pressed
        if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
            gameVar.characterXDirection = 0
        if event.key in (pygame.K_UP, pygame.K_DOWN):
            gameVar.characterYDirection = 0

def validMove(x,y):
    #Current cell of character
    col = gameVar.characterX // gameVar.cellSize
    row = gameVar.characterY // gameVar.cellSize
    cell = gameVar.grid[row][col]
    #Check walls
    if x == -1:
        return not cell.walls['left']
    if x == 1:
        return not cell.walls['right']
    if y == -1:
        return not cell.walls['top']
    if y == 1:
        return not cell.walls['bottom']
    return False