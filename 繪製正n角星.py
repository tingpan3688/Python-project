# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 20:22:07 2021

@author: user
"""

import turtle

window = turtle.Screen()
pen = turtle.Turtle()

print("[ for迴圈 繪製正n角星 ]")
n = int( input("n: ") )
d = int( input("d: ") )
length = 100
angle = 180-360*(n-2*d)/(2*n)

for i in range(n) :
    pen.forward(length)
    pen.left(angle)
    
window.exitonclick()
exit()
