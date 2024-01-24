# `041` Frequency of words

## 📝 Instrucciones:

1. Escribe una función llamada `compute_word_frequency()` para calcular la frecuencia de las palabras a partir de un string de entrada.

2. Coloca cada palabra separada por un espacio en un diccionario y cuenta su frecuencia.

3. Ordena el diccionario alfanuméricamente e imprime en la consola cada clave en una nueva línea.

## 📎 Ejemplo de entrada:

```py
compute_word_frequency("New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.")
```

## 📎 Ejemplo de salida:

```text
2: 2
3.: 1
3?: 1
New: 1
Python: 5
Read: 1
and: 1
between: 1
choosing: 1
or: 2
to: 1
```

## 💡 Pista:

+ Puedes poner cada palabra de un string en una lista con el método `split()`, luego te será mucho más fácil trabajar en la solución.
