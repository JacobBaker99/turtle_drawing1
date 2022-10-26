#Successfully completed Part 1 of the project
#Also, successfully completed Part 2 of the project. 
#Also, successfully completed Part 3 of the project.

#all imports for code
import turtle
import math
import random

#the main(starter)
def main():
    print("Project 1 by Jacob Baker")
    draw_picture()

#going to perform most code(calls most functions)
def draw_picture():
    window=turtle.Screen()
    jac=turtle.Turtle()
    bak=turtle.Turtle()
    jac.up()
    bak.up()
    bak.goto(-330,330)
    draw_background(bak, "gray", 660)
    perform_boxtrot(jac)
    jac.goto(-225,250)
    draw_first_initial(jac)
    jac.goto(75,-50)
    jac.right(180)
    draw_last_initial(jac)
    window.colormode(255)
    bak.left(90)
    draw_whole_border(bak, 44, 62.23)
    jac.up()
    jac.goto(-374,374)
    draw_line_border(jac)

#the line around the triangles shown on the picture, but not listed in document
def draw_line_border(turtle):
    turtle.pencolor("black")
    turtle.down()
    turtle.right(90)
    turtle.forward(748)
    turtle.left(90)
    turtle.forward(748)
    
    
def draw_filled_square(turtle, size, color):
    turtle.down()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(size)
        turtle.right(90)
    turtle.end_fill()
    turtle.up()

def perform_boxtrot(turtle):
    turtle.goto(-300,300)
    draw_filled_square(turtle, 300, "blue")
    turtle.goto(0,300)
    draw_filled_square(turtle, 300, "green")    
    turtle.goto(0,0)
    draw_filled_square(turtle, 300, "blue")
    turtle.goto(-300,0)
    draw_filled_square(turtle, 300, "green")

def draw_first_initial(turtle):
    turtle.up()
    for i in range(15):
        astamp=turtle.stamp()
        turtle.forward(10)
    turtle.right(180)
    turtle.forward(75)
    turtle.left(90)
    for i in range (20):
        turtle.forward(10)
        astamp=turtle.stamp()
    turtle.right(90)
    for i in range(6):
        turtle.forward(10)
        astamp=turtle.stamp()
    turtle.up()

def draw_last_initial(turtle):
    turtle.up()
    for i in range (2):
        for i in range(2):
            for i in range (15):
                turtle.forward(10)
                astamp=turtle.stamp()
            turtle.right(90)
            for i in range(10):
                turtle.forward(10)
                astamp=turtle.stamp()
            turtle.right(90)
        turtle.right(90)
        turtle.forward(100)
        turtle.left(90)
    turtle.up()

def draw_background(turtle, color, size):
    turtle.down()
    draw_filled_square(turtle, size, color)
    turtle.up()

#only from bottom corner of triangle
def draw_triangle(turtle, short, hypo):
    turtle.down()
    rgb = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
    turtle.fillcolor(rgb)
    turtle.begin_fill()
    turtle.forward(short)
    turtle.left(90)
    turtle.forward(short)
    turtle.left(135)
    turtle.forward(hypo)
    turtle.left(45)
    turtle.end_fill()
    turtle.up()

def draw_triangle_border_sideTB(turtle, short, hypo):
    for i in range (17):
        draw_triangle(turtle, short, hypo)
        turtle.forward(short)
        turtle.left(90)

def draw_triangle_border_sideRL(turtle, short, hypo):
    for i in range (15):
        draw_triangle(turtle, short, hypo)
        turtle.left(90)
        turtle.forward(short)
    
def draw_whole_border(turtle, short, hypo):
    draw_triangle_border_sideTB(turtle, short, hypo)
    turtle.forward(short)
    turtle.goto(-330,-374)
    draw_triangle_border_sideTB(turtle, short, hypo)
    turtle.goto(374,-330)
    draw_triangle_border_sideRL(turtle, short, hypo)
    turtle.goto(-330,-330)
    draw_triangle_border_sideRL(turtle, short, hypo)
    
main()
