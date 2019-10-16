"""
mountains.py
Generates a random collection of mountains
Created by Khalid Hussain and Elwood Olson
CS 111.01, Professor Jeff Ondich, 10/29/18
"""

import random
from graphics import *

class Mountain:
    """
    Creates class Mountain, which sets attributes describing each point of a mountain,
    and how each will be colored
    """
    def __init__(self, p1x, p2x, p2y, p3x, p4x, p5x, color):
        self.polygon = Polygon(Point(p1x, 25), Point(p2x, p2y), Point(p3x, 95), Point(p4x, p2y), Point(p5x, 25))
        self.polygon.setFill(color) #randomize shades of gray
        self.polygon.setOutline(color_rgb(255, 255, 255))

    def draw(self, window):
        self.polygon.draw(window)

def get_random_mountain(window_width):
    """
    Randomizes each point for each mountain generated
    """
    color = color_rgb(0, 0, 0)
    base = random.randint(25, 40)
    p1x = random.randint(0, 100 - base)
    p2x = random.randint(p1x, p1x + base // 3)
    p2y = random.randint(60, 95)
    p3x = p1x + base // 2
    p4x = (p1x + base) - (p2x - p1x)
    p5x = p1x + base
    mountain = Mountain(p1x, p2x, p2y, p3x, p4x, p5x, color)
    return mountain

def draw_mountains(window):
    """
    Randomly generates and draws 20 mountains
    """
    for k in range(20):
        mountain = get_random_mountain(100)
        mountain.draw(window)

def main():
    """
    Prototype function to test mountains.py
    """
    window = GraphWin('Mountains', 1000, 1000)
    window.setCoords(0, 0, 100, 100)
    input('Hit Enter to quit')
