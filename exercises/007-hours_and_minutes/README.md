# `007` Hours and Minutes

In this exercise we are going to suppose that it is midnight, we want that with the function `hours_minutes` that we have provided to you, you were able to tell us how much time has passed since then with the seconds that are introduced as parameter.

## 📝 Instructions:

1. Complete the function to return the expected result.

2. Perform two calculations with the seconds that are passed by parameter in the function so that one calculates the time according to the seconds that have passed and the other to know the minutes `(hour , minutes)`.

## Example 1:

```py
output = hours_minutes(3900)
print(output) # (1, 5)
```

## Example 2:

```py
output = hours_minutes(60)
print(output) # (0, 1)
```

## 💡 Hints:

+ Remember how many seconds there are in an hour (3600) and how many seconds in a minute (60).

+ If you don't know how to start solving this assignment, please, review a theory for this lesson: https://snakify.org/lessons/print_input_numbers/

+ You may also try step-by-step theory chunks: https://snakify.org/lessons/print_input_numbers/steps/1/


[comment]: <Solution: (secs//3600, secs//60)>
