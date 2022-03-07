# `08` Horas y minutos

En este ejercicio vamos a suponer que es medianoche, queremos que con la función `hours_minutes` que hemos provisto para tí nos digas cuánto tiempo han pasado desde entonces con los segundos que se introduzcan como parámetro.

## 📝 Instrucciones:

1. Completa la función para que retorne el resultado esperado.

2. Realiza dos calculos con los segundos que se pasan por parámetro en la función para que uno calcule la hora segun segundos que han pasado y el otro para saber los minutos `(hora , minutos)`

## Ejemplo de entrada:
```py
3900 # 1

60 # 2
```
## Ejemplo de salida:
```py
(2, 5) # 1

(0, 1) # 2
```
## 💡 Pista:

+ Recuerda cuantos segundos hay en una hora (3600) y cuantos segundos en un minuto (60).

+ Si no sabes cómo empezar la solución a esta asignación, por favor, revisa la teoría en esta lección:
https://snakify.org/lessons/print_input_numbers/

+ También puedes intentar paso a paso con trozos de la teoría:
https://snakify.org/lessons/print_input_numbers/steps/1/


[comment]: <Solution: (secs//3600, secs//60)>