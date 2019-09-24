from graphics import *

def main():
    win = GraphWin("Traffic Light")
    shape = Rectangle(Point(50, 20), Point(125, 155))
    shape.setOutline("black")
    shape.setFill("white")
    shape.draw(win)
    center = Point(87, 45)
    x = Circle(center, 20)
    x.setOutline("black")
    x.setFill("red")
    x.draw(win)

    center = Point(87,87)
    y = Circle(center, 20)
    y.setOutline("black")
    y.setFill("yellow")
    y.draw(win)

    center = Point(87,129)
    z = Circle(center, 20)
    z.setOutline("black")
    z.setFill("green")
    z.draw(win)

main()
    
