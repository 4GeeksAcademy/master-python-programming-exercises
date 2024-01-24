# Your code here
def remove_duplicate_words(text):
    words = text.split()
    return (" ".join(sorted(list(set(words)))))

print(remove_duplicate_words("hello world and practice makes perfect and hello world again"))
