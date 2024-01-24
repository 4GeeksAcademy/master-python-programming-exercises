# `030` Divisable binary

## 📝 Instrucciones:

1. Escribe la función `divisible_binary()` que tome una secuencia de números binarios de 4 dígitos separados por comas como entrada y verifique si son divisibles por 5. Imprime los números que son divisibles por 5 en una secuencia separada por comas.

## 📎 Ejemplo de entrada:

```py
divisible_binary("0100,0011,1010,1001")
```

## 📎 Ejemplo de salida:

```py
1010
```

## 💡 Pista:

+ Para convertir números binarios en nuestros números enteros cotidianos (base 10 o decimal), es necesario incluir la base del número que ingresamos en el primer argumento (en este caso, base 2 o binario), y la función `int()` se encargará del resto. Sería así:

```py
binary = '0101'
decimal = int(binary, 2)

print(decimal)  # Output: 5
```
