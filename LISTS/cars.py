# sort() method to sort a list permanently

cars = ['bmw','audi','toyota','subaru']
cars.sort()
print(cars)

cars = ['bmw','audi','toyota','subaru']
cars.sort(reverse=True)
print(cars)

# sorted() function to sort a list temporarily
cars = ['bmw','audi','toyota','subaru']
print("Here is the original list: ")
print(cars)
print("\nHere is the sorted list: ")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)

# use the reverse() method to reverse the original order of a list.
# and it is permanently,but you can reert to the original order anytime by applying reverse() to the same list a second time.
print()
print(cars)
cars.reverse()
print(cars)

# Finding the length of a list by the len() function.
cars = ['bmw','audi','toyota','subaru']
print(len(cars))
print(f"The length of the list cars is {len(cars)}")