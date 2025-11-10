
import pygame
from gameVar import colours

class Cell:
    def __init__(self,col,row,cellSize):
        self.col = col #Column where cell is located
        self.row = row #Row where cell is located
        self.cellSize = cellSize #Width and height of cells
        #Tracks the walls of the maze 
        self.walls ={'top':True, 'right':True,'bottom':True, 'left':True} #True indicates wall present
        self.visited = False #Tracks if cell has been visited during maze generation
    
    def draw(self,surface):
        #Convert grid coordinates to screen coordinates for drawing
        x = self.col * self.cellSize
        y = self.row * self.cellSize
        
        #Shows if a cell has been visited
        if self.visited:
            pygame.draw.rect(surface,(50,50,50),(x,y,self.cellSize,self.cellSize))
        
        wallColour = colours.black #Sets wall colour to black
        #Check if the walls exist and if so draw them
        if self.walls['top']:
            pygame.draw.line(surface,wallColour,(x,y),(x+self.cellSize,y),1)
        if self.walls['right']:
            pygame.draw.line(surface,wallColour,(x+self.cellSize,y),(x+self.cellSize,y+self.cellSize),1)
        if self.walls['bottom']:
            pygame.draw.line(surface,wallColour,(x,y+self.cellSize),(x+self.cellSize,y+self.cellSize),1)
        if self.walls['left']:
            pygame.draw.line(surface,wallColour,(x,y),(x,y+self.cellSize),1)

    def getUnvisitedNeighbours(self,grid):
       neighbours = []
       totalRows = len(grid)
       if totalRows>0:
           totalCols = len(grid[0]) 
       else:
           totalCols = 0
        
       directions = [(-1,0),(0,1),(1,0),(0,-1)]
       for rowChange,colChange in directions:
           neigbourRow = self.row + rowChange 
           neigbourCol = self.col + colChange 
           if (0 <= neigbourRow <totalRows and 0 <=neigbourCol <totalCols):
               neighbourCell = grid[neigbourRow][neigbourCol]
               if not neighbourCell.visited:
                   neighbours.append(neighbourCell)
        
       return neighbours
    
    def removeWall(self,adjCell):
        rowDiff = adjCell.row - self.row
        colDiff = adjCell.col - self.col
        
        
        if rowDiff == -1:
            self.walls['top'] = False
            adjCell.walls['bottom'] = False
        elif rowDiff == 1:
            self.walls['bottom'] = False
            adjCell.walls['top'] = False
        elif colDiff == -1:
            self.walls['left'] = False
            adjCell.walls['right'] = False
        elif colDiff == 1:
            self.walls['right'] = False
            adjCell.walls['left'] = False

