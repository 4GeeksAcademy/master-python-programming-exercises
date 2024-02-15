# `038` Sort Tuples Ascending

## 📝 Instructions:

Write a function `sort_tuples_ascending()` to sort the (`name`, `age`, `score`) tuples by ascending order, where `name`, `age` and `score` are all strings. The sort criteria is:

1. Sort based on name.
2. Then sort based on age.
3. Then sort by score.

The priority is `name` > `age` > `score`.

## 📎 Example input:

```py
sort_tuples_ascending(['Tom,19,80', 'John,20,90', 'Jony,17,91', 'Jony,17,93', 'Jason,21,85'])
```

## 📎 Example output:

```py
[('Jason', '21', '85'), ('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Tom', '19', '80')]
```

## 💡 Hints:

+ We use `itemgetter` to enable multiple sort keys.

+ Notice that the output is a list with tuples inside.
