class Human:
    def walk(self):
        pass

    def eat(self):
        pass


class Animal:
    def walk(self):
        pass


class Dog(Animal):
    def talk(self):
        return ("Auff")


class Cat(Animal):
    def talk(self):
        return ("Miau")


human = Human()
human.eat()

pet1 = Dog()
pet1.walk()

pet2 = Cat()
pet3 = Cat()
pet4 = Cat()

pet2.walk()

print(pet1.talk())
print(pet2.talk())


# Class Car, Moto, Bus, Truck, Vehicle
#===============================================================
class Vehicle:
    pass

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

v4= Truck()
print(v4.wheels())