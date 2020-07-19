motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

# modifying elements in a list
motorcycles[0] = 'ducati'
print(motorcycles)

# adding elements to a list
motorcycles = ['honda','yamaha','suzuki']
motorcycles.append('ducati')
print(motorcycles)

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

# inserting elements into a list
motorcycles.insert(0,'ducati')
print(motorcycles)

# removing elements from a list ,using the 'del' statement
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

del motorcycles[0]  #you know the position of the item
print(motorcycles)

del motorcycles[1]
print(motorcycles)

# removing elemnts from a list,using the 'pop()' method
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop() #remove the last item in a list
print(motorcycles)
print(popped_motorcycle)

motorcycles = ['honda','yamaha','suzuki']
last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}")

# popping items from any position in a list
motorcycles = ['honda','yamaha','suzuki']
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")


# removing an item by value,you only know the value of the item
# you want remove,you can use the remove() method

motorcycles = ['honda','yamaha','suzuki','ducati']

motorcycles.remove('ducati')
print(motorcycles)

motorcycles = ['honda','yamaha','suzuki','ducati']
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")

print(motorcycles)
print(motorcycles[3])