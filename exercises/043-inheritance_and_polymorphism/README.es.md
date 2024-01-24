# `043` Inheritance and polymorphism

Ahora que entendemos qué es una clase y algunas de sus características, hablemos sobre dos nuevos conceptos relacionados con las clases: herencia y polimorfismo. Considera el siguiente ejemplo:

```py
class HighSchoolStudent(Student):  # Agrega la clase padre dentro de los paréntesis
    def __init__(self, name, age, grade, specialization):
        super().__init__(name, age, grade)
        self.specialization = specialization

    def study(self, hours):
        return f"{self.name} is a high school student specializing in {self.specialization} and is studying for {hours} hours for exams."

# Creando una instancia de HighSchoolStudent
high_school_student = HighSchoolStudent("John", 16, 85, "Science")
print(high_school_student.introduce())  # Podemos llamar a este método gracias a la herencia
print(high_school_student.study(4))  # Este método ha sido ligeramente modificado y ahora retorna un string diferente
```

Suponiendo que la clase `Student` del ejercicio anterior está definida justo encima de esta clase `HighSchoolStudent`, para heredar sus métodos y atributos, simplemente incluimos el nombre de la clase que queremos heredar (la clase padre) dentro de los paréntesis de la clase hija (`HighSchoolStudent`). Como puedes ver, ahora podemos usar el método `introduce` de la clase `Student` sin tener que codificarlo nuevamente, haciendo nuestro código más eficiente. Lo mismo se aplica a los atributos; no necesitamos redefinirlos.

Además, tenemos la flexibilidad de agregar nuevos métodos exclusivamente para esta clase o incluso sobreescribir un método heredado si es necesario, como se demuestra en el método `study` que está ligeramente modificado con respecto a la clase `Student`; esto se llama **polimorfismo**.

## 📝 Instrucciones:

1. Crea una clase llamada `CollegeStudent` que herede de la clase `Student` ya definida.

2. Agrega un nuevo atributo llamado `major` para representar la carrera que están estudiando.

3. Modifica el método heredado `introduce` para retornar este string:

```py
"Hi there! I'm <name>, a college student majoring in <major>."
```

4. Agrega un nuevo método llamado `attend_lecture` que retorne el siguiente string:

```py
"<name> is attending a lecture for <major> students."
```

5. Crea una instancia de tu nueva clase y llama a cada uno de sus métodos. Ejecuta tu código para asegurarte de que funcione.


## 💡 Pista:

+ Puede que hayas notado el uso de un nuevo método `super()`, que es necesario para heredar de una clase padre. Observa dónde se encuentra ubicado y lee más sobre él aquí: [Entendiendo super() en Python](https://realpython.com/python-super/).
