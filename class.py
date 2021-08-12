


# Class Car, Moto, Bus, Truck, Vehicle
#===============================================================
class Vehicle:
    def walk(self):
        return("andou")

class Car(Vehicle):
    def wheels(self):
        return ("4")

class Moto(Vehicle):
    def wheels(self):
        return ("2")

class Bus(Vehicle):
    def wheels(self):
        return ("8")

class Truck(Vehicle):
    def wheels(self):
        return ("6")

v1 = Car()
print(v1.wheels())

v2 = Moto()
print(v2.wheels())

v3 = Bus()
print(v3.wheels())
print(v3.walk())

v4= Truck()
print(v4.wheels())