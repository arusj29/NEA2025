import pygame
class textBox:
    def __init__(self,x,y,width,height,font,textColour,boxColour,activeColour):
        self.rect = pygame.Rect(x,y,width,height)
        self.font = font
        self.text = ""
        self.textColour = textColour
        self.boxColour = boxColour
        self.activeColour = activeColour
        self.active = False
    
    def handle_event(self, event):
        # Check for mouse click
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = True
            else:
                self.active = False

        # Keyboard input when active
        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            #Allow digit input
            elif event.unicode.isdigit():
                # Add typed character
                self.text += event.unicode
    
    def draw(self, surface):
        # Draw the box
        if self.active:
            colour = self.activeColour 
        else: 
            colour = self.boxColour
        pygame.draw.rect(surface, colour, self.rect, 2)

        # Render text
        textSurface = self.font.render(self.text, True, self.textColour)
        surface.blit(textSurface, (self.rect.x + 5, self.rect.y + 5))

    def getValue(self):
        if self.text == "":
            return None
        return int(self.text)
