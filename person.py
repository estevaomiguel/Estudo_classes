class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    @property
    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

    @property
    def email(self):
        print(f"{self.name}@gmail.com")
    @email.setter
    def email(self,new_email):
        name = new_email.split("@")
        self.name = name[0]



Miguel = Person("Miguel", 20)


Miguel.email = "Bruno@gmail.com"

print(Miguel.name)
print(Miguel.display)
print(Miguel.email)


