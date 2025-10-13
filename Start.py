import pygame
import button
from gameVar import gameVar,colours
import cell
import random

#Initialise pygame modules
pygame.init()
gameVar = gameVar()

#Game window dimensions
screenWidth = 800   #Holds the value for the width of the screen
screenHeight = 600  #Holds the value for the height of the screen

#Create game window surface
screen = pygame.display.set_mode((screenWidth,screenHeight))  

#Test window dimensions
actualWidth,actualHeight = screen.get_size()  #Returns the dimensions of the surface and assigns it to the variables
print(actualWidth,actualHeight)

#Load and assign the button images to the corresponding variables
def imageLoad(fileName):
    return pygame.image.load(fileName).convert_alpha()

startImg = imageLoad('startBtn.png')
settingsImg = imageLoad('settingsBtn.png')
exitImg = imageLoad('exitBtn.png')

createImg = imageLoad('createBtn.png')
textboxImg = imageLoad('textboxBtn.png')

helpImg = imageLoad('helpBtn.png')
backImg = imageLoad('backBtn.png')

#Button instances
def buttonInstance(x,y,image,scale):
    return button.Button(x,y,image,scale)

startButton = buttonInstance(250,200,startImg,1)
settingsButton = buttonInstance(250,300,settingsImg,1)
exitButton = buttonInstance(250,400,exitImg,1)

createButton = buttonInstance(450,150,createImg,1)
widthButton = buttonInstance(250,140,textboxImg,1)
heightButton = buttonInstance(250,200,textboxImg,1)

fontsizeButton = buttonInstance(300,100,textboxImg,1)
themeButton = buttonInstance(300,200,textboxImg,1)
helpButton = buttonInstance(250,300,helpImg,0.65)
backButton = buttonInstance(250,400,backImg,0.65)

#The subroutine prints a line of text with a certain font and colour and at the coordinates(x,y)
#Called to display text on the screen
def drawText(text,font,textCol,x,y):
    txt = font.render(text,True,textCol)
    screen.blit(txt,(x,y))

def textInput(event):
    #Handle text input
    if event.type == pygame.TEXTINPUT:
        gameVar.userText += event.text
    
    #Handle special keys
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_BACKSPACE:
            gameVar.userText = gameVar.userText[:-1]

def characterMovement(event):
    #Changes the direction of the character based on the user input
    if event.type == pygame.KEYDOWN:
        currentX = gameVar.characterX
        currentY = gameVar.characterY

        if event.key == pygame.K_LEFT:
            newX = currentX - gameVar.cellSize
            if newX >= 0:
                gameVar.characterX = newX
            
        elif event.key == pygame.K_RIGHT:
            newX = currentX + gameVar.cellSize
            if newX <= gameVar.mazeWidth - gameVar.characterWidth:
                gameVar.characterX = newX
        
        elif event.key == pygame.K_UP:
            newY = currentY - gameVar.cellSize
            if newY >= 0:
                gameVar.characterY = newY
        
        elif event.key == pygame.K_DOWN:
            newY = currentY + gameVar.cellSize
            if newY <= gameVar.mazeHeight - gameVar.characterHeight:
                gameVar.characterY = newY
    #Keyup
    if event.type == pygame.KEYUP:
        #Stops the character from continuting to move once the key is no longer pressed
        if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
            gameVar.characterXDirection = 0
        if event.key in (pygame.K_UP, pygame.K_DOWN):
            gameVar.characterYDirection = 0

def mainMenu():
    pygame.display.set_caption("Start Screen") #Set title of window to start screen
    drawText("ESCAPEROUTE",gameVar.font,gameVar.textColour,250,100) #Display name of game at the top of the main menu
        
    startButton.draw(screen)
    settingsButton.draw(screen)
    exitButton.draw(screen)
    if startButton.isClicked(event):
        gameVar.menuState = "generate"
    if settingsButton.isClicked(event):
        gameVar.menuState = "settings"
    if exitButton.isClicked(event):
        gameVar.run = False  #Stop game loop

def generateMenu():
    pygame.display.set_caption("Maze generation") #Set title of window to maze generation
    drawText("Create a maze",gameVar.font,gameVar.textColour,250,50) #Display purpose of menu at the top of the  menu
    drawText("Width:",gameVar.font,gameVar.textColour,120,140) #Label the width text box
    drawText("Height:",gameVar.font,gameVar.textColour,105,200)#Label the height text box
    createButton.draw(screen)
    widthButton.draw(screen)
    heightButton.draw(screen)
    
    if createButton.isClicked(event):
        gameVar.menuState = "maze"
        if widthButton.isClicked(event):
            gameVar.mazeWidth = drawText(gameVar.userText,gameVar.font,gameVar.textColour,200,140)
        if heightButton.isClicked(event):
            gameVar.height = drawText(gameVar.userText,gameVar.font,gameVar.textColour,200,200)

def settingsMenu():
    pygame.display.set_caption("Settings") #Set title of window to settings
    drawText("Settings",gameVar.font,gameVar.textColour,300,50) #Display purpose of menu at the top of the  menu
    drawText("Font Size:",gameVar.font,gameVar.textColour,95,100)#Label the font size text box
    drawText("Theme:",gameVar.font,gameVar.textColour,95,200)#Label the theme text box
    fontsizeButton.draw(screen)
    themeButton.draw(screen)
    helpButton.draw(screen)
    backButton.draw(screen)
   
    if fontsizeButton.isClicked(event):
        textSurface = gameVar.font.render(gameVar.userText,True,(255,255,255))
        screen.blit(textSurface,fontsizeButton)
    if themeButton.isClicked(event):
        currentTheme = gameVar.theme #Assigns the theme before the button was clicked to a variable so that changes can be made
        if currentTheme == "light":
                gameVar.theme = "dark" #Changes the theme from light to dark
        if currentTheme == "dark":
                gameVar.theme = "light" #Changes the theme from light to dark
            
    if helpButton.isClicked(event):
        print("Help")
        #menuState = "help"
    if backButton.isClicked(event):
        gameVar.menuState = "main"

def helpMenu():
    pygame.display.set_caption("Help") #Set title of window to help
    drawText("Help",gameVar.font,gameVar.textColour,260,50) #Display purpose of menu at the top of the  menu

def mazeMenu():
    pygame.display.set_caption("Maze menu") #Set title of window to maze menu
    grid = createGrid()
    drawGrid(grid)
    #Character
    pygame.draw.rect(screen,colours.blue,[gameVar.characterX,gameVar.characterY,gameVar.characterWidth,gameVar.characterHeight]) #Display the character on the screen
    

#Creates the maze grid and returns it
def createGrid():
    grid = [] #Initialise empty grid
    #Iterates through each row position in the grid
    for row in range (gameVar.rows):
        grid.append([]) #Adds a new empty row to the grid
        #Iterates through each column position in the current row
        for col in range (gameVar.cols):
            grid[row].append(cell.Cell(row,col,gameVar.cellSize)) #Adds a new cell to the current row in the grid
    return grid

#Displays the maze grid on the screen
def drawGrid(grid):
    for row in grid:
        for cellObj in row:
            cellObj.draw(screen)

def generateMaze(grid):
    stack = []
    current = grid[0][0]
    current.visited = True
    stack.append(current)

    while stack:
        current = stack[-1]
        neighbours = current.getUnvisitedNeighbours(grid)

        if neighbours:
            nextCell = random.choice(neighbours)
            current.removeWall(nextCell)
            nextCell.visited =  True
            stack.append(nextCell)
        else:
            stack.pop()


run = True   #Used to determine whether the game is running
while run: 
    
    #Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False   #Game is not running so window can be closed
        textInput(event)
        characterMovement(event)
    #Set the background to the chosen colour
    screen.fill((gameVar.backgrdColour))
    
    #Check if menu state is main and if so draw the main menu buttons
    if gameVar.menuState == "main":
        mainMenu()
    #Check if menu state is generate and if so draw the maze generation buttons
    elif gameVar.menuState == "generate":
        generateMenu()
    #Check if menu state is settings and if so draw the settings buttons
    elif gameVar.menuState == "settings":
        settingsMenu()
    elif gameVar.menuState == "help":
        helpMenu()
    elif gameVar.menuState == "maze":
        mazeMenu()
    
        
    #Update the window
    pygame.display.update()

#Quit pygame when window closed
pygame.quit() 