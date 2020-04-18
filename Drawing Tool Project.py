"""Kyra Rivest
Python Drawing Tool Project
Mr. Rossetti
jan. 7 2019"""

from graphics import *
from time import sleep

win = GraphWin("Python Drawing", 800,600)
win.setBackground("light gray")

#Shape Menu
label = Text(Point(730,30), "Tools")
label.setStyle("bold")
label.draw(win)

pointRadio = Circle(Point(710,50), 8)
pointRadio.draw(win)
label = Text(Point(745,50), "Points")
label.draw(win)
lineRadio = Circle(Point(710,70), 8)
lineRadio.draw(win)
label = Text(Point(745,70), "Lines")
label.draw(win)
rectRadio = Circle(Point(710,90), 8)
rectRadio.draw(win)
label = Text(Point(750,90), "Rectangles")
label.draw(win)
polygonRadio = Circle(Point(710,110), 8)
polygonRadio.draw(win)
label = Text(Point(745,110), "Polygons")
label.draw(win)
circleRadio = Circle(Point(710,130), 8)
circleRadio.draw(win)
label = Text(Point(745,130), "Circles")
label.draw(win)
ovalRadio = Circle(Point(710,150),8)
ovalRadio.draw(win)
label = Text(Point(745, 150), "Ovals")
label.draw(win)
textRadio = Circle(Point(710, 170), 8)
textRadio.draw(win)
label = Text(Point(745,170),"Text")
label.draw(win)

#Stlye menu
label = Text(Point(750,200), "Style")
label.setStyle("bold")
label.draw(win)

outlineRadio = Circle(Point(710,220),8)
outlineRadio.draw(win)
label = Text(Point(745,220), "Outlined")
label.draw(win)
solidRadio = Circle(Point(710,240),8)
solidRadio.draw(win)
label = Text(Point(745, 240),"Solid")
label.draw(win)

#Colors menu
label = Text(Point(750,290), "Colors")
label.setStyle("bold")
label.draw(win)

blackRadio = Rectangle(Point(700,310), Point(740, 350))
blackRadio.setFill("black")
blackRadio.draw(win)
blueRadio = Rectangle(Point(750, 310), Point(790,350))
blueRadio.setFill("blue")
blueRadio.setOutline("blue")
blueRadio.draw(win)
greenRadio = Rectangle(Point(700,360), Point(740,400))
greenRadio.setFill("green")
greenRadio.setOutline("green")
greenRadio.draw(win)
yellowRadio = Rectangle(Point(750, 360), Point(790,400))
yellowRadio.setFill("yellow")
yellowRadio.setOutline("yellow")
yellowRadio.draw(win)
redRadio = Rectangle(Point(700, 410), Point(740,450))
redRadio.setFill("red")
redRadio.setOutline("red")
redRadio.draw(win)
orangeRadio = Rectangle(Point(750,410), Point(790,450))
orangeRadio.setFill("orange")
orangeRadio.setOutline("orange")
orangeRadio.draw(win)

#done/undo/exit buttons
undoButton = Rectangle(Point(700,470), Point(790,510))
undoButton.setFill("gray")
undoButton.draw(win)
undoText = Text(undoButton.getCenter(), "Undo")
undoText.draw(win)

doneButton = Rectangle(Point(700, 520), Point(790,560))
doneButton.setFill("gray")
doneButton.draw(win)
doneText = Text(doneButton.getCenter(), "Done")
doneText.draw(win)

exitButton = Rectangle(Point(760,10), Point(790,30))
exitButton.setFill("red")
exitButton.draw(win)
exitText = Text(exitButton.getCenter(), "X")
exitText.setTextColor("white")
exitText.draw(win)

#initialize the indicators
color = "black"
tool = "point"
style = "outline"
drawn = []

activeTool = Circle(pointRadio.getCenter(), 5)
activeTool.setFill("black")
activeTool.draw(win)

activeStyle = Circle(outlineRadio.getCenter(), 5)
activeStyle.setFill("black")
activeStyle.draw(win)

activeColor = Circle(blackRadio.getCenter(), 5)
activeColor.setFill("gray")
activeColor.draw(win)

#Functions

#checks if a button is clicked
def buttonclicked(point, button):
    p1 = button.getP1()
    p2 = button.getP2()
    return((point.getX() >= p1.getX())
           and (point.getX()<= p2.getX())
           and (point.getY() >= p1.getY())
           and (point.getY() <= p2.getY()))

#Changes the radio buttons to the correct tool/style/color
def setRadioButton(radioButton,activeRadio, color):
    activeRadio.undraw()
    activeRadio = Circle(radioButton.getCenter(), 5)
    activeRadio.setFill(color)
    activeRadio.draw(win)
    return activeRadio

#fucntion that draws point
def drawPoint(mouseClick):
    click.setFill(color)
    click.draw(win)
    drawn.append(click)

#function that draws line
def drawLine(firstClick,secondClick):
    aLine = Line(firstClick, secondClick)
    aLine.setFill(color)
    drawn.append(aLine)
    click.undraw()
    aLine.draw(win)

#function that draws rectangle    
def drawRectangle(firstClick,secondClick):
    aRect = Rectangle(firstClick, secondClick)
    if style == "solid":
        aRect.setFill(color)
        aRect.setOutline(color)
        click.undraw()
        aRect.draw(win)
        drawn.append(aRect)
    elif style == "outline":
        aRect.setOutline(color)
        click.undraw()
        aRect.draw(win)
        drawn.append(aRect)

#fucntion that draws polygon    
def drawPolygon(mouseClick):
    polygonPoints = []
    polygonPoints.append(mouseClick)
    mouseClick.draw(win)
    
    on = True
    while(on):
        clickPoint = win.getMouse()
        clickPoint.draw(win)
        polygonPoints.append(clickPoint)

        xPoint = clickPoint.getX()
        yPoint = clickPoint.getY()

        if(buttonclicked(clickPoint, undoButton)):
           clickPoint.undraw()
           polygonPoints.remove(clickPoint)

           secondPoint = polygonPoints[len(polygonPoints) - 1]
           secondPoint.undraw()
           polygonPoints.remove(polygonPoints[len(polygonPoints) -1])

        if(buttonclicked(clickPoint, doneButton)):
           clickPoint.undraw()
           polygonPoints.remove(clickPoint)
           for i in polygonPoints:
               i.undraw()
           shape = Polygon(polygonPoints)
           if style == "solid":
               shape.setFill(color)
               shape.setOutline(color)
               shape.draw(win)
               break
           elif style == "outline":
               shape.setOutline(color)
               shape.draw(win)
               break
    drawn.append(shape)
        
#function that draws circle        
def drawCircle(firstClick,secondClick):
    from math import sqrt
    
    x1 = firstClick.getX()
    y1 = firstClick.getY()
    x2 = secondClick.getX()
    y2 = secondClick.getY()

    dis = sqrt(((x2-x1)**2)+((y2-y1)**2))

    aCircle = Circle(firstClick,dis)
    if style =="solid":
        aCircle.setFill(color)
        aCircle.setOutline(color)
        click.undraw()
        aCircle.draw(win)
        drawn.append(aCircle)
    elif style == "outline":
        aCircle.setOutline(color)
        click.undraw()
        aCircle.draw(win)
        drawn.append(aCircle)

#function that draws oval    
def drawOval(firstClick,secondClick):
    aOval = Oval(firstClick,secondClick)
    if style =="solid":
        aOval.setFill(color) 
        aOval.setOutline(color)
        click.undraw()
        aOval.draw(win)
        drawn.append(aOval)
    elif style == "outline": 
        aOval.setOutline(color)
        click.undraw()
        aOval.draw(win)
        drawn.append(aOval)

#function that draws text    
def drawText(mouseClick):
    win2 = GraphWin("Text input", 300,300)
    win2.setBackground("light blue")
    text = Entry(Point(150,150), 24)
    text.draw(win2)
    textMessage = Text(Point(150,75), "Enter your text here: ")
    textMessage.draw(win2)

    button = Rectangle(Point(250,250), Point(280,290))
    button.setFill("gray")
    button.draw(win2)
    buttonMessage = Text(button.getCenter(), "Ok")
    buttonMessage.draw(win2)

    stop = True
    while(stop):
        cPoint = win2.getMouse()
        xPoint = cPoint.getX()
        yPoint = cPoint.getY()
        if(xPoint >= 250 and xPoint <= 280
           and yPoint >= 250 and yPoint <= 290):
            break
    win2.close()
    writing = text.getText()
    textDrawing = Text(mouseClick, writing)
    textDrawing.setTextColor(color)
    textDrawing.draw(win)
    drawn.append(textDrawing)

#function that undraws last shape drawn
def undoShape():
    if len(drawn) != 0:
        shape = drawn[len(drawn) - 1]
        shape.undraw()
        drawn.remove(shape)
    else:
        sorry = Text(Point(350,300), "Sorry, cannot undo because not shapes are drawn")
        sorry.setSize(20)
        sorry.setTextColor("red")
        sorry.draw(win)
        sleep(2)
        sorry.undraw()

#function that exits the progam
def exitProgram():
    win3 = GraphWin("Exit menu", 300,300)
    win3.setBackground("light blue")
    exitText = Text(Point(150,150), "Do you really want to exit \n the program?")
    exitText.draw(win3)

    okButton = Rectangle(Point(150,250), Point(200,280))
    okButton.setFill("gray")
    okButton.draw(win3)
    okText = Text(okButton.getCenter(), "Ok")
    okText.draw(win3)

    canButton = Rectangle(Point(210,250), Point(260,280))
    canButton.setFill("gray")
    canButton.draw(win3)
    canText = Text(canButton.getCenter(), "Cancel")
    canText.draw(win3)

    on = True
    while(on):
        exitClick = win3.getMouse()
        if (buttonclicked(exitClick, okButton)):
            win3.close()
            return True
            break
        elif(buttonclicked(exitClick, canButton)):
            win3.close()
            return False
            break



#main loop of program
while True:
    # code that draws shapes
    click = win.getMouse()
    if click.getX() < 700:
        click.draw(win)
        if tool == "line":
            click2 = win.getMouse()
            drawLine(click, click2)
        elif tool == "point":
            click.undraw()
            drawPoint(click)
        elif tool == "rectangle":
            click2 = win.getMouse()
            drawRectangle(click, click2)
        elif tool == "polygon":
            click.undraw()
            drawPolygon(click)
        elif tool == "circle":
            click2 = win.getMouse()
            drawCircle(click, click2)
        elif tool == "oval":
            click2 = win.getMouse()
            drawOval(click,click2)
        elif tool == "text":
            click.undraw()
            drawText(click)
    else:
    #to change radio buttons

        #code that changes radio buttons for tools
        if(buttonclicked(click, pointRadio)):
            activeTool = setRadioButton(pointRadio, activeTool, "black")
            tool = "point"
        elif(buttonclicked(click, lineRadio)):
           activeTool = setRadioButton(lineRadio, activeTool, "black")
           tool = "line"
        elif(buttonclicked(click, rectRadio)):
            activeTool = setRadioButton(rectRadio, activeTool, "black")
            tool = "rectangle"
        elif(buttonclicked(click, polygonRadio)):
            activeTool = setRadioButton(polygonRadio, activeTool, "black")
            tool = "polygon"
        elif(buttonclicked(click, circleRadio)):
            activeTool = setRadioButton(circleRadio, activeTool, "black")
            tool = "circle"
        elif(buttonclicked(click, ovalRadio)):
            activeTool = setRadioButton(ovalRadio, activeTool, "black")
            tool = "oval"
        elif(buttonclicked(click, textRadio)):
            activeTool = setRadioButton(textRadio, activeTool, "black")
            tool = "text"
        #code that changes radio buttons for styles
        elif(buttonclicked(click, outlineRadio)):
            activeStyle = setRadioButton(outlineRadio, activeStyle, "black")
            style = "outline"
        elif(buttonclicked(click, solidRadio)):
            activeStyle = setRadioButton(solidRadio, activeStyle, "black")
            style = "solid"
        #code that changes radio buttons for Colors
        elif(buttonclicked(click, blackRadio)):
            activeColor = setRadioButton(blackRadio, activeColor, "gray")
            color = "black"
        elif(buttonclicked(click, blueRadio)):
            activeColor = setRadioButton(blueRadio, activeColor, "gray")
            color = "blue"
        elif(buttonclicked(click, greenRadio)):
            activeColor = setRadioButton(greenRadio, activeColor, "gray")
            color = "green"
        elif(buttonclicked(click, yellowRadio)):
            activeColor = setRadioButton(yellowRadio, activeColor, "gray")
            color = "yellow"
        elif(buttonclicked(click, redRadio)):
            activeColor = setRadioButton(redRadio, activeColor, "gray")
            color = "red"
        elif(buttonclicked(click, orangeRadio)):
            activeColor = setRadioButton(orangeRadio, activeColor, "gray")
            color = "orange"
        #if exit/undo buttons are clicked
        elif(buttonclicked(click, exitButton)):
            if exitProgram():
                win.close()
                break
        elif(buttonclicked(click,undoButton)):
            undoShape()
        

