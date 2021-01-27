 # `129` Guess the number

## 📝 Instructions:

Augustus and Beatrice play the following game. Augustus thinks of a secret integer number from 1 to n. Beatrice tries to guess the number by providing a set of integers. Augustus answers YES if his secret number exists in the provided set, or NO, if his number does not exist in the provided set. Then after a few questions Beatrice, totally confused, asks you to help her determine Augustus's secret number.

Given the positive integer n in the first line, followed by the a sequence Beatrice's guesses, series of numbers seperated by spaces and Agustus's responses, or Beatrice's plea for HELP. When Beatrice calls for help, provide a list of all the remaining possible secret numbers, in ascending order, separated by a space.

**Example input**
10
1 2 3 4 5
YES
2 4 6 8 10
NO
HELP

**Example output**
1 3 5

**Theory**
If you don't know how to start solving this assignment, please, review a theory for this lesson:
https://snakify.org/lessons/sets/