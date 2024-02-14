# `044` static methods

Un **método estático** en Python es un método que está vinculado a una clase en lugar de a una instancia de la clase. A diferencia de los métodos regulares, los métodos estáticos no tienen acceso a la instancia o a la clase en sí.

Los métodos estáticos se utilizan a menudo cuando un método en particular no depende del estado de la instancia o de la clase. Son más parecidos a funciones de utilidad asociadas con una clase.

```py
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def is_adult(age):
        return age >= 18

# Creando instancias de Person
person1 = Person("Alice", 25)
person2 = Person("Bob", 16)

# Usando el static method para verificar si una persona es adulta
is_adult_person1 = Person.is_adult(person1.age)
is_adult_person2 = Person.is_adult(person2.age)
print(f"{person1.name} is an adult: {is_adult_person1}")
print(f"{person2.name} is an adult: {is_adult_person2}")
```

En este ejemplo:

+ El método estático `is_adult` verifica si una persona es adulta según su edad. No tiene acceso a variables de instancia o de clase directamente.

## 📝 Instrucciones:

1. Crea una clase llamada `MathOperations`.

2. Crea un método estático llamado `add_numbers` que tome dos números como parámetros y devuelva su suma.

3. Crea una instancia de la clase `MathOperations`.

4. Utiliza el método estático `add_numbers` para sumar dos números, por ejemplo, 10 y 15.

5. Imprime el resultado.

## 📎 Ejemplo de entrada:

```py
math_operations_instance = MathOperations()
sum_of_numbers = MathOperations.add_numbers(10, 15)
```

## 📎 Ejemplo de salida:

```py
# Sum of Numbers: 25
```

## 💡 Pistas:

+ Recuerda, para crear un método estático, utiliza el decorador `@staticmethod` encima de la definición del método.

+ Cualquier cosa que aún no entiendas completamente, te animamos a que siempre utilices las herramientas que te ofrece internet para buscar información y aclarar la mayoría de tus dudas (todos los desarrolladores hacen esto, no te preocupes).
