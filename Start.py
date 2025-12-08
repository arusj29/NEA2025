
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
        #gameVar.menuState = "help"
    if backButton.isClicked(event):
        gameVar.menuState = "main"

def helpMenu():
    pygame.display.set_caption("Help") #Set title of window to help
    drawText("Help",gameVar.font,gameVar.textColour,260,50) #Display purpose of menu at the top of the  menu
    drawText("Settings - contains different options to change the user experience.",gameVar.font,gameVar.textColour,0,70)
    drawText("Theme-There are light and dark themes which can be selected by clicking the theme button.The default theme is light.",gameVar.font,gameVar.textColour,0,100)


    

#Creates the maze grid and returns it
def createGrid():
    grid = [] #Initialise empty grid
    #Iterates through each row position in the grid
    for row in range (gameVar.rows):
        grid.append([]) #Adds a new empty row to the grid
        #Iterates through each column position in the current row
        for col in range (gameVar.cols):
            grid[row].append(cell.Cell(col,row,gameVar.cellSize,gameVar.rows,gameVar.cols)) #Adds a new cell to the current row in the grid
    startCell = grid[gameVar.rows - 1][0]
    endCell = grid[0][gameVar.cols - 1]
    startCell.isStart = True
    endCell.isStart = True

    return grid

#Displays the maze grid on the screen
def drawGrid(grid):
    for row in grid:
        for cellObj in row:
            cellObj.draw(screen)

#Generates the maze using the recursive backtracker algorithm
def generateMaze(grid):
    #Initialise stack to hold cells
    stack = []
    #Set start at bottom left
    startRow = len(grid) - 1
    startCol = 0
    startingCell = grid[startRow][startCol]
    #Adds intial cell to stack of visited cells
    startingCell.visited = True
    stack.append(startingCell)

    #Executes while stack is not empty
    while stack:
        #Finds the neighbours of the current cell
        current = stack[-1]
        neighbours = current.getUnvisitedNeighbours(grid)
        #Removes walls of a random adjacent cell
        if neighbours:
            nextCell = random.choice(neighbours)
            current.removeWall(nextCell)
            nextCell.visited =  True
            stack.append(nextCell)
        else:
            stack.pop()
    
    startCell = grid[len(grid)-1][0]
    startCell.walls["bottom"] = False

    endCell = grid[0][len(grid)-1]
    endCell.walls["top"] = False

    

    
def mazeMenu():
    pygame.display.set_caption("Maze menu") #Set title of window to maze menu
    #Ensure maze is only generated once
    if not gameVar.mazeGenerated:
        gameVar.grid = createGrid()
        generateMaze(gameVar.grid)
        gameVar.mazeGenerated = True

    if gameVar.mazeCompleted:
        totalTime = (gameVar.finalTime - gameVar.startTime) / 1000 #Time in seconds
        screen.fill(gameVar.backgrdColour)
        drawText(f"Maze completed in {totalTime:.2f} seconds!",gameVar.font,gameVar.textColour,30,150)
        drawText("Press SPACE to return to main menu",gameVar.font,gameVar.textColour,30,250)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit() 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    resetMaze()
                    gameVar.menuState = "main"

        return
    
    drawGrid(gameVar.grid)
   
    #Character
    pygame.draw.rect(screen,colours.blue,[gameVar.characterX,gameVar.characterY,gameVar.characterWidth,gameVar.characterHeight]) #Display the character on the screen
    #Start and end positions of maze
    pygame.draw.rect(screen,colours.red,(0,screenHeight-gameVar.cellSize,gameVar.cellSize,gameVar.cellSize))
    pygame.draw.rect(screen,colours.green,(screenWidth-gameVar.cellSize,0,gameVar.cellSize,gameVar.cellSize))

    if gameVar.timerStarted :
        gameVar.currentTime = (pygame.time.get_ticks() - gameVar.startTime) / 1000
        showTimer(gameVar.currentTime)
    
    #Check for maze completion
    if (gameVar.characterX == screenWidth - gameVar.cellSize and gameVar.characterY == 0):
        gameVar.timerStarted = False
        gameVar.finalTime = pygame.time.get_ticks()
        gameVar.mazeCompleted = True
   
    pygame.display.update()
    

def resetMaze():
    gameVar.mazeGenerated = False
    gameVar.startTime = 0
    gameVar.finalTime = None
    gameVar.timerStarted = False
    gameVar.currentTime = 0
    gameVar.characterX = 0
    gameVar.characterY = screenHeight - gameVar.cellSize

def showTimer(timeValue):
    drawText(f"Time:{timeValue:.2f}s",gameVar.font,gameVar.textColour,10,10)

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