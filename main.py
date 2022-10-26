# Python Drawing App
# This program loads drawing instructions
#  from a text file and processes them by
#  drawing on the screen using turtle

# Sprint - weekly development objective
# 

# Get a basic program written that draws lines using
# turtle
import turtle

# Globals and constants
APPLICATION_NAME = "Python Drawing App v1"

def initialize_turtle():
    return turtle.Turtle()

def main():
    print(APPLICATION_NAME)
    main_turtle = initialize_turtle()
    main_turtle.forward(100)
    main_turtle.left(90)
    main_turtle.forward(100)
    turtle.Screen().exitonclick()

if __name__ == '__main__':
    main()

