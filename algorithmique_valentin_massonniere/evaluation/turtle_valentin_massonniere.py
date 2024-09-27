from turtle import * 
import os
import turtle

# forward(120)
# left(90)
# color('red')
# forward(80)

# a=0
# while a<12:
#     a=a+1
#     forward(150)
#     left(150)


def triangle1(a):

    try:
        a = float(a)
        for i in range(3):
            forward(a)
            left(120)
        return
    except ValueError:
        print("Veuillez entrez un nombre")
        return

def triangle2(a):

    right(180)
    for i in range(3):
        forward(a)
        left(120)


def triangle3(a, angle):

    right(angle)
    for i in range(3):
        forward(a)
        left(120)

triangle1("fuehfu")
# triangle2(300)
# triangle3(300, 45)

os.system("pause")