class Dog:
    species = "Canis Familiaris"
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__price = 500

    def __repr__(self):
        return f"{self.name} is {self.age} years old!"

    def speak(self, sound="rouf"):
        return f"{self.name} says {sound}"

    def setPrice(self, n_price):
        self.__price = n_price
        return self.__price


class Golden(Dog):
    def __init__(self, name, age):
        super().__init__(name, age)

    def speak(self, sound="Arf"):
        return super().speak(sound)

miles = Dog("Miles", 5)

print(miles)
print(miles.speak())
print(isinstance(miles, Dog))

rudolf = Golden("Rudolf", 8)
print(rudolf)
print(rudolf.speak())


print(miles.setPrice(400))
