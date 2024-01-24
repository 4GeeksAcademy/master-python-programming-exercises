# `042` understanding classes

En Python, una clase es una estructura que te permite organizar y encapsular datos y funcionalidades relacionadas. Las clases son una característica fundamental de la programación orientada a objetos (OOP), un paradigma de programación que utiliza objetos para modelar y organizar el código.

En términos simples, una clase es como un plano o un molde para crear objetos. Un objeto es una instancia específica de una clase que tiene atributos (datos) y métodos (funciones) asociados. Los atributos representan características del objeto, y los métodos representan las acciones que el objeto puede realizar.

## 📎 Ejemplo:

```py
class Student:
    def __init__(self, name, age, grade): # Estos son sus atributos
        self.name = name
        self.age = age
        self.grade = grade

    def introduce(self): # Esto es un método
        return f"Hello! I am {self.name}, I am {self.age} years old, and my current grade is {self.grade}."

    def study(self, hours): # Esto es otro método
        self.grade += hours * 0.5
        return f"After studying for {hours} hours, {self.name}'s new grade is {self.grade}."

student1 = Student("Ana", 20, 80)

print(student1.introduce())
print(student1.study(3))
```

En este código:

+ La clase `Student` tiene un método `__init__` para inicializar los atributos *name*, *age* y *grade* del estudiante.
+ `introduce` es un método que imprime un mensaje presentando al estudiante.
+ `study` es un método que simula el acto de estudiar y actualiza la nota del estudiante.

## 📝 Instrucciones:

1. Para completar este ejercicio, copia el código proporcionado en el ejemplo y pégalo en tu archivo `app.py`. Ejecuta el código y prueba su funcionalidad. Experimenta con modificar diferentes aspectos del código para observar cómo se comporta. Este enfoque práctico te ayudará a comprender la estructura y el comportamiento de la clase `Student`. Una vez que te hayas familiarizado con el código y sus efectos, siéntete libre de pasar al siguiente ejercicio.

## 💡 Pistas:

+ Lee un poco sobre la función interna `__init__`: https://www.w3schools.com/python/gloss_python_class_init.asp

+ Si no comprendes la funcionalidad del parámetro `self` en el código que acabas de copiar, tómate un momento para visitar el siguiente enlace donde encontrarás una explicación detallada: [Entendiendo el parámetro 'self'](https://www.geeksforgeeks.org/self-in-python-class/)
