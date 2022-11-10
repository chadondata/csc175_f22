# Lab 07 Challenge

For this week's challenge, we need to refactor the get_actions_prompt. It simply does too much work for one function.

## Starting Code

Use the code [here](main_07.py)

## To Do

Create a function called edit_action(action_list) that uses the logic in the get_actions_prompt() function when the user selects 'e'
(Hint: look for elif response == 'e'  That's the logic I mean)

The function should:

* show the user all of the entries in the action_list array (including a numerical index)
* prompt the user for which index they'd like to edit
* Show the user a prompt to get the new direction (forward, left, right)
* Prompt the user for the distance
* Create a tuple from their responses
* Replace the tuple in the action_list with the new tuple
* Return the action_list

All of the logic is already here, you'll want to move it to a function (be sure to remember the return statement)

Once your function is done, replace the code for the 'e' response with a call to edit_action() like so:
action_list = edit_action(action_list)