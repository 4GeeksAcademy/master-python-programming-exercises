# Your code here
def sequence_of_words(words):
    palabras = words.split(",")
    palabras.sort()
    return (','.join(palabras))
    
  
print(sequence_of_words("without,hello,bag,world"))