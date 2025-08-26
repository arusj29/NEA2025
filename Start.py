import pygame

pygame.init()

screenWidth = 800   #Holds the value for the width of the screen
screenHeight = 600  #Holds the value for the height of the screen

screen = pygame.display.set_mode((screenWidth,screenHeight))

run = True   #
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit() 