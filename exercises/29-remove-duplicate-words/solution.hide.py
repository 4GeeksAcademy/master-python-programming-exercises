def remove_duplicate_words(text):
    words = text.split()
    return (" ".join(sorted(list(set(words)))))
