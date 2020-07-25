
# requested_toppings = ['mushroom','green peppers','extra cheese']
requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        if requested_topping == 'green peppers':
            print("sorry,we are out of green peppers right now.")
        else:
            print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you wnat a plain pizza?")


available_toppings = ['mushroom','olives','green peppers','pepperoni','pineapple','extra cheese']
requested_toppings = ['mushrooms','pineapple','extra cheesh']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry,we donot have {requested_topping}.")
print("\nFinished making your pizza!")
