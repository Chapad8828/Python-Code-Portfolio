# CTI-110
# P4LAB1a
# Daniel Chapa
# 4/19/2023

# To make the Triangle:
# Honu.forward(100)
# Honu.left(120)
# Honu.forward(100)
# Honu.left(120)
# Honu.forward(100)

# To make the Square:
# Honu.left(90)
# Honu.forward(100)          
# Honu.left(90)      
# Honu .forward(100)
# Honu.left(90)
# Honu.forward(100)
# Honu.left(90)
# Honu.forward(100)

import turtle
wn = turtle.Screen()
wn.bgcolor("tan")      
wn.title("P4LAB1A")      

Honu = turtle.Turtle()
Honu.color("olive")      
Honu.pensize(100)

import turtle
turtle.showturtle()
for x in range(3):
    turtle.forward(100)
    turtle.left(120)

import turtle
turtle.showturtle()
for x in range(4):
    turtle.left(90)
    turtle.forward(100)
