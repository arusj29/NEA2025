import pygame

pygame.init()

screenWidth = 800   #Holds the value for the width of the screen
screenHeight = 600  #Holds the value for the height of the screen

screen = pygame.display.set_mode((screenWidth,screenHeight))
pygame.display.set_caption("Start Screen")

font = pygame.font.SysFont("Roboto",60)
title = font.render("EscapeRoute",0,(0,0,0))


run = True   
while run:
    screen.fill((255,255,255)) #White background
    screen.blit(title,(280,100))
    
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    

pygame.quit() 



