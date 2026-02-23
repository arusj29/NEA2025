import pygame
from gameInstance import game as gameVar 
import cell
from collections import deque
import time

def getCurrentCell():
    col = gameVar.characterX // gameVar.cellSize
    row = gameVar.characterY // gameVar.cellSize
    return gameVar.grid[row][col]

def getNeighbours(cell, grid):
    neighbours = []

    if not cell.walls["top"]:
        neighbours.append(grid[cell.row - 1][cell.col])
    if not cell.walls["bottom"]:
        neighbours.append(grid[cell.row + 1][cell.col])
    if not cell.walls["left"]:
        neighbours.append(grid[cell.row][cell.col - 1])
    if not cell.walls["right"]:
        neighbours.append(grid[cell.row][cell.col + 1])

    return neighbours

def DFS(startCell, endCell, grid):
    stack = []
    visited = set()
    parent = {}
    startTime = time.time()
    # Push start cell onto stack
    stack.append(startCell)
    visited.add(startCell)

    # While stack is not empty
    while len(stack) > 0:
        current = stack.pop()

        # Check if end cell reached
        if current == endCell:
            path = reconstructPath(parent, startCell, endCell)
            # Store analytics
            gameVar.totalCellsExplored = len(visited)
            gameVar.pathLength = len(path)
            gameVar.algorithmTime = (time.time() - startTime) * 1000  # ms
            gameVar.efficiency = round((gameVar.pathLength / gameVar.totalCellsExplored) * 100, 2)
            return path

        # Check neighbours of current cell
        for neighbour in getNeighbours(current, grid):
            if neighbour not in visited:
                visited.add(neighbour)
                parent[neighbour] = current
                stack.append(neighbour)
    # No path found
    return []


def BFS(startCell, endCell, grid):
    # Queue used to explore cells in breadth-first order
    queue = deque()

    # Stores visited cells to prevent revisiting
    visited = set()

    # Stores each cell's parent to reconstruct the path
    parent = {}
    startTime = time.time()
    # Add start cell to queue and visited list
    queue.append(startCell)
    visited.add(startCell)

    # Loop while there are cells left to explore
    while queue:
        current = queue.popleft()

        # Check if the goal has been reached
        if current == endCell:
            path = reconstructPath(parent, startCell, endCell)
            # Store analytics
            gameVar.totalCellsExplored = len(visited)
            gameVar.pathLength = len(path)
            gameVar.algorithmTime = (time.time() - startTime) * 1000  # ms
            gameVar.efficiency = round((gameVar.pathLength / gameVar.totalCellsExplored) * 100, 2)
            return path

        # Get accessible neighbouring cells
        neighbours = getNeighbours(current, grid)

        for cell in neighbours:
            if cell not in visited:
                visited.add(cell)
                parent[cell] = current
                queue.append(cell)

    # If no path exists
    return []

def Dijkstra(startCell, endCell, grid):
    import heapq
    
    counter = 0
    # Priority queue stores tuples of (distance, cell)
    pq = [(0, counter, startCell)]
    
    # Dictionary to store the shortest distance to each cell
    distances = {startCell: 0}
    
    # Dictionary to store parent cells for path reconstruction
    parent = {}
    
    # Set to track visited cells
    visited = set()
    startTime = time.time()

    while pq:
        currentDist, _, current = heapq.heappop(pq)
        
        # Skip if already visited
        if current in visited:
            continue
            
        visited.add(current)
        
        # Check if goal reached
        if current == endCell:
            path = reconstructPath(parent, startCell, endCell)
            # Store analytics
            gameVar.totalCellsExplored = len(visited)
            gameVar.pathLength = len(path)
            gameVar.algorithmTime = (time.time() - startTime) * 1000  # ms
            gameVar.efficiency = round((gameVar.pathLength / gameVar.totalCellsExplored) * 100, 2)
            return path
        
        # Explore neighbors
        neighbours = getNeighbours(current, grid)
        
        for neighbour in neighbours:
            if neighbour not in visited:
                # Edges have weight 1
                newDist = currentDist + 1
                
                # If a shorter path to this neighbor is found
                if neighbour not in distances or newDist < distances[neighbour]:
                    distances[neighbour] = newDist
                    parent[neighbour] = current
                    counter += 1 # Increment counter
                    heapq.heappush(pq, (newDist, counter, neighbour))
    
    # No path found
    return []

def astar(startCell, endCell, grid):
    import heapq
    
    # Heuristic function using manhattan distance
    def heuristic(cell1, cell2):
        return abs(cell1.row - cell2.row) + abs(cell1.col - cell2.col)
    
    counter = 0
    # Priority queue stores tuples of (fScore, cell)
    # fScore = gScore + heuristic
    pq = [(heuristic(startCell, endCell), counter, startCell)]
    
    # gScore = cost from start to current cell
    gScore = {startCell: 0}
    
    # Dictionary to store parent cells for path reconstruction
    parent = {}
    
    # Set to track visited cells
    visited = set()
    startTime = time.time()

    while pq:
        _, _, current = heapq.heappop(pq)
        
        # Skip if already visited
        if current in visited:
            continue
            
        visited.add(current)
        
        # Check if goal reached
        if current == endCell:
            path = reconstructPath(parent, startCell, endCell)
            # Store analytics
            gameVar.totalCellsExplored = len(visited)
            gameVar.pathLength = len(path)
            gameVar.algorithmTime = (time.time() - startTime) * 1000  # ms
            gameVar.efficiency = round((gameVar.pathLength / gameVar.totalCellsExplored) * 100, 2)
            return path
        
        # Explore neighbors
        neighbours = getNeighbours(current, grid)
        
        for neighbour in neighbours:
            if neighbour not in visited:
                # Tentative gScore
                tentativeG = gScore[current] + 1
                
                # If better path found to neighbour
                if neighbour not in gScore or tentativeG < gScore[neighbour]:
                    gScore[neighbour] = tentativeG
                    fScore = tentativeG + heuristic(neighbour, endCell)
                    parent[neighbour] = current
                    counter += 1 # Increment counter to ensure unique entries in the priority queue
                    heapq.heappush(pq, (fScore, counter, neighbour))
    
    # No path found
    return []

def reconstructPath(parent, startCell, endCell):
    path = []
    current = endCell
    while current != startCell:
        path.append(current)
        current = parent[current]
    path.append(startCell)
    path.reverse()
    return path

def followPath():
    if gameVar.pathIndex < len(gameVar.solutionPath):
        # Only advance every N frames for visible animation
        if not hasattr(gameVar, 'frameCounter'):
            gameVar.frameCounter = 0
        
        gameVar.frameCounter += 1
        
        # Advance to next cell every 5 frames (adjust for speed)
        if gameVar.frameCounter >= 30:
            cell = gameVar.solutionPath[gameVar.pathIndex]
            gameVar.characterX = cell.col * gameVar.cellSize
            gameVar.characterY = cell.row * gameVar.cellSize
            gameVar.pathIndex += 1
            gameVar.frameCounter = 0
    else:
        # Mark as complete when path is finished
        if gameVar.autoSolve:
            gameVar.autoSolve = False
            # Check if at the end
            if gameVar.characterX == gameVar.screenWidth - gameVar.cellSize and gameVar.characterY == 0:
                gameVar.finalTime = pygame.time.get_ticks()
                gameVar.mazeCompleted = True
    
#Draw cells that have been explored during pathfinding
def drawExploredCells():
    for i in range(gameVar.currentExploredIndex):
        cell = gameVar.exploredCells[i]
        x = cell.col * gameVar.cellSize
        y = cell.row * gameVar.cellSize
        pygame.draw.rect(gameVar.screen, (173, 216, 230),(x + 5, y + 5, gameVar.cellSize - 10, gameVar.cellSize - 10))
        
def drawSolutionPath():
    for cell in gameVar.solutionPath:
        x = cell.col * gameVar.cellSize
        y = cell.row * gameVar.cellSize
        pygame.draw.rect(gameVar.screen,(200, 200, 0),(x + 10, y + 10, gameVar.cellSize - 20, gameVar.cellSize - 20))