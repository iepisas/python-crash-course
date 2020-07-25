class Car:
    """A simple attempt to represent a car."""
    
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")
    
    def update_odometer(self,mileage):
        #way2
        """set the odometer reading to the given value."""
        """Reject the change if it attempts to roll the odometer back."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self,mileage):
        #way3
        """increment the odometer reading to the given value."""
        self.odometer_reading += mileage


my_new_car = Car('adui','a4',2020)
print(my_new_car.get_descriptive_name())

"""There are three ways to change an attributes's value
way1:change the value directly through an instance
way2:set the value through a method
way3:increment the value through a method
"""

#way1:change the value directly through an instance
my_new_car.odometer_reading = 100
my_new_car.read_odometer()

#way2:set the value through a method
my_new_car.update_odometer(150)
my_new_car.update_odometer(30)
my_new_car.read_odometer()

#way3:increment the value through a method
my_new_car.increment_odometer(122_500)
my_new_car.read_odometer()