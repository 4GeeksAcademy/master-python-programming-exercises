def divisable_binary(text):
    value=[]
    items=[x for x in text.split(',')]
    for p in items:
        intp = int(p, 2)
        if not intp%5:
            value.append(p)

    return (','.join(value))