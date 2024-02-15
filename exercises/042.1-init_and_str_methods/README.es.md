# `042.1` `__init__` and `__str__` methods

Normalmente, al trabajar con clases, te encontrarás con métodos de este estilo `__<método>__`; estos son conocidos como "métodos mágicos". Existen varios de ellos, y cada uno desempeña una función específica. En esta ocasión, nos enfocaremos en aprender dos de los más fundamentales.

El método mágico `__init__` es esencial para la inicialización de objetos dentro de una clase. Se ejecuta automáticamente cuando se crea una nueva instancia de la clase, permitiendo la asignación de valores iniciales a los atributos del objeto. 

El método `__str__` se utiliza para proporcionar una representación de cadena legible de la instancia, permitiendo personalizar la salida cuando se imprime el objeto. Esto es especialmente útil para mejorar la legibilidad del código y facilitar la depuración, ya que define una versión amigable para humanos de la información contenida en el objeto.

## 📎 Ejemplo:

```py
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        return f"{self.name}, {self.age} years old, {self.gender}"

# Create an instance of the Person class
person1 = Person("Juan", 25, "Male")

# Print the information of the person using the __str__ method
print(person1)  # Output: Juan, 25 years old, Male
```

## 📝 Instrucciones:

1. Crea una clase llamada `Book` que tenga los métodos `__init__` y `__str__`.

2. El método `__init__` debe inicializar los atributos `title`, `author` y `year`.

3. El método `__str__` debe devolver una cadena que represente la información de una instancia del siguiente libro de esta manera:

```py
book1 = ("The Great Gatsby", "F. Scott Fitzgerald", 1925)

print(book1)

# Output:
#
# Book Title: The Great Gatsby
# Author: F. Scott Fitzgerald
# Year: 1925
```

## 💡 Pistas:

+ Utiliza el método `__init__` para inicializar los atributos de la instancia.

+ Utiliza el método `__str__` para proporcionar una representación de cadena legible de la instancia.

+ Para hacer saltos de línea dentro de un string puedes usar los siguientes caracteres `\n`.