<!-- hide -->
<div align="center">

# Domina Python Practicando (interactivo)

[![Tutorial certificado](https://img.shields.io/badge/4Geeks-tutorial%20certificado-2563eb)](https://4geeks.com/es/interactive-exercise/practice-python)
[![Autocorregido con LearnPack](https://img.shields.io/badge/LearnPack-43%20ejercicios%20autocorregidos-2563eb)](https://learnpack.co)
[![Abrir en GitHub Codespaces](https://img.shields.io/badge/Abrir%20en-GitHub%20Codespaces-fb5a1f?logo=github)](https://codespaces.new/?repo=4GeeksAcademy/master-python-programming-exercises)

</div>
<!-- endhide -->

Domina Python Practicando es un tutorial interactivo con 47 ejercicios de código que resuelves dentro de VS Code, más una página de bienvenida. 43 se corrigen solos con pytest y todos traen una solución de referencia. Se completa en unas 10 horas y va de la aritmética con enteros y el manejo de dígitos a las expresiones regulares, los generadores y la programación orientada a objetos con herencia, métodos estáticos y métodos de clase.

<!-- hide -->
## 📋 Sobre este tutorial

- **Dificultad**: declarada como `easy` en [learn.json](https://github.com/4GeeksAcademy/master-python-programming-exercises/blob/HEAD/learn.json), aunque el rango es amplio: el ejercicio 001 es un solo `print()` y el 045 es un método de clase con una variable de clase.
- **Duración**: 10 horas (`"duration": 10` en learn.json).
- **Ejercicios**: 48 carpetas dentro de [`exercises/`](https://github.com/4GeeksAcademy/master-python-programming-exercises/tree/HEAD/exercises) — 1 página de bienvenida y 47 ejercicios de código.
- **Corrección automática**: sí, `"graded": true`. 43 de los 47 ejercicios de código incluyen una batería de tests `test.py`.
- **Tecnologías**: Python 3 (el dev container fija la 3.10), pytest 6.2.5, pytest-testdox, mock y LearnPack sobre Node.js 22.
- **Soluciones en vídeo**: no hay (`"videoSolutions": false`), pero los 47 ejercicios de código traen un archivo `solution.hide.py`.
- **Instrucciones disponibles en**: [English](https://github.com/4GeeksAcademy/master-python-programming-exercises/blob/HEAD/README.md) y [Español](https://github.com/4GeeksAcademy/master-python-programming-exercises/blob/HEAD/README.es.md) — las 48 carpetas llevan `README.md` y `README.es.md`.
<!-- endhide -->

## 🎯 ¿Qué vas a aprender?

Los ejercicios están ordenados para que cada bloque se apoye en el anterior:

- **Aritmética con enteros y decimales**: división entera `//`, módulo `%`, potencia `**`, `round()` y el módulo `math` (importado en 6 de las soluciones de referencia).
- **Manejo de dígitos sin pasar por texto**: sacar la cifra de las decenas, sumar los dígitos de un número de tres cifras, intercambiar dígitos, leer la cifra que va justo después de la coma decimal.
- **Listas, tuplas y diccionarios**: construir un diccionario de cuadrados, generar una matriz de dos dimensiones, convertir un número indefinido de argumentos en una lista y en una tupla a la vez, contar la frecuencia de palabras.
- **Ordenación por varias claves**: `from operator import itemgetter` para ordenar tuplas `(nombre, edad, nota)` por tres criterios con prioridad.
- **Bases numéricas**: convertir cadenas binarias de 4 dígitos con `int(binario, 2)`.
- **Expresiones regulares**: `import re` y `re.search()` para validar una contraseña contra seis reglas a la vez.
- **Generadores**: una clase con una función generadora que usa `yield` para recorrer los múltiplos de 7.
- **Programación orientada a objetos**: `__init__`, `__str__`, herencia con `super()`, polimorfismo sobrescribiendo un método del padre, `@staticmethod` y `@classmethod` con variables de clase.

Hay dos temas que no aparecen: no se toca el manejo de errores con `try`/`except` ni la lectura o escritura de ficheros en ninguna de las 48 carpetas (comprobado en todos los `README.md`, `app.py` y `solution.hide.py`). La recursividad y `async` tampoco salen.

## 👀 ¿Qué vas a construir?

47 programas pequeños en Python, cada uno en su carpeta numerada. Los tres bloques:

**Ejercicios 001 a 022 — 23 problemas numéricos** (la carpeta `006.1` desdobla uno de ellos). Escribes `digits_sum()`, que debe devolver 17 para la entrada 854; `day_of_week()`, que devuelve 4 para el día 1 de un año que empieza en jueves; `digital_clock()`, que convierte 150 minutos después de medianoche en `(2, 30)`; `square_root()`, que devuelve `7.07` para 50; además de un factorial, un cálculo de siglo, un reparto de manzanas y una ruta de coche.

**Ejercicios 023 a 041 — 19 problemas de estructuras de datos y algoritmos** (dos de ellos, el `024` y el `039`, ya te piden escribir una clase). `two_dimensional_list(3, 5)` tiene que devolver `[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]`. `divisible_binary("0100,0011,1010,1001")` tiene que devolver la cadena `"1010"`. `computed_value(9)` tiene que devolver 11106, la suma de 9 + 99 + 999 + 9999. `net_amount("D 300 D 300 W 200 D 100")` tiene que devolver 500. `valid_password("ABd1234@1")` tiene que devolver exactamente la cadena `"Valid password"`. `compute_robot_distance(["UP 5", "DOWN 3", "LEFT 3", "RIGHT 2"])` tiene que devolver 2. Y `compute_word_frequency()` tiene que informar `Python:5` para la frase de ejemplo.

**Ejercicios 042 a 045 — 5 ejercicios de orientación a objetos.** Construyes una clase `Student`, le añades `__init__` y `__str__` a una clase `Book`, extiendes `Student` en un `CollegeStudent` con un atributo `major` y un método `attend_lecture()`, y terminas con una clase `MathOperations` con un `add_numbers()` estático y un método de clase `calculate_circle_area()` que devuelve `78.53975` para un radio de 5.

## 🎓 ¿Qué necesitas antes de empezar?

No necesitas instalar nada si abres el repositorio en GitHub Codespaces: el dev container ya provisiona Python 3.10, Node.js 22, pytest y el plugin de Python de LearnPack.

Lo que sí necesitas es Python previo: esta es la cuarta y última serie de un recorrido, y la página de bienvenida te remite a las tres anteriores.

- [Python para principiantes](https://github.com/4GeeksAcademy/python-beginner-programming-exercises) — variables, `print()`, condicionales.
- [Practica funciones](https://github.com/4GeeksAcademy/python-functions-programming-exercises) — parámetros, valores de retorno, ámbito.
- [Practica bucles y listas](https://github.com/4GeeksAcademy/python-lists-loops-programming-exercises) — `for`, `while`, manejo de listas.

Si ya sabes declarar una función y recorrer una lista, puedes empezar por aquí sin más. El ejercicio 001 sigue siendo un `print("Hello World")` a secas, así que la entrada es suave.

## ✅ ¿Cómo funciona la corrección automática?

Cada ejercicio corregido lleva un `test.py` escrito con pytest. Cada comprobación va etiquetada con `@pytest.mark.it("...")` y `pytest-testdox` imprime esas etiquetas como frases legibles, así que un fallo te dice qué se esperaba en vez de soltarte un traceback.

Las baterías comprueban dos cosas distintas según el ejercicio:

- **Valores devueltos.** En `013-sum_of_digits` los tests verifican que `digits_sum` existe y es invocable, que devuelve algo, que el tipo devuelto es `int` y, por último, que `digits_sum(854) == 17`.
- **Lo que se imprime.** En `001-hello_world` el test captura la salida estándar y la compara carácter a carácter con `"Hello World\n"`.

Cuatro ejercicios no tienen `test.py` y son práctica libre: `031-sum-eigth-digit`, `033-number-of-uppercase`, `035-square-each-odd-number` y `039-class-that-iterates`. Es decir, 43 corregidos de 47.

> 💡 La corrección es estricta a propósito, y los propios mantenedores del repositorio lo advierten: toma un test en rojo como una pista sobre la forma que se espera de tu respuesta, no como un veredicto sobre tu lógica.

## 💡 ¿Qué errores conviene evitar?

- **Imprimir cuando el test espera un `return`.** La mayoría de las baterías llaman a tu función y miran el valor que devuelve. `digits_sum(854)` tiene que *devolver* 17; imprimir 17 falla la comprobación de tipo.
- **Fiarte del enunciado en vez del test en los ejercicios 019 y 030.** Las instrucciones de `019-digital_clock` dicen que la función debe *imprimir* dos números, pero su test comprueba `digital_clock(194) == (3, 14)`. La misma trampa está en `030-divisable-binary`: el enunciado dice *imprimir* los números divisibles entre 5, mientras que el test comprueba `divisible_binary("0100,0011,1010,1001") == "1010"`. En los dos hay que devolver el valor.
- **Formatear el ejercicio 041 línea a línea.** El enunciado pide una clave por línea, pero el test compara la salida contra una sola línea: `"2:2 3.:1 3?:1 New:1 Python:5 Read:1 and:1 between:1 choosing:1 or:2 to:1\n"`. Fíjate en que no hay espacio después de los dos puntos.
- **Olvidar `import re` en el ejercicio 037**, y olvidar que las reglas de la contraseña incluyen *los dos* límites: mínimo 6 caracteres y máximo 12. La cadena de fallo tiene que ser exactamente `"Invalid password. Please try again"`.
- **Cambiar filas por columnas en el ejercicio 026.** `two_dimensional_list(3, 5)` devuelve 3 filas de 5 elementos, no 5 filas de 3.
- **Redondear con la precisión equivocada.** El ejercicio 021 se queda con dos decimales (`square_root(50)` da `7.07`); el 040 redondea la distancia del robot al entero más cercano.
- **Confundir métodos estáticos con métodos de clase.** Un `@staticmethod` (ejercicio 044) no recibe ni `self` ni `cls` y no puede leer el estado de la clase; un `@classmethod` (ejercicio 045) recibe `cls`, y eso es lo que permite que `calculate_circle_area()` llegue a la variable de clase `pi`.
- **Cambiarle el nombre a la función.** La primera comprobación de casi todas las baterías es `assert callable(app.<nombre>)`, así que una errata en el nombre tumba todo lo que viene detrás.

## ❓ Preguntas frecuentes

### ¿Cuánto se tarda en terminar estos ejercicios de Python?

El tutorial declara 10 horas. Repartidas entre 47 ejercicios de código salen unos 13 minutos de media, pero la distribución es desigual: el bloque numérico (001–022) va rápido en cuanto dominas `//` y `%`, mientras que los de expresiones regulares, ordenación y objetos cuestan bastante más.

### ¿Hace falta saber Python antes de empezar?

Algo sí. Esta es la última serie de un recorrido de cuatro, y la página de bienvenida da por sabidos las variables, las funciones, los bucles y las listas. No necesitas base de orientación a objetos: la teoría se explica desde cero en el ejercicio 042, con un ejemplo resuelto de la clase `Student` antes de pedirte que escribas nada. Eso sí, avisamos: hay dos ejercicios anteriores que ya dan por hecho que sabes escribir una clase casi sin explicación previa, el `024-class-with-two-methods` (que además está corregido) y el `039-class-that-iterates`.

### ¿Es gratis y puedo reutilizar el contenido?

Abrirlo y resolverlo no cuesta nada. Reutilizar el contenido sí tiene condiciones: [LICENSE.md](https://github.com/4GeeksAcademy/master-python-programming-exercises/blob/HEAD/LICENSE.md) reserva todos los derechos de propiedad intelectual y prohíbe expresamente republicar, vender, sublicenciar, reproducir o redistribuir el material. No es una licencia de código abierto. El Python que escribas en tus propios `app.py` es tuyo.

### ¿Tengo que instalar algo en mi ordenador?

No. Abrir el repositorio en Codespaces te da un entorno listo. La instalación local también es posible y está documentada más abajo: necesita Python 3, Node.js y el plugin de Python de LearnPack.

### ¿Hay soluciones en vídeo?

No. `learn.json` pone `videoSolutions` en `false`. Lo que sí tienes es un archivo `solution.hide.py` en cada una de las 47 carpetas de código, además de las pistas al final de la mayoría de los ejercicios (39 de las 48 carpetas llevan sección de pistas), que enlazan a referencias externas como las lecciones de snakify sobre números enteros y decimales.

### ¿Sigue mereciendo la pena practicar algoritmos así?

Los ejercicios apuntan a la mecánica que una entrevista o una revisión de código siguen mirando: razonar con división entera en lugar de convertir a texto, elegir el contenedor adecuado, ordenar por varias claves y entender por qué un método está atado a la clase y no a la instancia. Eso no caduca. Lo que esta serie no enseña es manejo de errores, ficheros ni ninguna librería de terceros.

<!-- hide -->
## 🚀 Cómo empezar

El camino más rápido es un clic: [abrir este tutorial en GitHub Codespaces](https://codespaces.new/?repo=4GeeksAcademy/master-python-programming-exercises). También existe la alternativa de [Gitpod](https://gitpod.io#https://github.com/4GeeksAcademy/master-python-programming-exercises).

Cuando se abra VS Code, los ejercicios de LearnPack deberían arrancar solos. Si no lo hacen, ejecuta esto en la terminal:

```bash
learnpack start
```

## 💻 Instalación local

1. Instala LearnPack y el plugin de Python, con las mismas versiones que provisiona el dev container:

```bash
npm i @learnpack/learnpack@5.0.348 -g && learnpack plugins:install @learnpack/python@1.0.6
```

2. Clona el repositorio y entra en él:

```bash
git clone https://github.com/4GeeksAcademy/master-python-programming-exercises.git
cd master-python-programming-exercises
```

3. Instala las dependencias de test y arranca el tutorial desde la misma carpeta donde está `learn.json`:

```bash
pip3 install pytest==6.2.5 pytest-testdox mock
learnpack start
```

## 📚 Cómo están organizados los ejercicios

Cada ejercicio es una carpeta dentro de `exercises/` y contiene hasta cinco archivos:

- `app.py` — el archivo que editas y el que ejecuta el ordenador. Está en los 47 ejercicios de código.
- `README.md` — las instrucciones, en inglés.
- `README.es.md` — las mismas instrucciones en español. Está en las 48 carpetas.
- `test.py` — la batería de pytest. No hace falta que lo abras. Está en 43 carpetas.
- `solution.hide.py` — una solución de referencia. Está en los 47 ejercicios de código.

La carpeta `000-welcome` solo tiene los dos READMEs: es la página de introducción, no un ejercicio.

¿Encuentras un fallo o una errata? Abre una incidencia en [este repositorio](https://github.com/4GeeksAcademy/master-python-programming-exercises/issues) — los ejercicios se construyeron en colaboración y los reportes son bienvenidos.

## 🤝 Colaboradores

Gracias a estas personas ([leyenda de emojis](https://github.com/kentcdodds/all-contributors#emoji-key)):

- [Alejandro Sánchez (alesanchezr)](https://github.com/alesanchezr) — código 💻, idea 🤔, tests ⚠️, revisión de pull requests 👀, construcción del tutorial ✅, documentación 📖
- [Paolo (plucodev)](https://github.com/plucodev) — reportes de fallos 🐛, código 💻, traducción 🌎
- [Marco Gómez (marcogonzalo)](https://github.com/marcogonzalo) — reportes de fallos 🐛, traducción 🌎

Y a [todo el mundo que aparece en el gráfico de colaboradores](https://github.com/4GeeksAcademy/master-python-programming-exercises/graphs/contributors). Este proyecto sigue la especificación [all-contributors](https://github.com/kentcdodds/all-contributors) y toda contribución es bienvenida.

Este tutorial es uno de tantos construidos por alumnos y profesores de [4Geeks Academy](https://4geeks.com).
<!-- endhide -->
