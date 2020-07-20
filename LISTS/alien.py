alien_color = ['green','yellow','red']

if 'green' in alien_color:
    print("The player earned 5 points.")
if 'blue' in alien_color:
    print("The player earned 5 points.")


if 'green' in alien_color:
    print("The player earned 5 points.")
else:
    print("The player earned 10 points.")

if 'green' in alien_color:
    print("The player earned 5 points.")
elif 'yellow' in alien_color:
    print("The player earned 10 points.")
elif 'red' in alien_color:
    print("The player earned 15 points.")
else:
    print("The player earned 0 points.")



age = int(input("please enter you age: "))
if age < 2:
    print("He is a baby")
elif 2<=age<4:
    print("He is toddler")
elif 4<=age<12:
    print("He is kid.")
elif 12<=age<20:
    print("He is a teenager")
elif 20<=age<65:
    print("He is adult")
else:
    print("He is a elder")