<!-- hide -->
<div align="center">

# Master Python by practice (interactive)

[![Certified tutorial](https://img.shields.io/badge/4Geeks-certified%20tutorial-2563eb)](https://4geeks.com/en/interactive-exercise/practice-python)
[![Autograded with LearnPack](https://img.shields.io/badge/LearnPack-43%20autograded%20exercises-2563eb)](https://learnpack.co)
[![Open in GitHub Codespaces](https://img.shields.io/badge/Open%20in-GitHub%20Codespaces-fb5a1f?logo=github)](https://codespaces.new/?repo=4GeeksAcademy/master-python-programming-exercises)

</div>
<!-- endhide -->

Master Python by practice is an interactive tutorial with 47 coding exercises that you solve inside VS Code, plus a welcome page. 43 of them are auto-graded by pytest and every one ships a reference solution. It takes roughly 10 hours and goes from integer arithmetic and digit manipulation to regular expressions, generators and object-oriented programming with inheritance, static methods and class methods.

<!-- hide -->
## 📋 About this tutorial

- **Difficulty**: declared as `easy` in [learn.json](https://github.com/4GeeksAcademy/master-python-programming-exercises/blob/HEAD/learn.json), although the range is wide: exercise 001 is a single `print()` and exercise 045 is a class method with a class variable.
- **Duration**: 10 hours (`"duration": 10` in learn.json).
- **Exercises**: 48 folders inside [`exercises/`](https://github.com/4GeeksAcademy/master-python-programming-exercises/tree/HEAD/exercises) — 1 welcome page and 47 coding exercises.
- **Automatic grading**: yes, `"graded": true`. 43 of the 47 coding exercises include a `test.py` pytest suite.
- **Technologies**: Python 3 (the dev container pins 3.10), pytest 6.2.5, pytest-testdox, mock, LearnPack on Node.js 22.
- **Video solutions**: none (`"videoSolutions": false`), but all 47 coding exercises ship a `solution.hide.py` file.
- **Instructions available in**: [English](https://github.com/4GeeksAcademy/master-python-programming-exercises/blob/HEAD/README.md) and [Español](https://github.com/4GeeksAcademy/master-python-programming-exercises/blob/HEAD/README.es.md) — all 48 folders carry both a `README.md` and a `README.es.md`.
<!-- endhide -->

## 🎯 What will you learn?

The exercises are ordered so that each block builds on the previous one:

- **Integer and float arithmetic**: floor division `//`, modulo `%`, exponentiation `**`, `round()` and the `math` module (imported in 6 of the reference solutions).
- **Digit manipulation without strings**: extracting the tens digit, summing the digits of a three-digit number, swapping digits, reading the digit right after the decimal point.
- **Lists, tuples and dictionaries**: building a squares dictionary, generating a 2-D matrix, turning a variable number of arguments into both a list and a tuple, counting word frequency.
- **Multi-key sorting**: `from operator import itemgetter` to order `(name, age, score)` tuples by three criteria in priority order.
- **Number bases**: converting 4-digit binary strings with `int(binary, 2)`.
- **Regular expressions**: `import re` and `re.search()` to validate a password against six rules at once.
- **Generators**: a class with a generator function that uses `yield` to walk the multiples of 7.
- **Object-oriented programming**: `__init__`, `__str__`, inheritance with `super()`, polymorphism by overriding a parent method, `@staticmethod` and `@classmethod` with class variables.

Two topics are deliberately absent: there is no `try`/`except` error handling and no file input/output anywhere in the 48 exercise folders (verified across every `README.md`, `app.py` and `solution.hide.py`). Recursion and `async` do not appear either.

## 👀 What will you build?

47 small Python programs, each in its own numbered folder. The three blocks:

**Exercises 001 to 022 — 23 numeric problems** (folder `006.1` splits one of them in two). You write `digits_sum()`, which must return 17 for the input 854; `day_of_week()`, which returns 4 for day 1 of a year that starts on a Thursday; `digital_clock()`, which turns 150 minutes past midnight into `(2, 30)`; `square_root()`, which returns `7.07` for 50; plus a factorial, a century calculator, an apple-sharing problem and a car-route problem.

**Exercises 023 to 041 — 19 data-structure and algorithm problems** (two of them, `024` and `039`, already ask you to write a class). `two_dimensional_list(3, 5)` must return `[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]`. `divisible_binary("0100,0011,1010,1001")` must return the string `"1010"`. `computed_value(9)` must return 11106, the sum of 9 + 99 + 999 + 9999. `net_amount("D 300 D 300 W 200 D 100")` must return 500. `valid_password("ABd1234@1")` must return the exact string `"Valid password"`. `compute_robot_distance(["UP 5", "DOWN 3", "LEFT 3", "RIGHT 2"])` must return 2. `compute_word_frequency()` must report `Python:5` for the sample sentence.

**Exercises 042 to 045 — 5 object-oriented exercises.** You build a `Student` class, add `__init__` and `__str__` to a `Book` class, extend `Student` into a `CollegeStudent` with a `major` attribute and an `attend_lecture()` method, then write a `MathOperations` class with a static `add_numbers()` and a class method `calculate_circle_area()` that returns `78.53975` for a radius of 5.

## 🎓 What do you need before starting?

Nothing installed, if you open the repository in GitHub Codespaces: the dev container provisions Python 3.10, Node.js 22, pytest and the LearnPack Python plugin on its own.

What you do need is prior Python: this is the fourth and last set in a series, and the welcome page points you to the three that come first.

- [Python for beginners](https://github.com/4GeeksAcademy/python-beginner-programming-exercises) — variables, `print()`, conditionals.
- [Practice functions](https://github.com/4GeeksAcademy/python-functions-programming-exercises) — parameters, return values, scope.
- [Practice loops and lists](https://github.com/4GeeksAcademy/python-lists-loops-programming-exercises) — `for`, `while`, list handling.

If you already know how to declare a function and loop over a list, you can start here directly. Exercise 001 is still a plain `print("Hello World")`, so the on-ramp is gentle.

## ✅ How does the automatic grading work?

Every graded exercise carries a `test.py` written with pytest. Each assertion is labelled with `@pytest.mark.it("...")`, and `pytest-testdox` prints those labels as readable sentences, so a failure tells you what was expected instead of dumping a traceback.

The suites check two different things depending on the exercise:

- **Returned values.** In `013-sum_of_digits` the tests assert that `digits_sum` is callable, that it returns something, that the return type is `int`, and finally that `digits_sum(854) == 17`.
- **Printed output.** In `001-hello_world` the test captures stdout and compares it byte for byte against `"Hello World\n"`.

Four exercises have no `test.py` and are free practice: `031-sum-eigth-digit`, `033-number-of-uppercase`, `035-square-each-odd-number` and `039-class-that-iterates`. That is 43 graded out of 47.

> 💡 The grading is strict on purpose, and the repository maintainers say so themselves: treat a red test as a hint about the expected shape of your answer, not as a verdict on your logic.

## 💡 What mistakes should you avoid?

- **Printing when the test wants a `return`.** Most suites call your function and inspect the value it hands back. `digits_sum(854)` has to *return* 17; printing 17 fails the type assertion.
- **Trusting the wording over the test in exercises 019 and 030.** The instructions of `019-digital_clock` say the function should *print* two numbers, but its test asserts `digital_clock(194) == (3, 14)`. Same trap in `030-divisable-binary`: the instructions say *print* the numbers divisible by 5, while the test asserts `divisible_binary("0100,0011,1010,1001") == "1010"`. Return the value in both.
- **Formatting exercise 041 line by line.** The instructions ask for one key per line, yet the test compares stdout against a single line: `"2:2 3.:1 3?:1 New:1 Python:5 Read:1 and:1 between:1 choosing:1 or:2 to:1\n"`. Note there is no space after the colon.
- **Forgetting `import re` in exercise 037**, and forgetting that the password rules include *both* bounds: minimum 6 characters and maximum 12. The failure string must be exactly `"Invalid password. Please try again"`.
- **Swapping rows and columns in exercise 026.** `two_dimensional_list(3, 5)` returns 3 rows of 5 items, not 5 rows of 3.
- **Rounding to the wrong precision.** Exercise 021 keeps two decimals (`square_root(50)` gives `7.07`); exercise 040 rounds the robot distance to the nearest integer.
- **Confusing static methods with class methods.** A `@staticmethod` (exercise 044) receives neither `self` nor `cls` and cannot read class state; a `@classmethod` (exercise 045) receives `cls` and is what lets `calculate_circle_area()` reach the class variable `pi`.
- **Renaming the function.** The first assertion of most suites is `assert callable(app.<name>)`, so a typo in the function name fails everything downstream.

## ❓ Frequently asked questions

### How long does it take to finish these Python exercises?

The tutorial declares 10 hours. Spread over 47 coding exercises that averages about 13 minutes each, but the distribution is uneven: the numeric block (001–022) tends to go fast once you know `//` and `%`, while the regex, sorting and OOP exercises take noticeably longer.

### Do I need to know Python before starting?

Yes, some. This is the last set of a four-part series, and the welcome page assumes you have already covered variables, functions, loops and lists. You do not need an object-oriented background: the theory is taught from scratch in exercise 042, with a worked `Student` example before you are asked to write anything. Be warned, though, that two earlier exercises already expect a class with barely any explanation — `024-class-with-two-methods`, which is graded, and `039-class-that-iterates`.

### Is this tutorial free, and can I reuse the content?

Opening and solving it costs nothing. Reusing the content does not: [LICENSE.md](https://github.com/4GeeksAcademy/master-python-programming-exercises/blob/HEAD/LICENSE.md) reserves all intellectual property rights and explicitly forbids republishing, selling, sub-licensing, reproducing or redistributing the material. It is not an open source licence. The Python you write in your own `app.py` files is yours.

### Do I have to install anything on my computer?

No. Opening the repository in Codespaces gives you a ready dev container. A local setup is possible and documented below, and needs Python 3, Node.js and the LearnPack Python plugin.

### Are there video solutions?

No. `learn.json` sets `videoSolutions` to `false`. What you do get is a `solution.hide.py` file in each of the 47 coding folders, plus the hints at the bottom of most exercises (39 of the 48 folders carry a hints section), which link to outside references such as the snakify lessons on integer and float numbers.

### Is practising algorithms like this still worth it?

The exercises target the mechanics an interview or a code review still checks: reasoning about integer division instead of reaching for a string cast, picking the right container, sorting with several keys, and knowing why a method is bound to the class rather than to the instance. Those do not expire. What this set does not teach is error handling, file I/O or any third-party library.

<!-- hide -->
## 🚀 How to start

The fastest path is one click: [open this tutorial in GitHub Codespaces](https://codespaces.new/?repo=4GeeksAcademy/master-python-programming-exercises). There is also a [Gitpod](https://gitpod.io#https://github.com/4GeeksAcademy/master-python-programming-exercises) alternative.

Once VS Code is open, the LearnPack exercises should start on their own. If they do not, run this in the terminal:

```bash
learnpack start
```

## 💻 Local installation

1. Install LearnPack and the Python plugin, using the same versions the dev container provisions:

```bash
npm i @learnpack/learnpack@5.0.348 -g && learnpack plugins:install @learnpack/python@1.0.6
```

2. Clone the repository and move into it:

```bash
git clone https://github.com/4GeeksAcademy/master-python-programming-exercises.git
cd master-python-programming-exercises
```

3. Install the Python test dependencies and start the tutorial from the same folder as `learn.json`:

```bash
pip3 install pytest==6.2.5 pytest-testdox mock
learnpack start
```

## 📚 How the exercises are organized

Each exercise is a folder inside `exercises/` and contains up to five files:

- `app.py` — the file you edit and the one the computer runs. Present in all 47 coding exercises.
- `README.md` — the instructions, in English.
- `README.es.md` — the same instructions in Spanish. Present in all 48 folders.
- `test.py` — the pytest suite. You never open it. Present in 43 folders.
- `solution.hide.py` — a reference solution. Present in all 47 coding exercises.

The folder `000-welcome` holds only the two READMEs: it is the intro page, not an exercise.

Found a bug or a typo? Open an issue in [this repository](https://github.com/4GeeksAcademy/master-python-programming-exercises/issues) — the exercises were built collaboratively and reports are welcome.

## 🤝 Contributors

Thanks to these people ([emoji key](https://github.com/kentcdodds/all-contributors#emoji-key)):

- [Alejandro Sánchez (alesanchezr)](https://github.com/alesanchezr) — code 💻, idea 🤔, tests ⚠️, pull request review 👀, tutorial build ✅, documentation 📖
- [Paolo (plucodev)](https://github.com/plucodev) — bug reports 🐛, code 💻, translation 🌎
- [Marco Gómez (marcogonzalo)](https://github.com/marcogonzalo) — bug reports 🐛, translation 🌎

Plus [everyone in the contributors graph](https://github.com/4GeeksAcademy/master-python-programming-exercises/graphs/contributors). This project follows the [all-contributors](https://github.com/kentcdodds/all-contributors) specification, and contributions of any kind are welcome.

This tutorial is one of many built by students and teachers at [4Geeks Academy](https://4geeks.com).
<!-- endhide -->
