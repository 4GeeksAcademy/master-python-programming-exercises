# Your code here
def sequence_of_words(words):
    items=[x for x in "{}".format(words).split(',')]
    items.sort()
    return (','.join(items))

print(sequence_of_words("this,is,sorted"))
