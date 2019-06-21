import random

tree_age = 1

state = "alive"

value = 1

age_display = "Your tree have an age of: {}".format(tree_age)
state_display = "Your tree is {}.".format(state)

def tree_state(x):
    if x <= 19:
        state = "alive"
        return state
    elif x <= 49:
        rand = random.randrange(tree_age, 51, 1)
        if rand == 50:
            state = "dead"
        else:
            state = "alive"
        return state
    else:
        state = "dead"
        return state
    
print("Welcome to your tree garden!")

while value == 1 :
    
    print(age_display)
    print(state_display)
    print("Please press 1 to increase is age or 2 to quit.")
    action = input("Select 1/2 ")

    if action  == "2" :
                 value = 2

    elif action == "1" :
                 tree_age += 1
                 #la fonction tree_state ne se lance pas je crois
                 tree_state(tree_age)
                 print(state)
                 if state == "dead":
                     print("Sorry your tree is dead.")
                     quit()
                 else:
                     age_display = "Your tree have an age of: {}".format(tree_age)

    else:
                 print("Invalid input, please enter the right input.")

if value == 2:
                 print("Thanks")
