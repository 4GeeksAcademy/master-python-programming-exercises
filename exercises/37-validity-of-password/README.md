# `37` Validity of password

## 📝 Instructions:

A website requires the users to input a username and password to register. Write a function named `valid_password()` to check the validity of password input by users. Following are the criteria for checking the password:

1. At least 1 letter between [a-z]. 
2. At least 1 number between [0-9]. 
3. At least 1 letter between [A-Z]. 
4. At least 1 character from [$#@]. 
5. Minimum length of password: 6. 
6. Maximum length of password: 12. 

Your program should accept a sequence of comma separated passwords and check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.  

## 📎 Example input:

```text
valid_password("ABd1234@1,a F1#,2w3E*,2We3345")
```

## 📎 Example output:

```text
ABd1234@1
```

## 💡 Hints:

+ Read about regular expressions in Python.

+ You will need the `search()` function.
