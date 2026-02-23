import pygame
from gameInstance import game as gameVar 

#The subroutine prints a line of text with a certain font and colour and at the coordinates(x,y)
#Called to display text on the screen
def drawText(text,font,textCol,x,y):
    txt = font.render(text,True,textCol)
    gameVar.screen.blit(txt,(x,y))

def textInput(event):
    if event.type == pygame.KEYDOWN and gameVar.menuState == "generate":
        
        
        if gameVar.inputActive == "width":
            if event.key == pygame.K_BACKSPACE:
                gameVar.widthInput = gameVar.widthInput[:-1]
            elif event.unicode.isdigit():
                gameVar.widthInput += event.unicode

        elif gameVar.inputActive == "height":
            if event.key == pygame.K_BACKSPACE:
                gameVar.heightInput = gameVar.heightInput[:-1]
            elif event.unicode.isdigit():
                gameVar.heightInput += event.unicode