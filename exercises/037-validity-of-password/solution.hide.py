# Your code here
import re

def valid_password(password):
    pattern = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[$#@]).{6,12}$')
    
    if not pattern.match(password):
        return "Invalid password. Please try again"
    else:
        return "Valid password"


print(valid_password("ABd1234@1"))
