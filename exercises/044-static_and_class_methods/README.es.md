# `044` static and class methods

Un **método de clase** es un método que está vinculado a la clase y no a la instancia de la clase. Toma la clase misma como su primer parámetro, a menudo llamado "cls". Los métodos de clase se definen utilizando el decorador @classmethod.

La característica principal de un método de clase es que puede acceder y modificar atributos a nivel de clase, pero no puede acceder ni modificar atributos específicos de la instancia, ya que no tiene acceso a una instancia de la clase. Los métodos de clase se utilizan a menudo para tareas que involucran a la clase en sí misma en lugar de a instancias individuales.

Un **método estático** en Python es un método que está vinculado a una clase en lugar de a una instancia de la clase. A diferencia de los métodos regulares, los métodos estáticos no tienen acceso a la instancia o a la clase en sí.

Los métodos estáticos se utilizan a menudo cuando un método en particular no depende del estado de la instancia o de la clase. Son más parecidos a funciones de utilidad asociadas con una clase.

```py
class Person:
    total_people = 0  # Variable de clase para llevar el seguimiento del número total de personas

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.total_people += 1  # Incrementa el recuento de total_people por cada nueva instancia

    @classmethod
    def get_total_people(cls):
        return cls.total_people

    @staticmethod
    def is_adult(age):
        return age >= 18

# Creando instancias de Person
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

# Usando el class method para obtener el número total de personas
total_people = Person.get_total_people()
print(f"Total People: {total_people}")

# Usando el static method para verificar si una persona es adulta
is_adult_person1 = Person.is_adult(person1.age)
is_adult_person2 = Person.is_adult(person2.age)
print(f"{person1.name} is an adult: {is_adult_person1}")
print(f"{person2.name} is an adult: {is_adult_person2}")
```

En este ejemplo:

+ El método de clase `get_total_people` devuelve el número total de personas creadas (instancias de la clase Persona).

+ El método estático `is_adult` verifica si una persona es adulta según su edad. No tiene acceso a variables de instancia o de clase directamente.

## 📝 Instrucciones:

1. Crea una clase llamada `MathOperations`.

2. Dentro de la clase, define lo siguiente:

+ Una variable de clase llamada `pi` con un valor de `3.14159`.
+ Un método de clase llamado `calculate_circle_area` que tome un radio como parámetro y devuelva el área de un círculo utilizando la fórmula: `area = π × radio²`.

3. Crea un método estático llamado `add_numbers` que tome dos números como parámetros y devuelva su suma.

4. Crea una instancia de la clase `MathOperations`.

5. Utiliza el método de clase `calculate_circle_area` para calcular el área de un círculo con un radio de 5.

6. Utiliza el método estático `add_numbers` para sumar dos números, por ejemplo, 10 y 15.

7. Imprime los resultados de cada operación.

## 📎 Ejemplo de entrada:

```py
math_operations_instance = MathOperations()
circle_area = MathOperations.calculate_circle_area(5)
sum_of_numbers = MathOperations.add_numbers(10, 15)
```

## 📎 Ejemplo de salida:

```py
78.53975
25
```

## 💡 Pistas:

+ Recuerda, para crear un método de clase, utiliza el decorador `@classmethod` encima de la definición del método.

+ Recuerda, para crear un método estático, utiliza el decorador `@staticmethod` encima de la definición del método.

+ Cualquier cosa que aún no entiendas completamente, te animamos a que siempre utilices las herramientas que te ofrece internet para buscar información y aclarar la mayoría de tus dudas (todos los desarrolladores hacen esto, no te preocupes).
