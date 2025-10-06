import pygame

class Cell:
    def __init__(self,col,row,cellSize):
        self.col = col
        self.row = row
        self.cellSize = cellSize
        
        self.walls ={'top':True, 'right':True,'bottom':True, 'left':True}
        self.visited = False
    
    def draw(self,screen):
        x = self.i * self.cellSize
        y = self.j * self.cellSize
        pygame.draw.rect(screen,(0,0,0),(x,y,self.cellSize,self.cellSize,1))
        


