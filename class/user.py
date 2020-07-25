#exercise 9-3
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