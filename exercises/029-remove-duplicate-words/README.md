# `029` Remove duplicate words

## 📝 Instructions:

1. Write a function called `remove_duplicate_words()` that accepts a sequence of whitespace separated words as input and returns the words after removing all duplicate words and sorting them alphanumerically.

## 📎 Example input:

```py
remove_duplicate_words("hello world and practice makes perfect and hello world again")
```

## 📎 Example output:

```text
again and hello makes perfect practice world
```

## 💡 Hints:

+ You can convert your input into the `set` data type to automatically eliminate duplicates.

+ You can use `sorted()` to sort the data from a list.
