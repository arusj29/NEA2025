import pygame

class colours:
    #Colour definitions
    black = (0,0,0)
    white = (255,255,255)
    blue = (5,25,245)
    red = (255,0,0)
    green = (0,255,0)

class gameVar:
    def __init__(self):
        #Game variables
        
        #Game window dimensions
        self.screenWidth = 800   #Holds the value for the width of the screen
        self.screenHeight = 600  #Holds the value for the height of the screen
        self.screen = None
        self.menuState = "main"   #Holds which menu is being accessed
        self.theme = "light" #Stores the selected theme
        self.textColour = colours.black #Sets the text colour as black
        self.backgrdColour = colours.white #Used to store the colour for the background
        self.startTime = None
        self.mazeCompleted = False

        #Font definitions
        self.font = pygame.font.SysFont("Roboto",60) #Sets the font as Roboto and size 60
        self.helpFont = pygame.font.SysFont("Roboto",40) #Sets the font as Roboto and size 60
        
        #Create empty string
        self.userText = ""
        self.errorMessage = ""
        
        #Dimensions of the maze 
        self.mazeWidth = self.screenWidth 
        self.mazeHeight = self.screenHeight
        self.cellSize = 40
        self.cols = int(self.mazeWidth/self.cellSize)
        self.rows = int(self.mazeHeight/self.cellSize)

        #User character
        #Dimensions of character
        self.characterWidth = self.cellSize 
        self.characterHeight = self.cellSize 
        #Coordinates of character
        self.characterX = 0
        self.characterY = 560
        #Determnies which direction the character is moving in both x and y direction
        self.characterXDirection = 0
        self.characterYDirection = 0

        self.grid = None

        self.mazeGrid = None
        self.mazeGenerated = False

        #Timing
        self.timerStarted = False
        self.startTime = 0
        self.currentTime = 0
        self.finalTime = 0

        #Inputs
        self.inputActive = False
        self.inputText = ""
        self.askMazeSize = True
        self.widthInput = ""
        self.heightInput = ""

        #Algorithms
        self.solutionPath = []
        self.pathIndex = 0
        self.autoSolve = False
        self.solveAlgorithm = None
        self.frameCounter = 0
        self.pathCalculated = False  # Track if path has been calculated

        #Visualization 
        self.visualizationSpeed = 10  # Frames to wait between steps
        self.exploredCells = []  # Track cells explored during pathfinding
        self.currentExploredIndex = 0  # Current position in exploration animation
        self.showingExploration = True 

        # Analytics
        self.totalCellsExplored = 0
        self.pathLength = 0
        self.algorithmTime = 0
        self.efficiency = 0

        # Leaderboard
        self.leaderboard = []  # List of dictionaries storing attempt data
        self.attemptNumber = 0 
        self.attemptSaved = False 
    def updateTheme(self):
        if self.theme == "light":
            self.textColour = colours.black #Makes the text colour black
            self.backgrdColour = colours.white #Makes the background colour white
        if self.theme == "dark":
            self.textColour = colours.white #Makes the text colour white
            self.backgrdColour = colours.black #Makes the background colour black