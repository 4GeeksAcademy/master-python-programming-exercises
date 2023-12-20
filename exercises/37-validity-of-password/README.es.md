# `37` Validity of password

## 📝 Instrucciones:

Un sitio web requiere que los usuarios ingresen un nombre de usuario y una contraseña para registrarse. Escribe una función llamada `valid_password()` para verificar la validez de la contraseña ingresada por los usuarios. A continuación, se detallan los criterios para verificar la contraseña:

1. Al menos 1 letra entre [a-z].
2. Al menos 1 número entre [0-9].
3. Al menos 1 letra entre [A-Z].
4. Al menos 1 carácter de [$#@].
5. Longitud mínima de la contraseña: 6.
6. Longitud máxima de la contraseña: 12.

Tu programa debería aceptar una secuencia de contraseñas separadas por comas y verificarlas según los criterios anteriores. Las contraseñas que cumplan con los criterios deben imprimirse, cada una separada por una coma.

## 📎 Ejemplo de entrada:

```text
valid_password("ABd1234@1,a F1#,2w3E*,2We3345")
```

## 📎 Ejemplo de salida:

```text
ABd1234@1
```

## 💡 Pistas:

+ Lee sobre expresiones regulares en Python.

+ Necesitarás importar el módulo 're' (regular expressions) para poder usar la función `search()`.

+ Para importarlo, copia y pega lo siguiente al inicio de tu archivo `import re`.
