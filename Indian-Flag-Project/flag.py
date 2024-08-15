import turtle
from turtle import *

# Screen setup
screen = turtle.Screen()
screen.title("Independence Day Edition")

# Access the Tkinter window underlying the turtle screen
root = screen.getcanvas().winfo_toplevel()

# Change the screen icon to your custom icon
root.iconbitmap("india-flag-icon.ico")  # Replace "your_icon.ico" with the path to your .ico file


# Turtle setup
t = turtle.Turtle()
t.speed(25)
t.pensize(4)

# Display "Happy Independence Day"
t.penup()
t.goto(-40, 255)
t.color("red")
t.write("Happy Independence Day", font=("Verdana", 20, "normal"), align='center')
t.pendown()

# Move to the starting position for drawing the flag
t.penup()
t.goto(-400, 250)
t.pendown()

# Draw the saffron rectangle
t.color("orange")
t.begin_fill()
t.forward(800)
t.right(90)
t.forward(167)
t.right(90)
t.forward(800)
t.end_fill()

# Draw the white rectangle
t.left(90)
t.color("white")
t.begin_fill()
t.forward(167)
t.end_fill()

# Draw the green rectangle
t.color("green")
t.begin_fill()
t.forward(167)
t.left(90)
t.forward(800)
t.left(90)
t.forward(167)
t.end_fill()

# Draw the big blue circle (Ashoka Chakra)
t.penup()
t.goto(70, 0)
t.pendown()
t.color("navy")
t.begin_fill()
t.circle(70)
t.end_fill()

# Draw the big white circle
t.penup()
t.goto(60, 0)
t.pendown()
t.color("white")
t.begin_fill()
t.circle(60)
t.end_fill()

# Draw the 24 mini blue circles inside the Ashoka Chakra
t.penup()
t.goto(-57, -8)
t.pendown()
t.color("navy")
for i in range(24):
    t.begin_fill()
    t.circle(3)
    t.end_fill()
    t.penup()
    t.forward(15)
    t.right(15)
    t.pendown()

# Draw the small blue circle at the center
t.penup()
t.goto(20, 0)
t.pendown()
t.begin_fill()
t.circle(20)
t.end_fill()

# Draw the 24 spokes inside the Ashoka Chakra
t.penup()
t.goto(0, 0)
t.pendown()
t.pensize(2)
for i in range(24):
    t.forward(60)
    t.backward(60)
    t.left(15)

# Display "Jai Hind 🙏"
t.penup()
t.goto(-40, -280)
t.color("red")
t.write("Jai Hind 🙏", font=("Verdana", 20, "normal"), align='center')

# Finish
t.hideturtle()
turtle.done()
