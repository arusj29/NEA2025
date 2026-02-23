import pygame
from gameInstance import game as gameVar 
import random
import cell

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
            cellObj.draw(gameVar.screen)

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
            random.shuffle(neighbours)
            nextCell = neighbours[0]
            current.removeWall(nextCell)
            nextCell.visited =  True
            stack.append(nextCell)
        else:
            stack.pop()

def resetMaze():
    gameVar.mazeGenerated = False
    gameVar.mazeCompleted = False
    gameVar.startTime = 0
    gameVar.finalTime = None
    gameVar.timerStarted = False
    gameVar.currentTime = 0
    #Reset character position to bottom left corner
    gameVar.characterX = 0 
    gameVar.characterY = gameVar.screenHeight - gameVar.cellSize 
    gameVar.pathCalculated = False 
    gameVar.solutionPath = []  # Clear solution path
    gameVar.leaderboard = []  # Clear leaderboard for new maze
    gameVar.attemptNumber = 0  # Reset attempt number for new maze


#Adds additional loops to the maze by randomly removing extra walls
def addLoops(grid, loopChance=0.05):
    #Iterates through each row and column of the maze
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            cell = grid[row][col]

            if random.random() < loopChance:
                neighbours=[]
                if row>0:
                    neighbours.append(grid[row-1][col])
                if row<len(grid)-1:
                    neighbours.append(grid[row+1][col])
                if col>0:
                    neighbours.append(grid[row][col-1])
                if col<len(grid[0])-1:
                    neighbours.append(grid[row][col+1])
                
                if neighbours:
                    neighbour = random.choice(neighbours)
                    cell.removeWall(neighbour)