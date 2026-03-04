# (a)
# Create a file called user_logins.py
# Inside it, create this dictionary:

logins = {"Katie": 1, "Ben": 2, "Ciara": 1}

# (b)
# Still inside user_logins.py,
# add this TOP-LEVEL print statement:

print("Loading user_logins...")


# (c)
# Inside user_logins.py, write a function:
#     add_login(logins, username)
# It should:
#     - increase the count if username exists
#     - otherwise create it with value 1

def add_login(logins, username):
    if username in logins:
        logins[username] += 1
    else:
        logins[username] = 1


# (a)
# Inside user_logins.py, write a function:
#     get_login_count(logins, username)
# It should:
#     - return the login count if the user exists
#     - return 0 if the user does not exist

def get_login_count(logins, username):
    return logins.get(username, 0)

# (b)
# Inside user_logins.py, add a test block:

#     if __name__ == "__main__":
#         # test your functions here

# In the test block:
#     - print Katie’s login count
#     - print David’s login count
#     - call add_login(logins, "Katie")
#     - print the updated dictionary

if __name__ == "__main__":
    print(get_login_count(logins, "Katie"))  # should print 1
    print(get_login_count(logins, "David"))  # should print 0
    add_login(logins, "Katie")
    print(logins)  # Katie's count should now be 2