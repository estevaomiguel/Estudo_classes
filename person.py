class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

class Student(Person):
    def __init__(self, name, age, section):
        super().__init__(name, age)
        self.section = section

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Section: {self.section}")

Miguel = Student("Miguel", 20, "Mathematics")
Miguel.display()
