# `037`sort tuples ascending

## 📝 Instructions:

1. You are required to write a function `sort_tuples_ascending()` to sort the (name, age, height) tuples by ascending order where name is string, age and height are numbers. The tuples are input by console. The sort criteria is:

- Sort based on name;-
- Then sort based on age;
- Then sort by score.

*The priority is that name > age > score.*

## Example input:

If the following tuples are given as input to the program:

```py
sort_tuples_ascending(Tom,19,80,Juan,20,90,Juan,17,91,Juan, 17,93,Json,21,85)
```

## Example output:

+ [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]

## 💡 Hint:

+ In case of input data being supplied to the question, it should be assumed to be a console input.

+  Use `itemgetter` to enable multiple sort keys (fom the `operator` module)