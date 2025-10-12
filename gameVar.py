import pygame

class colours:
    #Colour definitions
    black = (0,0,0)
    white = (255,255,255)
    blue = (5,25,245)

class gameVar:
    def __init__(self):
        #Game variables
        self.menuState = "main"   #Holds which menu is being accessed
        self.theme = "light" #Stores the selected theme
        self.textColour = colours.black #Sets the text colour as black
        self.backgrdColour = colours.white #Used to store the colour for the background

        #Font definitions
        self.font = pygame.font.SysFont("Roboto",60) #Sets the font as Roboto and size 60
        
        #Create empty string
        self.userText = ""
        
        #Dimensions of the maze 
        self.mazeWidth = 800 
        self.mazeHeight = 800
        self.cellSize = 40
        self.cols = int(self.mazeWidth/self.cellSize)
        self.rows = int(self.mazeHeight/self.cellSize)

        #User character
        #Dimensions of character
        self.characterWidth = 40 
        self.characterHeight = 40 
        #Coordinates of character
        self.characterX = 0
        self.characterY = 560
        #Determnies which direction the character is moving in both x and y direction
        self.characterXDirection = 0
        self.characterYDirection = 0

    
    def updateTheme(self):
        if self.theme == "light":
            self.textColour = colours.black #Makes the text colour black
            self.backgrdColour = colours.white #Makes the background colour white
        if self.theme == "dark":
            self.textColour = colours.white #Makes the text colour white
            self.backgrdColour = colours.black #Makes the background colour black