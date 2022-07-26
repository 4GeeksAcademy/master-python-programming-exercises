def sequence_of_words(words):
    items=[x for x in "{}".format(words).split(',')]
    items.sort()
    return (','.join(items))
