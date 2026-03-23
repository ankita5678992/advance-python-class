class Vehicle:
    total = 0

    def rent(self):
        Vehicle.total += 1


class Car(Vehicle):
    def rent(self, days):
        super().rent()
        return days * 1000


class Bike(Vehicle):
    def rent(self, days):
        super().rent()
        return days * 300


class Truck(Vehicle):
    def rent(self, days):
        super().rent()
        return days * 2000


c = Car()
print("Car Rent:", c.rent(2))

b = Bike()
print("Bike Rent:", b.rent(3))

print("Total rented:", Vehicle.total)