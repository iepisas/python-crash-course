#variable in the definition of a function is an example of a parameter
#the value in function call is an example of a argument.

#function can have multiple parameters
#function call may need multiple arguments.

#positional arguments,which need to be in the same order the parameters were written
#keyword arguments where each argument consists of a variable name and a value


#positional arguments
def describe_pet(animal_type, pet_name):
    """Display information anout a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

#order matters inpositional arguments
describe_pet('hamster','harry')
describe_pet('harry','hamster')
describe_pet('dog','willie')


#keyword arguments
#A keyword argument is a name-value pair that you pass to a funcion.
describe_pet(animal_type='hamster',pet_name='harry')
describe_pet(pet_name='harry',animal_type='hamster')
#Note:When you use keyword arguments,be sure to use the exact names
#of the parameters in the function's definition.

#Default values
def describe_pet(pet_name,animal_type='dog'):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='willie')


#equivalent function calls
describe_pet('willie')
describe_pet(pet_name='willie')
describe_pet('harry','hamster')
describe_pet(pet_name='harry',animal_type='hamster')
describe_pet(animal_type='hamster',pet_name='harry')
