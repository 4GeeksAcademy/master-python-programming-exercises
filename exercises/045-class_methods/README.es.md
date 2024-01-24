# `045` class methods

Un **método de clase** es un método que está vinculado a la clase y no a la instancia de la clase. Toma la clase misma como su primer parámetro, a menudo llamado "cls". Los métodos de clase se definen utilizando el decorador @classmethod.

La característica principal de un método de clase es que puede acceder y modificar atributos a nivel de clase, pero no puede acceder ni modificar atributos específicos de la instancia, ya que no tiene acceso a una instancia de la clase. Los métodos de clase se utilizan a menudo para tareas que involucran a la clase en sí misma en lugar de a instancias individuales.

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

# Creando instancias de Person
person1 = Person("Alice", 25)
person2 = Person("Bob", 16)

# Usando el class method para obtener el número total de personas
total_people = Person.get_total_people()
print(f"Total People: {total_people}")
```

En este ejemplo:

+ El método de clase `get_total_people` devuelve el número total de personas creadas (instancias de la clase Persona).

## 📝 Instrucciones:

1. Crea una clase llamada `MathOperations`.

2. Dentro de la clase, define lo siguiente:

+ Una variable de clase llamada `pi` con un valor de `3.14159`.
+ Un método de clase llamado `calculate_circle_area` que tome un radio como parámetro y devuelva el área de un círculo utilizando la fórmula: `area = π × radio²`.

3. Utiliza el método de clase `calculate_circle_area` para calcular el área de un círculo con un radio de 5.

4. Imprime el resultado. (No es necesario crear ninguna instancia)

## 📎 Ejemplo de entrada:

```py
circle_area = MathOperations.calculate_circle_area(5)
```

## 📎 Ejemplo de salida:

```py
# Circle Area: 78.53975
```

## 💡 Pistas:

+ Recuerda, para crear un método de clase, utiliza el decorador `@classmethod` encima de la definición del método.

+ ¿Atascado? Si tienes alguna pregunta, ponte en contacto con tus profesores, compañeros de clase, o utiliza el canal de Slack `#public-support-full-stack` para aclarar tus dudas.

+ Cuando termines con este ejercicio, añade el `@staticmethod` del ejercicio anterior a tu clase y tómate tu tiempo para entender sus diferencias y el porqué de cada uno.