import pygame

#Button class
class Button():
    def __init__(self,x,y,image,scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image,(int(width*scale),int(height*scale))) #Change dimensions using scale
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y) 
        
        self.clicked = False  #Used to prevent clicks from carrying over
    
    def draw(self, surface):
        
        surface.blit(self.image,(self.rect.x,self.rect.y))
        

    def isClicked(self,event):
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos): 
            
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if not self.clicked:
                    self.clicked = True #Stop anymore clicks until mouse released
                    action = True
                    
        
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1: #Checks for left click
                self.clicked = False #Allow for clicks when mouse is released
        else:
            self.clicked = False
        return action
            
        

        