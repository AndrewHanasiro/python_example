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
