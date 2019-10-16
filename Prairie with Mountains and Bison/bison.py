"""
bison.py
Generates a random collection of 2 bison
Created by Khalid Hussain and Elwood Olson
CS 111.01, Professor Jeff Ondich, 10/29/18
"""
from graphics import *
import time
from random import *
class Bison:
    """
    Create a class, Bison, and give it attributes that describe each of its body parts
    and what each of these parts contain
    """
    def __init__(self, window, color):
        self.window = window
        self.Rectangle = Rectangle(Point(95,10), Point(70,25))
        self.Rectangle.draw(window)
        self.Rectangle.setFill(color)
        self.head = Oval(Point(74, 30), Point(60, 12))
        #self.head = Circle(Point(70, 25), 7)
        self.head.draw(window)
        self.head.setFill(color)
        self.backfoot = Polygon(Point(95, 10), Point(91, 0), Point(87, 10))
        self.backfoot.draw(window)
        self.backfoot.setFill(color)
        self.frontfoot = Polygon(Point(78, 10), Point(74, 0), Point(70, 10))
        self.frontfoot.draw(window)
        self.frontfoot.setFill(color)
        self.tail = Polygon(Point(95, 25), Point(97, 22), Point(95, 20))
        self.tail.draw(window)
        self.tail.setFill(color)
    def step(self):
        """
        Moves Bison forward
        """
        dx = -2
        self.Rectangle.move(dx, 0)
        self.head.move(dx, 0)
        self.backfoot.move(dx, 0)
        self.frontfoot.move(dx, 0)
        self.tail.move(dx, 0)
    def get_x(self):
        """
        Returns position of Bison
        """
        self.Center = self.Rectangle.getCenter()
        return self.Center.getX()
    def undraw(self):
        """
        Undraws the Bison
        """
        self.Rectangle.undraw()
        self.head.undraw()
        self.backfoot.undraw()
        self.frontfoot.undraw()
        self.tail.undraw()
    def initialize_bison2(self):
        """
        Pre-positions bison2 part way across the screen to facilitate animation
        """
        dx = -60
        self.Rectangle.move(dx, 0)
        self.head.move(dx, 0)
        self.backfoot.move(dx, 0)
        self.frontfoot.move(dx, 0)
        self.tail.move(dx, 0)
def get_random_color():
    """
    Function to create a randomly generated color for all of the parts within Bison class
    """
    red = randrange(0, 255)
    green = randrange(0, 255)
    blue = randrange(0, 255)
    return color_rgb(red, green, blue)
def create_bison(window):
    """
    Creates and animates Bison objects, using the Bison class
    """
    bison = Bison(window, get_random_color())
    bison2 = Bison(window, get_random_color())
    bison2.initialize_bison2()
    while True:
        if bison.get_x() > -20:
            bison.step()
            if bison2.get_x() > -20:
                bison2.step()
            else:
                bison2.undraw()
                bison2 = Bison(window, get_random_color())
            time.sleep(0.05)
        else:
            if bison2.get_x() > -20:
                bison2.step()
            else:
                bison2.undraw()
                bison2 = Bison(window, get_random_color())
            bison.undraw()
            bison = Bison(window, get_random_color())
        time.sleep(0.05)
        update(30)
    input('Hit Enter to quit')
def main():
    """
    Prototype function to test bison.py
    """
    # First, create a window with a white background.
    window_width = 1000
    window_height = 1000
    window = GraphWin('Test', window_width, window_height, autoflush=False)
    window.setCoords(0, 0, 100, 100)
    window.setBackground(color_rgb(255, 255, 255))
    create_bison(window)
