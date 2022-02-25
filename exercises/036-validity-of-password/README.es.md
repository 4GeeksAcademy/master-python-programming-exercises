# `036` validity of password

## 📝 Instrucciones:

1. Un sitio web requiere que los usuarios ingresen el nombre de usuario y la contraseña para registrarse. Escribe un programa para verificar la validez de la contraseña ingresada por los usuarios. Los criterios para verificar la contraseña son los siguientes:

- Al menos 1 letra entre [a-z].
- Al menos 1 número entre [0-9].
- Al menos 1 letra entre [A-Z].
- Al menos 1 carácter de [$#@].
- Longitud mínima de la contraseña de transacción: 6.
- Longitud máxima de la contraseña de transacción: 12.


*Tu programa debe aceptar una secuencia de contraseñas separadas por comas y las verificará de acuerdo con los criterios anteriores. Las contraseñas que coincidan con los criterios deben imprimirse, cada una separada por una coma.*

## Ejemplo de entradaE:

```pía
ABd1234@1,a F1#,2w3E*,2We3345
```

## Ejemplo de salida:

```pía
ABd1234@1
```
 
## 💡 Pista:

+ En caso de que se proporcionen datos de entrada a la pregunta, se debe suponer que se trata de una entrada de consola. 