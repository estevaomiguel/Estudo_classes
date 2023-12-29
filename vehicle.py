class Vehicle:
    color = "white"
    def __init__(self,name, max_speed, mileage, capacity):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.capacity = capacity

    def seating_capacity(self):
        return f"The seating capacity of {self.name} is {self.capacity}"
    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    def __init__(self, name, max_speed, mileage, capacity=50):
        super().__init__(name,max_speed,mileage, capacity)

    def fare(self):
        total = super().fare()
        total_fare = total + (total*0.1)
        return total_fare


class Car(Vehicle):
    pass

School_bus = Bus("School Volvo", 180, 12)
print(School_bus.color, School_bus.name, "Speed:", School_bus.max_speed, "Mileage:", School_bus.mileage)
print(School_bus.fare())

print(type(School_bus))

