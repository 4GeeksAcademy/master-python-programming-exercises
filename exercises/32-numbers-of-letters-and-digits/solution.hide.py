def letters_and_digits(text):
    d={"DIGITS":0, "LETTERS":0}
    for c in text:
        if c.isdigit():
            d["DIGITS"]+=1
        elif c.isalpha():
            d["LETTERS"]+=1
        else:
            pass
    
    return ("LETTERS {} DIGITS {}".format(d['LETTERS'], d['DIGITS']))