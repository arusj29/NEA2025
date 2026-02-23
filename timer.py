from gameInstance import game as gameVar 
import pygame

def showTimer(timeValue):
    timerFont = pygame.font.SysFont("Roboto",28)
    totalSeconds = timeValue
    minutes = totalSeconds // 60
    seconds = totalSeconds % 60

    if timeValue < 60:
        timerText = timerFont.render(f"Time:{timeValue:.2f}s",gameVar.font,gameVar.textColour)
    else:
        timerText = timerFont.render(f"Time:{minutes:02.0f}:{seconds:02.0f}",gameVar.font,gameVar.textColour)
    
    gameVar.screen.blit(timerText,(10, 10))