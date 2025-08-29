import pygame
import button

pygame.init()

screenWidth = 800   #Holds the value for the width of the screen
screenHeight = 600  #Holds the value for the height of the screen

screen = pygame.display.set_mode((screenWidth,screenHeight))
pygame.display.set_caption("Start Screen")

font = pygame.font.SysFont("Roboto",60)
title = font.render("EscapeRoute",0,(0,0,0))

#Button images
startImg = pygame.image.load('startBtn.png').convert_alpha()
settingsImg = pygame.image.load('settingsBtn.png').convert_alpha()
exitImg = pygame.image.load('exitBtn.png').convert_alpha()



#Button instances
startButton = button.Button(250,200,startImg)
settingsButton = button.Button(250,300,settingsImg)
exitButton = button.Button(250,400,exitImg)


run = True   
while run:
    screen.fill((255,255,255)) #White background
    screen.blit(title,(250,100))
    
    if startButton.draw(screen):
        print("Start")
    if settingsButton.draw(screen):
        print("Settings")
    if exitButton.draw(screen):
        run = False
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    

pygame.quit() 



