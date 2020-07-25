#exercise 9-1
class Restaurant:
    
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"The restaurant's name is {self.restaurant_name},and it's cuisine type is {self.cuisine_type}.")
    
    def open_restaurant(self):
        print(f"The restaurant {self.restaurant_name} is opening now.")

restaurant = Restaurant('qinqin fandian','chao mian etc')
print(f"The name is {restaurant.restaurant_name}")
print(f"The restaurant's cuisine is {restaurant.cuisine_type}")
restaurant.describe_restaurant()
restaurant.open_restaurant()

#exercise 9-2
my_res = Restaurant('qinqin fandian','chao mian etc')
your_res = Restaurant('shaxianxiaochi','buhaochi')
his_res = Restaurant('coucouhuoguo','haibucuo')
my_res.describe_restaurant()
your_res.describe_restaurant()
his_res.describe_restaurant()

#exercise 9-3
print()
class User:

    def __init__(self,first_name,last_name,age,city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
    
    def describe_user(self):
        linshi = f"The user's info is:"
        linshi += f"\n\tfirst_name:{self.first_name}"
        linshi += f"\n\tlast_name:{self.last_name}"
        linshi += f"\n\tage:{self.age}"
        linshi += f"\n\tcity:{self.city}"
        print(linshi)
    
    def greet_user(self):
        full_name = f"{self.first_name} {self.last_name}"
        print(f"welcome our guest,{full_name.title()},have enjoy!")

me = User('chen','iepi',30,'hefei')
she = User('w','z',30,'shanghai')
me.describe_user()
she.describe_user()
me.greet_user()
she.greet_user()