# `023` List and tuple

## 📝 Instrucciones:

1. Crea una función llamada `list_and_tuple()` que, dado un conjunto de `n` números como entrada, devuelve una lista y una tupla con esos números y los transforma a cada uno de ellos en string.

2. Imprime la lista primero, y en la siguiente línea la tupla.

## 📎 Ejemplo de entrada:

```py
list_and_tuple(34,67,55,33,12,98)
```

## 📎 Ejemplo de salida:

```py
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')
```

## 💡 Pistas:

+ La cantidad de parámetros aceptados por la función no está limitado.

+ Para crear una función que acepta un número ilimitado de argumentos, utiliza el operador `*` y luego cualquier nombre que desees. De esta forma:

```py
def my_function(*args)
```
