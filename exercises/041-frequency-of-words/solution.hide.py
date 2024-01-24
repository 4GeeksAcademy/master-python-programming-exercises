# Your code here
def compute_word_frequency(sentence):
    words = sentence.split()

    word_frequency = {}

    for word in words:
        word_frequency[word] = word_frequency.get(word, 0) + 1

    sorted_word_frequency = sorted(word_frequency.items(), key=lambda x: x[0])

    for word, frequency in sorted_word_frequency:
        print(f"{word}: {frequency}")


input_sentence = "New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3."
compute_word_frequency(input_sentence)
