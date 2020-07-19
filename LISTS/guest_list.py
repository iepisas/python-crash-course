people_to_dinner = ['iepi','zhima','xixi','sas','cxh']
print(f"hi,{people_to_dinner[0]},could you have a dinner with me this evening?")
print(f"hi,{people_to_dinner[1]},could you have a dinner with me this evening?")
print(f"hi,{people_to_dinner[2]},could you have a dinner with me this evening?")
print(f"hi,{people_to_dinner[3]},could you have a dinner with me this evening?")
print(f"hi,{people_to_dinner[4]},could you have a dinner with me this evening?")

print(f"oh,my god,{people_to_dinner[3]} can't come to dinner,he is busy now.")

people_to_dinner[3] = "pinpin"
print()
for friend in people_to_dinner:
    print(f"hi,{friend},could you have a dinner with me this evening?")

print(people_to_dinner)

people_to_dinner.insert(0,'mama')
print(people_to_dinner)
people_to_dinner.insert(1,'baba')
print(people_to_dinner)
people_to_dinner.append('yeye')
print(people_to_dinner)
people_to_dinner.append('nainai')
print(people_to_dinner)
people_to_dinner.remove('pinpin')
print(people_to_dinner)
people_to_dinner.pop(4)
print(people_to_dinner)
people_to_dinner.pop()
print(people_to_dinner)
del people_to_dinner[3]
print(people_to_dinner)
