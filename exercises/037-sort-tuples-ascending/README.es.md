# `037`sort tuples ascending

## 📝 Instrucciones:

1. Debes escribir un programa para clasificar las tuplas (nombre, edad, altura) en orden ascendente, donde el nombre es una cadena, la edad y la altura son números. Las tuplas son ingresadas por consola. El criterio de clasificación es:

- Ordenar según el nombre; -
- Luego ordenar según la edad;
- Luego ordenar por puntuación.

*La prioridad es ese nombre > edad > puntuación.*

## Entrada de ejemplo:

Si se dan las siguientes tuplas como entrada al programa:

+ Tom,19,80
  Juan,20,90
  Juan, 17, 91
  Juan, 17, 93
  Json,21,85

## Salida de ejemplo:

+ [('Juan', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', ' 21', '85'), ('Tom', '19', '80')]

## 💡 Pista:

+ En caso de que se proporcionen datos de entrada a la pregunta, se debe suponer que se trata de una entrada de consola.

+ Usa `itemgetter` para habilitar varias claves de ordenación (módulo `operator`).