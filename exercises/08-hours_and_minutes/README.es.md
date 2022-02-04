# `08` Horas y minutos

La siguiente función nos dirá la hora pasada la medianoche, es decir, suponiendo que es medianoche la función va a recibir por parámetro la cantidad de segundos que han pasado y esto resultará en una hora estimada.
## 📝 Instrucciones:

1. Completa la función para que retorne el resultado esperado.

2. Realiza dos calculos con los segundos que se pasan por parámetro en la función para que uno calcule la hora segun segundos que han pasado y el otro para saber los minutos `(hora , minutos)`


[comment]: <Dado el número entero `N` - el número de segundos que pasan desde la medianoche:
 
 1. ¿cuántas horas y minutos completos han pasado desde la medianoche?

El programa debe imprimir dos números: el número de horas (entre 0 y 23) y el número de minutos (entre 0 y 1339).

Por ejemplo:

* Si N = 3900  han pasado 3900 segundos desde la medianoche ,es decir, ahora es la 1:05 am. 
 
El programa debe imprimir 1 65  1 hora completa ha pasado desde la medianoche, 65 minutos completos han pasado desde la medianoche.>


## Ejemplo de entrada:
```py
3900
```
## Ejemplo de salida:
```py
(1, 65)
```
## 💡 Pista:

+ Recuerda cuantos segundos hay en una hora y cuantos segundos en un minuto.

+ Si no sabes cómo empezar la solución a esta asignación, por favor, revisa la teoría en esta lección:
https://snakify.org/lessons/print_input_numbers/

+ También puedes intentar paso a paso con trozos de la teoría:
https://snakify.org/lessons/print_input_numbers/steps/1/


[comment]: <Solution: (secs//3600, secs//60)>