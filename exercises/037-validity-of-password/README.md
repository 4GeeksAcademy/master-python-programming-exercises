# `037` Validity of password

## 📝 Instructions:

A website requires the users to input a username and password to register. Write a function named `valid_password()` to check the validity of password input by users. Following are the criteria for checking the password:

1. At least 1 letter between [a-z]. 
2. At least 1 number between [0-9]. 
3. At least 1 letter between [A-Z]. 
4. At least 1 character from [$#@]. 
5. Minimum length of password: 6. 
6. Maximum length of password: 12. 

Your program should accept a password and verify it according to the previous criteria. If the password is successfully validated, the function returns the following string `"Valid password"`. Otherwise, it returns `"Invalid password. Please try again"`.

## 📎 Example input:

```py
valid_password("ABd1234@1")
```

## 📎 Example output:

```py
"Valid password"
```

## 💡 Hints:

+ Read about regular expressions in Python.

+ You will need to import the 're' module (regular expressions) to be able to use the `search()` function.

+ To import it, copy and paste the following at the beginning of your file: `import re`.
