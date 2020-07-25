#passing an arbitrary number of arguments
#*args tells python to make an empty tuple called args
# and pack whatever values it receives into this tuple
#Note that python packs the arguemnts into a tuple
#even if the function receives only one value
#thsi syntax works no matter how many arguments the function receives


def make_pizza_1(*toppings):
    #print(toppings)
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"-{topping}")
make_pizza_1('pepperoni')
make_pizza_1('asdf','extare cheese','chaojila')

'''
mixing positional and arbitrary arguments
If you want a function to accept several different kinds of arugments
The paarament that accepts an arbitrary number of arguments must be
placed last in the function definition.
Python matchers positional and keyword arguments first and the collects any remaining arguments in the final parameter
'''
def make_pizza(size,*toppings):
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"-{topping}")
    
make_pizza(16,'pepproni')
make_pizza(123,'mushroon','lajiao','dasuan')
