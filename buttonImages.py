import pygame
import button
import textBox

#Load and assign the button images to the corresponding variables
def imageLoad(fileName):
    return pygame.image.load(fileName)

startImg = imageLoad('Images/startBtn.png')
settingsImg = imageLoad('Images/settingsBtn.png')
exitImg = imageLoad('Images/exitBtn.png')

createImg = imageLoad('Images/createBtn.png')
textboxImg = imageLoad('Images/textboxBtn.png')

helpImg = imageLoad('Images/helpBtn.png')
backImg = imageLoad('Images/backBtn.png')
themeImg = imageLoad('Images/themeBtn.png')

solveImg = imageLoad('Images/solveBtn.png')
DFSImg = imageLoad('Images/DFSBtn.png')
BFSImg = imageLoad('Images/BFSBtn.png')
dijkstraImg = imageLoad('Images/dijkstraBtn.png')
AstarImg = imageLoad('Images/AstarBtn.png')

mazeBackImg = imageLoad('Images/backBtn.png')
helpBackImg = imageLoad('Images/backBtn.png')

resetImg = imageLoad('Images/resetBtn.png')


#Button instances
def buttonInstance(x,y,image,scale):
    return button.Button(x,y,image,scale)

startButton = buttonInstance(250,200,startImg,1)
settingsButton = buttonInstance(250,300,settingsImg,1)
exitButton = buttonInstance(250,400,exitImg,1)

createButton = buttonInstance(450,150,createImg,1)
widthBox = textBox.textBox(250, 140, 150, 40, pygame.font.SysFont("Roboto", 30), (0,0,0), (200,200,200), (0,0,255))
heightBox = textBox.textBox(250, 200, 150, 40, pygame.font.SysFont("Roboto", 30), (0,0,0), (200,200,200), (0,0,255))

fontSizeBox = textBox.textBox(300, 100, 100, 40,pygame.font.SysFont("Roboto", 30),(0,0,0), (200,200,200), (0,0,255))

themeButton = buttonInstance(300, 200, themeImg, 0.4)
helpButton = buttonInstance(250,350,helpImg,0.65)
backButton = buttonInstance(250,400,backImg,0.65)

solveButton = buttonInstance(250,200,solveImg,0.4)
DFSButton = buttonInstance(250,275,DFSImg,0.4)
BFSButton = buttonInstance(250,350,BFSImg,0.4)
dijkstraButton = buttonInstance(250,425,dijkstraImg,0.4)
AstarButton = buttonInstance(250,500,AstarImg,0.4)

resetButton = buttonInstance(580, 550, resetImg, 0.3)

#Back buttons
mazeBackButton = buttonInstance(680, 550, mazeBackImg, 0.3)
helpBackButton = buttonInstance(650, 550, helpBackImg, 0.4)
solveBackButton = buttonInstance(650, 550, backImg, 0.4)
generateBackButton = buttonInstance(250, 550, backImg, 0.65)
