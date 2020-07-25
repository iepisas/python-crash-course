def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello,{username.title()}!")

greet_user('jesse')
print()

#using a funcion with a while loop
def get_formatted_name(first_name,last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nPlease tellme your name:")
    f_name = input("First name:")
    if f_name == 'q':
        break
    l_name = input('Last name:')
    if l_name == 'q':
        break
    formatted_name = get_formatted_name(f_name,l_name)
    print(f"\nHello,{formatted_name}!")