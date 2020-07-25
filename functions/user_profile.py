#using arbitrary keyword arguments
#using **kwargs,python create an empty dictionary called kwargs,
#and pack what ever name_value pairsit receives into this dictionary.
def build_profile(first,last,**user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert','einstein',location='princeton',filed='physics')
print(user_profile)