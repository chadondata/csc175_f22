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

def draw(t, direction, distance):
    if direction == 'left':
        t.left(distance)
    elif direction == 'forward':
        t.forward(distance)

def initialize_turtle():
    return turtle.Turtle()

def process_draw_list(t, draw_list):
    for i in range(len(draw_list)):
        draw(t, draw_list[i][0], draw_list[i][1])

def main():
    print(APPLICATION_NAME)
    directions = ['forward', 'left', 'forward', 'left', 'forward']
    distances = [100, 90, 100, 90, 100]
    main_turtle = initialize_turtle()

    draw_list = [
        ['forward', 100]
        , ['left', 90]
        , ['forward', 100]
        , ['left', 90]
        , ['forward', 90]
        , ['left', 45]
        , ['forward', 100]
    ]

    process_draw_list(main_turtle, draw_list)

    # for i in range(len(directions)):
    #    draw(main_turtle, directions[i], distances[i])

    turtle.Screen().exitonclick()

if __name__ == '__main__':
    main()

