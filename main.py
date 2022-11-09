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
def print_draw_list(draw_list):
    print("Current drawing list:")
    for i in draw_list:
        print(i)

def get_actions_prompt():
    draw_list = []
    prompt = """
Enter a direction from the following:
[0] Left
[1] Right
[2] Forward
[e] Edit an entry
[z] Undo last entry
[q] Quit
Your choice: """

    edit_prompt = """
Enter a direction from the following:
[0] Left
[1] Right
[2] Forward
[c] Cancel
Your choice: """
    keep_going = True
    while keep_going:
        response = input(prompt)
        if response == 'q':
            keep_going = False
        elif response == 'e':
            if len(draw_list) > 0:
                print("Editing an item:")
                for i in range(len(draw_list)):
                    print(f"[{i}] {draw_list[i]}")
                edit_item = eval(input("Enter the index of the action to edit: "))
                edit_response = input(edit_prompt)
                if edit_response == 'c':
                    print("Edit canceled")
                else:
                    if eval(edit_response) == 0:
                        direction = 'left'
                    elif eval(edit_response) == 1:
                        direction = 'right'
                    elif eval(edit_response) == 2:
                        direction = 'forward'
                    else:
                        direction = 'NA'
                    distance = eval(input('Enter a numeric value to go: '))
                    action = (direction, distance)
                    draw_list[edit_item] = action
            else:
                print("Nothing to edit.")
        elif response == 'z':
            if len(draw_list) > 0:
                last_action = draw_list.pop()
                print(f'{last_action} removed')
            else:
                print("Nothing to undo.")
        else:
            if eval(response) == 0:
                direction = 'left'
            elif eval(response) == 1:
                direction = 'right'
            elif eval(response) == 2:
                direction = 'forward'
            else:
                direction = 'NA'
            distance = eval(input('Enter a numeric value to go: '))
            action = (direction, distance)
            draw_list.append(action)
        print_draw_list(draw_list)
    return draw_list
    
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
    elif direction == 'right':
        t.right(distance)
    else:
        print(direction, 'not implemented')
        return

def initialize_turtle():
    return turtle.Turtle()

def process_draw_list(t, draw_list):
    for i in range(len(draw_list)):
        draw(t, draw_list[i][0], draw_list[i][1])

def main():
    print(APPLICATION_NAME)
    main_turtle = initialize_turtle()

    # Tuple - used to store multiple items in a single variable
    # nicedraw_list_tuple = get_actions()
    draw_list_tuple = get_actions_prompt()
    process_draw_list(main_turtle, draw_list_tuple)

    turtle.Screen().exitonclick()

if __name__ == '__main__':
    main()

