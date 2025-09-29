import pygame
import button
import random
import time
import cell
#Initialise pygame modules
pygame.init()

#Game window dimensions
screenWidth = 800   #Holds the value for the width of the screen
screenHeight = 600  #Holds the value for the height of the screen

#Create game window surface
screen = pygame.display.set_mode((screenWidth,screenHeight))  

#Test window dimensions
actualWidth,actualHeight = screen.get_size()  #Returns the dimensions of the surface and assigns it to the variables
print(actualWidth,actualHeight)

#Font definitions
font = pygame.font.SysFont("Roboto",60) #Sets the font as Roboto and size 60

#Colour definitions
black = (0,0,0)
white = (255,255,255)
blue = (5,25,245)

#Create empty string
userText = ""

#Game variables
menuState = "main"   #Holds which menu is being accessed
theme = "light" #Stores the selected theme
textColour = black #Sets the text colour as black
backgrdColour = white #Used to store the colour for the background
#Dimensions of the maze to be generated
mazeWidth = 50 
mazeHeight = 50
cellSize = 20

#Load and assign the button images to the corresponding variables
startImg = pygame.image.load('startBtn.png').convert_alpha()
settingsImg = pygame.image.load('settingsBtn.png').convert_alpha()
exitImg = pygame.image.load('exitBtn.png').convert_alpha()

createImg = pygame.image.load('createBtn.png').convert_alpha()
textboxImg = pygame.image.load('textboxBtn.png').convert_alpha()

helpImg = pygame.image.load('helpBtn.png').convert_alpha()
backImg = pygame.image.load('backBtn.png').convert_alpha()

#Button instances
startButton = button.Button(250,200,startImg,1)
settingsButton = button.Button(250,300,settingsImg,1)
exitButton = button.Button(250,400,exitImg,1)

createButton = button.Button(450,150,createImg,1)
widthButton = button.Button(250,140,textboxImg,1)
heightButton = button.Button(250,200,textboxImg,1)

fontsizeButton = button.Button(300,100,textboxImg,1)
themeButton = button.Button(300,200,textboxImg,1)
helpButton = button.Button(250,300,helpImg,0.65)
backButton = button.Button(250,400,backImg,0.65)

#The subroutine prints a line of text with a certain font and colour and at the coordinates(x,y)
#Called to display text on the screen
def drawText(text,font,textCol,x,y):
    txt = font.render(text,True,textCol)
    screen.blit(txt,(x,y))

#User character
#Dimensions of character
characterWidth = 50 
characterHeight = 50 
#Coordinates of character
characterX = 300
characterY = 500
#Determnies which direction the character is moving in both x and y direction
characterXDirection = 0
characterYDirection = 0

#Updates the position of the character according to the user input
def updateCharacterPos():
    global characterX
    global characterY
    global characterXDirection
    global characterYDirection
    #Changes the position of the character based on the user input
    if characterXDirection > 0:
        if characterX<800 - characterWidth:
            characterX += characterXDirection
    if characterXDirection < 0:
        if characterX > 0:
            characterX += characterXDirection
    if characterYDirection > 0:
        if characterY<600 - characterHeight:
            characterY += characterYDirection
    if characterYDirection < 0:
        if characterY > 0:
            characterY += characterYDirection


#Creates the maze grid and returns it
def createGrid():
    grid = []
    for row in range(mazeWidth):
        grid.append([])
        for col in range(mazeHeight):
            grid[row].append(cell(row,col))
        return grid

run = True   #Used to determine whether the game is running
while run:
    #Set a white background
    screen.fill((backgrdColour)) 
    
    #Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False   #Game is not running so window can be closed
        #Handle text input
        if event.type == pygame.TEXTINPUT:
            userText += event.text
        #Handle special keys
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                userText = userText[:-1]
           
            #Changes the direction of the character based on the user input
            if event.key == pygame.K_LEFT:
                characterXDirection = -1
            if event.key == pygame.K_RIGHT:
                characterXDirection = 1
            if event.key == pygame.K_UP:
                characterYDirection = -1
            if event.key == pygame.K_DOWN:
                characterYDirection = 1
            #Keyup
        if event.type == pygame.KEYUP:
            #Stops the character from continuting to move once the key is no longer pressed
            if event.key == pygame.K_LEFT:
                characterXDirection = 0
            if event.key == pygame.K_RIGHT:
                characterXDirection = 0
            if event.key == pygame.K_UP:
                characterYDirection = 0
            if event.key == pygame.K_DOWN:
                characterYDirection = 0
        #Check if menu state is main and if so draw the main menu buttons
        if menuState == "main": 
            pygame.display.set_caption("Start Screen") #Set title of window to start screen
            drawText("ESCAPEROUTE",font,textColour,250,100) #Display name of game at the top of the main menu
        
            startButton.draw(screen)
            settingsButton.draw(screen)
            exitButton.draw(screen)
            if startButton.isClicked(event):
                menuState = "generate"
            if settingsButton.isClicked(event):
                menuState = "settings"
            if exitButton.isClicked(event):
                run = False  #Stop game loop
                
        #Check if menu state is generate and if so draw the maze generation buttons
        if menuState == "generate":
            pygame.display.set_caption("Maze generation") #Set title of window to maze generation
            drawText("Create a maze",font,textColour,250,50) #Display purpose of menu at the top of the  menu
            drawText("Width:",font,textColour,120,140) #Label the width text box
            drawText("Height:",font,textColour,105,200)#Label the height text box
            createButton.draw(screen)
            widthButton.draw(screen)
            heightButton.draw(screen)
           
            #Character
            pygame.draw.rect(screen,blue,[characterX,characterY,characterWidth,characterHeight]) #Display the character on the screen
            updateCharacterPos()
            if createButton.isClicked(event):
                create = True
                if create == True:
                    if mazeWidth == "" or mazeHeight == "":
                        drawText("Can't generate maze, enter width and height first",font,textColour,250,50)
            if widthButton.isClicked(event):
                width = drawText(userText,font,textColour,200,140)
            if heightButton.isClicked(event):
                height = drawText(userText,font,textColour,200,200)
        
        #Check if menu state is settings and if so draw the settings buttons
        if menuState == "settings":
            pygame.display.set_caption("Settings") #Set title of window to settings
            drawText("Settings",font,textColour,300,50) #Display purpose of menu at the top of the  menu
            drawText("Font Size:",font,textColour,95,100)#Label the font size text box
            drawText("Theme:",font,textColour,95,200)#Label the theme text box
            fontsizeButton.draw(screen)
            themeButton.draw(screen)
            helpButton.draw(screen)
            backButton.draw(screen)
            
            if fontsizeButton.isClicked(event):
                textSurface = font.render(userText,True,(255,255,255))
                screen.blit(textSurface,fontsizeButton)
            if themeButton.isClicked(event):
                currentTheme = theme #Assigns the theme before the button was clicked to a variable so that changes can be made
                if currentTheme == "light":
                    theme = "dark" #Changes the theme from light to dark
                if currentTheme == "dark":
                    theme = "light" #Changes the theme from light to dark
            
            if helpButton.isClicked(event):
                print("Help")
                #menuState = "help"
            if backButton.isClicked(event):
                menuState = "main"
        
        if menuState == "help":
            pygame.display.set_caption("Help") #Set title of window to help
            drawText("Help",font,textColour,260,50) #Display purpose of menu at the top of the  menu
        
        if theme == "light":
            textColour = black #Makes the text colour black
            backgrdColour = white #Makes the background colour white
        if theme == "dark":
            textColour = white #Makes the text colour white
            backgrdColour = black #Makes the background colour black
        
        #Update the window
        pygame.display.update()

#Quit pygame when window closed
pygame.quit() 