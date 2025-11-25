import pygame
from gameVar import colours

class Cell():
    def __init__(self,col,row,cellSize,totalRows,totalCols):
        self.col = col #Column where cell is located
        self.row = row #Row where cell is located
        self.cellSize = cellSize #Width and height of cells
        self.totalRows = totalRows
        self.totalCols = totalCols
       
        #Tracks the walls of the maze 
        self.walls ={'top':True, 'right':True,'bottom':True, 'left':True} #True indicates wall present
        self.visited = False #Tracks if cell has been visited during maze generation
        self.isStart = False
        self.isEnd = False

        #Perimeter walls
        if row == 0 :
            self.walls['top'] = True
        if row == self.totalRows - 1 :
            self.walls['bottom'] = True
        if col == 0 :
            self.walls['left'] = True
        if col == self.totalRows -1  :
            self.walls['right'] = True
    
    def draw(self,surface):
        #Convert grid coordinates to screen coordinates for drawing
        x = self.col * self.cellSize
        y = self.row * self.cellSize
        
        #Shows if a cell has been visited
        #if self.visited:
            #pygame.draw.rect(surface,(50,50,50),(x,y,self.cellSize,self.cellSize))

        pygame.draw.rect(surface,colours.white,(x,y,self.cellSize,self.cellSize))
        
        wallColour = colours.black #Sets wall colour to black
        lineWidth = 3 #Sets thickness of lines
        #Check if the walls exist and if so draw them
        if self.walls['top']:
            pygame.draw.line(surface,wallColour,(x,y),(x+self.cellSize,y),lineWidth)
        if self.walls['right']:
            pygame.draw.line(surface,wallColour,(x+self.cellSize,y),(x+self.cellSize,y+self.cellSize),lineWidth)
        if self.walls['bottom']:
            pygame.draw.line(surface,wallColour,(x,y+self.cellSize),(x+self.cellSize,y+self.cellSize),lineWidth)
        if self.walls['left']:
            pygame.draw.line(surface,wallColour,(x,y),(x,y+self.cellSize),lineWidth)

    def getUnvisitedNeighbours(self,grid):
       #Initialise list of neighbours
       neighbours = []
       #Iterates through maze grid
       totalRows = len(grid)
       if totalRows>0:
           totalCols = len(grid[0]) 
       else:
           totalCols = 0
        #Finds neighbours
       directions = [(-1,0),(0,1),(1,0),(0,-1)]
       for rowChange,colChange in directions:
           neigbourRow = self.row + rowChange 
           neigbourCol = self.col + colChange 
           if (0 <= neigbourRow <totalRows and 0 <=neigbourCol <totalCols):
               neighbourCell = grid[neigbourRow][neigbourCol]
               #Adds to list of unvisited neighbours
               if not neighbourCell.visited:
                   neighbours.append(neighbourCell)
       #Returns list of unvisited neighbours
       return neighbours
    
    def removeWall(self,adjCell):
        #Identify position of adjacent cell
        rowDiff = adjCell.row - self.row
        colDiff = adjCell.col - self.col
        
        #Removes walls based on position of adjacent walls
        #Top
        if rowDiff == -1 and self.row > 0:
            self.walls['top'] = False
            adjCell.walls['bottom'] = False
        #Bottom
        elif rowDiff == 1 and self.row < self.totalRows - 1:
            self.walls['bottom'] = False
            adjCell.walls['top'] = False
        #Left
        elif colDiff == -1 and self.col>0:
            self.walls['left'] = False
            adjCell.walls['right'] = False
        #Right
        elif colDiff == 1 and self.col < self.totalCols - 1:
            self.walls['right'] = False
            adjCell.walls['left'] = False

