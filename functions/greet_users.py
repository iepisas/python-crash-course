def greet_users(names):
    for name in names:
        if type(name) == str:
            msg = f"Hello,{name.title()}"
            print(msg)
        else:
            msg = f"Hello,{name}"
            print(msg)

usernames = ['adhfa','adf','qw','awe',12,45,33]
greet_users(usernames)