s = raw_input()
words = [word for word in s.split(" ")]
print " ".join(sorted(list(set(words))))