# Python drawing application
# Takes a filename from the command line, reads the file
#  and processes the file contents by executing the
#  commands listed in the file.
# The commands will be instructions on what to do draw
#  on the screen

# Sprint - Weekly objectives for fixes and new features
import turtle

WELCOME = "Python Drawing Application"

def draw(t, direction, distance):
    if direction == 'left':
        t.left(distance)
    elif direction == 'forward':
        t.forward(distance)

def initialize_turtle():
    return turtle.Turtle()

def process_draw_steps(t, draw_steps):
    for i in range(len(draw_steps)):
        draw(t, draw_steps[i][0], draw_steps[i][1])

def main():
    print(WELCOME)
    main_turtle = initialize_turtle()

    draw_steps = [
        ['forward', 100]
        , ['left', 90]
        , ['forward', 100]
        , ['left', 45]
        , ['forward', 75]
    ]
    process_draw_steps(main_turtle, draw_steps)
    
    turtle.Screen().exitonclick()

if __name__ == '__main__':
    main()
