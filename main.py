import pygame
from gameInstance import game as gameVar 
import gameMenu
import text
import playerControl
import buttonImages
import mazeGeneration

#Initialise screen
screen = pygame.display.set_mode((gameVar.screenWidth,gameVar.screenHeight))  #Create game window surface
gameVar.screen = screen 

#Test window dimensions
actualWidth,actualHeight = screen.get_size()  #Returns the dimensions of the surface and assigns it to the variables
print(actualWidth,actualHeight)

run = True   #Used to determine whether the game is running
while run: 
    
    #Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False   #Game is not running so window can be closed
         
        # Handle text input events
        if event.type in (pygame.KEYDOWN, pygame.TEXTINPUT):
            text.textInput(event)
        
        # Handle character movement events
        if event.type in (pygame.KEYDOWN, pygame.KEYUP):
            playerControl.characterMovement(event, gameVar)

        # Pass every event to settings menu so textbox receives all keypresses
        if gameVar.menuState == "settings":
            gameMenu.settingsMenu(event)
        
        # Pass every event to settings menu so textbox receives all keypresses
        if gameVar.menuState == "generate":
            gameMenu.generateMenu(event)
            
    #Set the background to the chosen colour
    screen.fill((gameVar.backgrdColour))
    
    #Check if menu state is main and if so draw the main menu buttons
    if gameVar.menuState == "main":
        if event:
            gameMenu.mainMenu(event)
    
    #Check if menu state is generate and if so draw the maze generation buttons
    elif gameVar.menuState == "generate":
        if event:
            gameMenu.generateMenu(event)
    
    #Check if menu state is settings and if so draw the settings buttons
    elif gameVar.menuState == "settings":
        if event:
            gameMenu.settingsMenu(event)

    elif gameVar.menuState == "help":
            gameMenu.helpMenu()
            if buttonImages.helpBackButton.isClicked(event):
                gameVar.menuState = "settings"
    
    elif gameVar.menuState == "solve":
        if event:
            gameMenu.solveMenu(event)
    
    elif gameVar.menuState == "maze":
        # Check back button
        if buttonImages.mazeBackButton.isClicked(event):
            mazeGeneration.resetMaze()
            gameVar.menuState = "solve"
        
       
        gameMenu.mazeMenu(event)
    
    #Update the window
    pygame.display.update()

#Quit pygame when window closed
pygame.quit() 