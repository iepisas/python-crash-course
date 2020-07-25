age = int(input("Please enter you age: "))
if age < 3:
    print("your ticket is free.")
elif 3<= age <= 12:
    print("Your ticket is $10.")
else:
    print("your ticket is $15.")

while True:
    age = int(input("Please enter you age: "))