import pygame
import text
from gameInstance import game as gameVar 
from variables import colours
import buttonImages
import pathFinding
import mazeGeneration
import timer


def mainMenu(event):
    pygame.display.set_caption("Start Screen") #Set title of window to start screen
    text.drawText("ESCAPEROUTE",gameVar.font,gameVar.textColour,250,100) #Display name of game at the top of the main menu
        
    buttonImages.startButton.draw(gameVar.screen)
    buttonImages.settingsButton.draw(gameVar.screen)
    buttonImages.exitButton.draw(gameVar.screen)
    
    if buttonImages.startButton.isClicked(event):
        gameVar.menuState = "generate"
    if buttonImages.settingsButton.isClicked(event):
        gameVar.menuState = "settings"
    if buttonImages.exitButton.isClicked(event):
        gameVar.run = False  #Stop game loop

def generateMenu(event):
    pygame.display.set_caption("Maze generation") #Set title of window to maze generation
    gameVar.screen.fill(gameVar.backgrdColour)
    
    # Clear error when returning to menu
    if gameVar.menuState != "generate":
        gameVar.errorMessage = ""

    text.drawText("Create a maze",gameVar.font,gameVar.textColour,250,50) #Display purpose of menu at the top of the  menu
    text.drawText("Width:",gameVar.font,gameVar.textColour,120,140) #Label the width text box
    text.drawText("Height:",gameVar.font,gameVar.textColour,105,200)#Label the height text box
    text.drawText("Leave blank for default (20x15)", gameVar.helpFont, gameVar.textColour, 100, 250)

    
    buttonImages.createButton.draw(gameVar.screen)
    buttonImages.generateBackButton.draw(gameVar.screen)  # Draw back button
   

    # Handle and draw the textboxes
    buttonImages.widthBox.handle_event(event)
    buttonImages.heightBox.handle_event(event)
    buttonImages.widthBox.draw(gameVar.screen)
    buttonImages.heightBox.draw(gameVar.screen)
    
    if buttonImages.createButton.isClicked(event):
        newWidth = buttonImages.widthBox.getValue()
        newHeight = buttonImages.heightBox.getValue()

        validInput = True
        errorMessage = ""

        if newWidth is None and newHeight is None:
            #Use default settings
            newWidth = gameVar.screenWidth // gameVar.cellSize  
            newHeight = gameVar.screenHeight // gameVar.cellSize  
        elif newWidth is None or newHeight is None:
            errorMessage = "Please enter both width and height or leave both blank for default!"
            validInput = False
        elif newWidth < 2 or newHeight < 2:
            errorMessage = "Width and height must be at least 2!"
            validInput = False
        elif newWidth > 20 or newHeight > 15:
            errorMessage = "Width max is 20, height max is 15!"
            validInput = False

        if validInput:
            gameVar.cols = newWidth
            gameVar.rows = newHeight
            gameVar.mazeWidth = gameVar.mazeWidth * gameVar.cellSize
            gameVar.mazeHeight = gameVar.mazeHeight * gameVar.cellSize
            gameVar.menuState = "solve"
        else: 
            gameVar.errorMessage = errorMessage
    
    # Display error message if there is one
    if  gameVar.errorMessage:
        text.drawText(gameVar.errorMessage, gameVar.helpFont, (255,0,0), 100, 280)

    # Back button returns to main menu
    if buttonImages.generateBackButton.isClicked(event):
        gameVar.menuState = "main"
    
    pygame.display.update() 

def settingsMenu(event):
    pygame.display.set_caption("Settings") #Set title of window to settings
    text.drawText("Settings",gameVar.font,gameVar.textColour,300,50) #Display purpose of menu at the top of the  menu
    text.drawText("Font Size:",gameVar.font,gameVar.textColour,95,100)#Label the font size text box
    text.drawText("Theme:",gameVar.font,gameVar.textColour,95,200)#Label the theme text box
    
    # Show current theme next to label
    text.drawText(f"Current: {gameVar.theme}", gameVar.helpFont, gameVar.textColour, 95, 240)

    # Handle textbox events and draw it
    buttonImages.fontSizeBox.handle_event(event)
    buttonImages.fontSizeBox.draw(gameVar.screen)

    buttonImages.themeButton.draw(gameVar.screen)
    buttonImages.helpButton.draw(gameVar.screen)
    buttonImages.backButton.draw(gameVar.screen)
   
    # Apply font size when enter is pressed
    if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
        newSize = buttonImages.fontSizeBox.getValue()
        if 20 <= newSize <= 100:  #Size limits
            gameVar.font = pygame.font.SysFont("Roboto", newSize)


    if buttonImages.themeButton.isClicked(event):
        if gameVar.theme == "light":
            gameVar.theme = "dark" #Changes the theme from light to dark
        else:
            gameVar.theme = "light" #Changes the theme from light to dark
        gameVar.updateTheme() #Apply the theme changes to the game
    if buttonImages.helpButton.isClicked(event):
        gameVar.menuState = "help"
    if buttonImages.backButton.isClicked(event):
        gameVar.menuState = "main"

def helpMenu():
    pygame.display.set_caption("Help Menu") #Set title of window to help
    #Display title at the top of the menu
    text.drawText("HELP GUIDE",gameVar.font,gameVar.textColour,280,0) 
    #Information provided for the different sections
    #Settings
    text.drawText("Settings Menu:",gameVar.helpFont,gameVar.textColour,0,85)
    text.drawText("Contains different options to change the user experience.",gameVar.helpFont,gameVar.textColour,0,115)
    #Theme
    text.drawText("Theme",gameVar.helpFont,gameVar.textColour,0,170)
    text.drawText("Change between light and dark mode by clicking the theme button.",gameVar.helpFont,gameVar.textColour,0,200)
    text.drawText("The default theme is light.",gameVar.helpFont,gameVar.textColour,0,230)
    #Creating maze
    text.drawText("Creating a maze:",gameVar.helpFont,gameVar.textColour,0,260)
    text.drawText("Click the create button to generate a maze",gameVar.helpFont,gameVar.textColour,0,290)
    #Controls
    text.drawText("Controls:",gameVar.helpFont,gameVar.textColour,0,340)
    text.drawText("Use the arrow keys to move the character through the maze",gameVar.helpFont,gameVar.textColour,0,380)
    #Aim
    text.drawText("Aim:",gameVar.helpFont,gameVar.textColour,0,430)
    text.drawText("Complete the maze by reaching the end position",gameVar.helpFont,gameVar.textColour,0,460)
    #Start and end squares
    pygame.draw.rect(gameVar.screen, colours.red, (70, 495, 25, 25))
    text.drawText("=Start",gameVar.helpFont,gameVar.textColour,105,495)
    pygame.draw.rect(gameVar.screen, colours.green, (250, 495, 25, 25))
    text.drawText("=Finish",gameVar.helpFont,gameVar.textColour,285,495)
    #Draw back button
    buttonImages.helpBackButton.draw(gameVar.screen)
    

def mazeMenu(event):
    pygame.display.set_caption("Maze menu") #Set title of window to maze menu
    #Ensure maze is only generated once
    if not gameVar.mazeGenerated:
        gameVar.grid = mazeGeneration.createGrid()
        mazeGeneration.generateMaze(gameVar.grid)
        mazeGeneration.addLoops(gameVar.grid, loopChance=0.05)  

        gameVar.mazeGenerated = True
        gameVar.solutionPath = []
        
        gameVar.mazeCompleted = False

    if gameVar.autoSolve and not gameVar.solutionPath:
        # Set start cell to bottom left and end cell to top right
        start = gameVar.grid[gameVar.rows - 1][0]
        end = gameVar.grid[0][gameVar.cols - 1]
    
        # Reset character to starting position
        gameVar.characterX = 0
        gameVar.characterY = gameVar.screenHeight - gameVar.cellSize
        
        if gameVar.autoSolve and not gameVar.pathCalculated:

            print(f"Starting {gameVar.solveAlgorithm} algorithm...")
        
            if gameVar.solveAlgorithm == "DFS":
                gameVar.solutionPath = pathFinding.DFS(start, end, gameVar.grid)

            elif gameVar.solveAlgorithm == "BFS":
                gameVar.solutionPath = pathFinding.BFS(start, end, gameVar.grid)

            elif gameVar.solveAlgorithm == "DIJKSTRA":
                gameVar.solutionPath = pathFinding.Dijkstra(start, end, gameVar.grid)

            elif gameVar.solveAlgorithm == "ASTAR":
                gameVar.solutionPath = pathFinding.astar(start, end, gameVar.grid)
        
            print(f"Path found with {len(gameVar.solutionPath)} steps")
            gameVar.pathCalculated = True
            gameVar.pathIndex = 0
            gameVar.frameCounter = 0

    if gameVar.mazeCompleted:
        totalTime = (gameVar.finalTime - gameVar.startTime) / 1000 #Time in seconds
         # Save attempt to leaderboard if not already saved
        if  not gameVar.attemptSaved:
            gameVar.attemptNumber += 1
            attempt = {
            'attempt': gameVar.attemptNumber,
            'time': totalTime,
            }
            gameVar.leaderboard.append(attempt)
            # Sort leaderboard by time
            gameVar.leaderboard.sort(key=lambda x: x['time'])
            gameVar.attemptSaved = True
        
        gameVar.screen.fill(gameVar.backgrdColour)
        
        if totalTime<60:
            text.drawText(f"Maze completed in {totalTime:.2f} seconds!",gameVar.font,gameVar.textColour,30,30)
        else:
             minutes = totalTime // 60
             seconds = totalTime % 60
             text.drawText(f"Maze completed in:{minutes:02}:{seconds:02}",gameVar.font,gameVar.textColour,30,30)

        # Algorithm analytics summary after solving
        if gameVar.solveAlgorithm:
            text.drawText(f"Algorithm: {gameVar.solveAlgorithm}", gameVar.helpFont, gameVar.textColour, 30, 120)
            text.drawText(f"Path length: {gameVar.pathLength} steps", gameVar.helpFont, gameVar.textColour, 30, 165)
            text.drawText(f"Cells explored: {gameVar.totalCellsExplored}", gameVar.helpFont, gameVar.textColour, 30, 210)
            text.drawText(f"Efficiency: {gameVar.efficiency}%", gameVar.helpFont, gameVar.textColour, 30, 255)
            text.drawText(f"Solve time: {gameVar.algorithmTime:.2f}ms", gameVar.helpFont, gameVar.textColour, 30, 300)    
            text.drawText("Press SPACE to return to main menu",gameVar.font,gameVar.textColour,30,370)
            text.drawText("Press R to retry the same maze", gameVar.font, gameVar.textColour, 30, 410)
        else:
            text.drawText("Press SPACE to return to main menu",gameVar.font,gameVar.textColour,30,450)
            text.drawText("Press R to retry the same maze", gameVar.font, gameVar.textColour, 30, 500)
            # Leaderboard
            text.drawText("LEADERBOARD", gameVar.font, gameVar.textColour, 250, 105)

            # Display up to 5 entries
            for i, entry in enumerate(gameVar.leaderboard[:5]):
                y = 145 + i * 35
                timeStr = f"{entry['time']:.2f}s" if entry['time'] < 60 else f"{int(entry['time']//60)}:{entry['time']%60:05.2f}" 
                rowText = f"#{i+1}  Attempt {entry['attempt']}  {timeStr} "
    
                #Highlight current attempt in gold
                colour = (200, 170, 0) if entry['attempt'] == gameVar.attemptNumber else gameVar.textColour
                text.drawText(rowText, gameVar.font, colour, 30, y)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit() 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    mazeGeneration.resetMaze()
                    gameVar.menuState = "main"
                elif event.key == pygame.K_r:
                    # Reset everything except mazeGenerated so same maze is kept
                    gameVar.mazeCompleted = False
                    gameVar.timerStarted = False
                    gameVar.startTime = 0
                    gameVar.finalTime = 0
                    gameVar.currentTime = 0
                    gameVar.characterX = 0
                    gameVar.characterY = gameVar.screenHeight - gameVar.cellSize
                    gameVar.solutionPath = []
                    gameVar.pathIndex = 0
                    gameVar.pathCalculated = False
                    gameVar.autoSolve = False
                    gameVar.attemptSaved = False  # Allow next attempt to be saved
        return
    
    mazeGeneration.drawGrid(gameVar.grid)
    
    # Draw back button
    buttonImages.mazeBackButton.draw(gameVar.screen)

    # Draw reset button
    buttonImages.resetButton.draw(gameVar.screen)
    # Reset character to start of same maze if reset clicked
    if buttonImages.resetButton.isClicked(event):
        gameVar.characterX = 0
        gameVar.characterY = gameVar.screenHeight - gameVar.cellSize
        gameVar.timerStarted = False
        gameVar.startTime = 0
        gameVar.currentTime = 0
        gameVar.solutionPath = []
        gameVar.pathIndex = 0
        gameVar.pathCalculated = False
        gameVar.autoSolve = False

    # Animate solution if autosolving and current analytics
    if gameVar.autoSolve and gameVar.solutionPath:
        pathFinding.followPath()
        pathFinding.drawSolutionPath()

    #Character
    pygame.draw.rect(gameVar.screen,colours.blue,[gameVar.characterX,gameVar.characterY,gameVar.characterWidth,gameVar.characterHeight]) #Display the character on the screen
    
    #Start and end positions of maze
    pygame.draw.rect(gameVar.screen,colours.red,(0,gameVar.screenHeight-gameVar.cellSize,gameVar.cellSize,gameVar.cellSize))
    pygame.draw.rect(gameVar.screen,colours.green,(gameVar.screenWidth-gameVar.cellSize,0,gameVar.cellSize,gameVar.cellSize))

    #Timer
    if gameVar.timerStarted :
        gameVar.currentTime = (pygame.time.get_ticks() - gameVar.startTime) / 1000
        timer.showTimer(gameVar.currentTime)
    
    #Check for maze completion
    if (gameVar.characterX == gameVar.screenWidth - gameVar.cellSize and gameVar.characterY == 0):
        gameVar.finalTime = pygame.time.get_ticks()
        gameVar.mazeCompleted = True
   
    pygame.display.update()

def solveMenu(event):
    pygame.display.set_caption("Solve menu") #Set title of window 
    gameVar.screen.fill(gameVar.backgrdColour)
    
    text.drawText("Select an algorithm or solve the maze",gameVar.font,gameVar.textColour,0,50) #Display purpose of menu at the top of the  menu
    
    buttonImages.solveButton.draw(gameVar.screen)
    buttonImages.DFSButton.draw(gameVar.screen)
    buttonImages.BFSButton.draw(gameVar.screen)
    buttonImages.dijkstraButton.draw(gameVar.screen)
    buttonImages.AstarButton.draw(gameVar.screen)
     # Draw back button
    buttonImages.solveBackButton.draw(gameVar.screen) 

    # Back button goes to generate menu
    if buttonImages.solveBackButton.isClicked(event):
        gameVar.menuState = "generate"

    
    if buttonImages.solveButton.isClicked(event):
        gameVar.autoSolve = False # User will solve manually
        gameVar.solveAlgorithm = None
        gameVar.solutionPath = []
        gameVar.pathIndex = 0
        gameVar.mazeGenerated = False  
        gameVar.pathCalculated = False  # Reset flag
        gameVar.menuState = "maze"

        
    elif buttonImages.DFSButton.isClicked(event):
        gameVar.solveAlgorithm = "DFS"
        gameVar.autoSolve = True
        gameVar.solutionPath = []  
        gameVar.pathIndex = 0
        gameVar.mazeGenerated = False  
        gameVar.pathCalculated = False  # Reset flag
        gameVar.menuState = "maze"
        
    elif buttonImages.BFSButton.isClicked(event):
        gameVar.solveAlgorithm = "BFS"
        gameVar.autoSolve = True
        gameVar.solutionPath = []  
        gameVar.pathIndex = 0
        gameVar.mazeGenerated = False  
        gameVar.pathCalculated = False  # Reset flag
        gameVar.menuState = "maze"
        
    elif buttonImages.dijkstraButton.isClicked(event):
        gameVar.solveAlgorithm = "DIJKSTRA"
        gameVar.autoSolve = True
        gameVar.solutionPath = []  
        gameVar.pathIndex = 0
        gameVar.mazeGenerated = False  
        gameVar.pathCalculated = False  # Reset flag
        gameVar.menuState = "maze"

    elif buttonImages.AstarButton.isClicked(event):
        gameVar.solveAlgorithm = "ASTAR"
        gameVar.autoSolve = True
        gameVar.solutionPath = []  
        gameVar.pathIndex = 0
        gameVar.mazeGenerated = False  
        gameVar.pathCalculated = False  # Reset flag
        gameVar.menuState = "maze"
            
    pygame.display.update()