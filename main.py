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

def get_actions():
    draw_list_tuple = []
    draw_list_tuple.append(('forward', 100))
    draw_list_tuple.append(('left', 90))
    draw_list_tuple.append(('forward', 100))
    draw_list_tuple.append(('left', 90))
    draw_list_tuple.append(('forward', 100))
    draw_list_tuple.append(('left', 45))
    draw_list_tuple.append(('forward', 90))
    draw_list_tuple.append(('left', 45))
    
    # Use this as an example for the challenge
    direction = 'forward'
    distance = 90
    vector = (direction, distance)
    draw_list_tuple.append(vector)

    return draw_list_tuple


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
    main_turtle = initialize_turtle()

    # Tuple - used to store multiple items in a single variable
    draw_list_tuple = get_actions()
    process_draw_list(main_turtle, draw_list_tuple)

    turtle.Screen().exitonclick()

if __name__ == '__main__':
    main()

