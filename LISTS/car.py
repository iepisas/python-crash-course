cars = ['audi','bmw','subaru','toyota']

# check for equality with  ==
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

#check for inequality with !=

requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")

# using and to check multiple conditions
# using or to check multiple conditons
age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)

#using in to check whether a value is in a list
requested_topping = ['mushroom','onions','pineapple']
print('mushroom' in requested_topping)
print('pepperoni' in requested_topping)

#using not in to check whether a value is not in a list

banned_users = ['andrew','carolina','david']
user = 'marie'
if user not in banned_users:
    print(f"{user.title()},you can post a response if you wish.")
