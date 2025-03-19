from turtle import *
from math import sqrt
def koch_line(a, deep, t):
    if deep==0:
        t.forward(a)
    else:
        for i in [60, -120, 60, 0]:
            koch_line(a/3, deep-1)
            t.left(i)
def koch(a, deep):
    t = Turtle()
    t.speed(0)
    t.penup()
    t.goto(-a/2, sqrt(a**2-(a/2)**2)/2)
    t.pendown()
    for i in range(3):
        koch_line(a, deep, t)
        t.left(-120)
koch(400, 5)
