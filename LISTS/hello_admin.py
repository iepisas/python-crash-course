#5-8 & 5-9
users = ['iepi','xixi','zhima','pinpin','admin','cxh','sas']

if users:
    for user in users:
        if user == 'admin':
            print(f"Hello admin,would you like to see a status report?")
        else:
            print(f"hello,{user},thank you for logging in again.")
else:
    print("We need to find some users!")

print()
#5-10
current_users = ['iepi','xixi','zhima','pinpin','admin','cxh','sas']
new_users = ['Iepi','xiyunfu','wushan','pinpin','tianshui','lele','sas']
for new_user in new_users:
    if new_user.lower() in current_users:
        print(f"{new_user} ,you need to enter a new username.")
    else:
        print(f"hi {new_user},your username is available.welcome to lezhi.com.")

#5-11
print("5-11 test")
number = [1,2,3,4,5,6,7,8,9]
for i in number:
    if i==1:
        print('1st')
    elif i==2:
        print('2nd')
    elif i==3:
        print('3rd')
    else:
        print(f"{i}th")