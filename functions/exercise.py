#8-12
def sandwich(*toppings):
    print("The list of items that you want on your sandwich is:")
    for topping in toppings:
        print(f"-{topping}")

sandwich('dasuan','lajiao','jiemo')
print()


#8-13
def build_profile(first,last,**user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
my_profile=build_profile('chen','xinhong',school='XMU',company='BOE',hometown='tianshui')
print(my_profile)
print()


#8-14
def car_info(manufacturer,model,**car_info):
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info
my_car = car_info('volvo','s60',color='white',tow_package=False,price=300000)
print(my_car)