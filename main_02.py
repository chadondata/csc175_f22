# Python drawing application
# Takes a filename from the command line, reads the file
#  and processes the file contents by executing the
#  commands listed in the file.
# The commands will be instructions on what to do draw
#  on the screen

# Sprint - Weekly objectives for fixes and new features
import turtle

WELCOME = "Python Drawing Application"

    # action_list = [
    #     ('forward', 100)
    #     , ('left', 90)
    #     , ('forward', 100)
    #     , ('left', 45)
    #     , ('forward', 75)
    # ]

def get_actions_prompt():
    action_list = []
    prompt = """
Enter an action from the list below:
    [0] forward
    [1] left
    [2] right
    [q] quit
Your choice:  """

    keep_going = True
    while keep_going:
        response = input(prompt)
        if response == 'q':
            keep_going = False
        else:
            response = int(response)
            if response == 0:
                action = 'forward'
            elif response == 1:
                action = 'left'
            elif response == 2:
                action = 'right'
            else:
                action = 'NA'
            distance = eval(input('Enter a value for the distance: '))
            vector = (action, distance)
            action_list.append(vector)
    
    return action_list

def get_actions():
    action_list = []
    action_list.append(('forward', 100))
    action_list.append(('left', 90))
    action_list.append(('forward', 100))
    action_list.append(('left', 45))
    
    # The following code is a good start for this week's programming challenge
    action = 'forward'
    distance = 75
    vector = (action, distance)
    action_list.append(vector)

    return action_list

def draw(t, direction, distance):
    if direction == 'left':
        t.left(distance)
    elif direction == 'right':
        t.right(distance)
    elif direction == 'forward':
        t.forward(distance)
    else:
        print(f'{direction} not implemented.')

def initialize_turtle():
    return turtle.Turtle()

def process_draw_steps(t, draw_steps):
    for i in range(len(draw_steps)):
        draw(t, draw_steps[i][0], draw_steps[i][1])

def main():
    print(WELCOME)
    main_turtle = initialize_turtle()

    # Tuple - Multiple values stored in one variable
    # draw_steps_tuples = get_actions()
    draw_steps_tuples = get_actions_prompt()

    process_draw_steps(main_turtle, draw_steps_tuples)
    
    turtle.Screen().exitonclick()

if __name__ == '__main__':
    main()
