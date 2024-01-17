# Your code here
import re

def valid_password(password):
    pattern = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[$#@]).{6,12}$')
    
    if pattern.match(password):
        return "Valid password"
    else:
        return "Invalid password. Please try again"


print(valid_password("ABd1234@1"))
