# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 21:06:40 2019

@author: Dat Nguyen
"""

 import turtle

 def draw_square(t, sz):
     """Make turtle t draw a square of sz."""
     for i in range(4):
         t.forward(sz)
         t.left(90)


 wn = turtle.Screen()        # Set up the window and its attributes
 wn.bgcolor("lightgreen")
 wn.title("Alex meets a function")

 alex = turtle.Turtle()      # Create alex
 draw_square(alex, 50)       # Call the function to draw the square
 wn.mainloop()