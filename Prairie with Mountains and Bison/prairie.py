"""
prairie.py
Imports mountains.py and bison.py to create a prairie of random mountains and bison
Created by Khalid Hussain and Elwood Olson
CS 111.01, Professor Jeff Ondich, 10/29/18
"""
from bison import *
from mountains import *
from graphics import *
from random import *

def sun():
    """
    Generates a sun
    """
    sun = Circle(Point(100,100), 10)
    sun.setFill("yellow")
    return sun
def clouds(window):
    """
    Generates a cloud from a set of four circles
    """
    circle1 = Circle(Point(20, 97), 3)
    circle1.setOutline("white")
    circle1.setFill("white")
    circle2 = Circle(Point(24, 97), 3)
    circle2.setOutline("white")
    circle2.setFill("white")
    circle3 = Circle(Point(20, 93), 3)
    circle3.setOutline("white")
    circle3.setFill("white")
    circle4 = Circle(Point(24, 93), 3)
    circle4.setFill("white")
    circle4.setOutline("white")
    circle1.draw(window)
    circle2.draw(window)
    circle3.draw(window)
    circle4.draw(window)
def main():
    """
    Main function to draw mountains and bison, from respective programs, to window
    """
    window = GraphWin("Prairie", 500, 500, autoflush=False)
    window.setCoords(0, 0, 100, 100)
    window.setBackground(color_rgb(135, 206, 250))
    grass = Rectangle(Point(0, 0), Point(100, 25))
    grass.setFill("green")
    grass.setOutline("green")
    grass.draw(window)
    sun().draw(window)
    clouds(window)
    draw_mountains(window)
    print("Hit Ctrl-C to Quit")
    create_bison(window)
    input('Hit Enter to quit')
main()
