# Your code here
import re

def valid_password(password):
    if len(password) < 6 or len(password) > 12:
        return "Invalid password. Please try again"

    if not re.search("[a-z]", password):
        return "Invalid password. Please try again"
    elif not re.search("[0-9]", password):
        return "Invalid password. Please try again"
    elif not re.search("[A-Z]", password):
        return "Invalid password. Please try again"
    elif not re.search("[$#@]", password):
        return "Invalid password. Please try again"
    elif re.search("\s", password):
        return "Invalid password. Please try again"

    return "Valid password"

print(valid_password("ABd1234@1"))


### SOLUTION 2 ###

# import re

# def valid_password(password):
#     pattern = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[$#@]).{6,12}$')

#     if pattern.match(password):
#         return "Valid password"
#     else:
#         return "Invalid password. Please try again"

# print(valid_password("ABd1234@1"))
