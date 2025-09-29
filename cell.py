import pygame

class Cell:
    def __init__(self,row,col):
        self.row = row
        self.col = col
        self.walls ={'top':True, 'right':True,'bottom':True, 'left':True}
        self.visited = False
    def draw(self):
        