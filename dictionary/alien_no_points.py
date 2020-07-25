alien_0 = {'color':'green','speed':'slow'}
print(alien_0['points']) #here will get an error,cause the key is not exist

point_value = alien_0.get('points','No point value assigned.')
print(point_value)
#use the get() method to set a default value that will be returned if the requested key doesn't exist.
#THe get() method requires a key as a first argument ,as a second optional argument ,you can pass the value to be returned if the key doesn't exist.
