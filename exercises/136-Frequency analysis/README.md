  # `136` Frequency analysis

## 📝 Instructions:

Given a number n, followed by n lines of text, print all words encountered in the text, one per line, with their number of occurrences in the text. The words should be sorted in descending order according to their number of occurrences, and all words within the same frequency should be printed in lexicographical order.

Hint. After you created a dictionary of the words and their frequencies, you would like to sort it according to the frequencies. This can be achieved if you create a list whose elements are lists of two elements: the number of occurrences of a word and the word itself. For example, [[2, 'hi'], [1, 'what'], [3, 'is']]. Then the standard list sort will sort a list of lists, with the lists compared by the first element, and if these are equal, by the second element. This is nearly what is required.

**Example input**
9
hi
hi
what is your name
my name is bond
james bond
my name is damme
van damme
claude van damme
jean claude van damme

**Example output**
damme 4
is 3
name 3
van 3
bond 2
claude 2
hi 2
my 2
james 1
jean 1
what 1
your 1

**Theory**
If you don't know how to start solving this assignment, please, review a theory for this lesson:
https://snakify.org/lessons/dictionaries_dicts/