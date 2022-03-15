# `028` remove duplicate words

## 📝 Instructions:

1. Write a function `remove_duplicate_words()` that receives a string as parameter and returns the words after removing all duplicate words and sorting them alphanumerically.

## Example input:

```py
remove_duplicate_words("hello world and practice makes perfect and hello world again")
```

## Example output:

+ "again and hello makes perfect practice world"

## 💡 Hints:

+ We use set container to remove duplicated data automatically and then use sorted() to sort the data.
