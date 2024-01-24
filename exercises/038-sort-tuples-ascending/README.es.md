# `038` Sort Tuples Ascending

## 📝 Instrucciones:

Escribe una función llamada `sort_tuples_ascending()` para ordenar las tuplas (`name`, `age`, `score`) en orden ascendente, donde `name`, `age` y `score` son strings. El criterio de orden es:

1. Ordenar según el nombre.
2. Luego, ordenar según la edad.
3. Después, ordenar por puntuación.

La prioridad es `name` > `age` > `score`.

## 📎 Ejemplo de entrada:

```py
sort_tuples_ascending(['Tom,19,80', 'John,20,90', 'Jony,17,91', 'Jony,17,93', 'Jason,21,85'])
```

## 📎 Ejemplo de salida:

```py
[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Jason', '21', '85'), ('Tom', '19', '80')]
```

## 💡 Pistas:

+ Utilizamos `itemgetter` para habilitar múltiples claves de orden.

+ Observa que la salida es una lista con tuplas en su interior.
