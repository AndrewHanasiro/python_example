

# andar frente, virar esquerda, virar a direita, ré*
# combustivel, reabastecer
# grana
# abrir porta mala*
# empinar*
class Vehicle:
    def turn_left(self):
        pass

    def go_forward(self):
        pass

    def turn_right(self):
        pass


class VehicleWithGoBack:
    def go_back(self):
        pass


class Car(Vehicle, VehicleWithGoBack):
    num_wheels = 4

    def wheels(self):
        return self.num_wheels

    def payTax(self, variacao: float):
        return variacao * self.num_wheels


class Moto(Vehicle):
    def __init__(self, num_wheels):
        if num_wheels > 3:
            msg = "não existe moto com {} rodas".format(num_wheels)
            raise Exception(msg)
        self.num_wheels = num_wheels

    def empinar(self):
        if self.num_wheels > 2:
            raise Exception("não da pra empinar com 3 ou mais rodas")
        else:
            print("empianndo")


class Bus(Vehicle):
    def wheels(self):
        return ("8")


class Truck(Vehicle):
    def wheels(self):
        return ("6")


v1 = Car()
v1.turn_left()
v1.go_forward()
v1.go_back()

v2 = Moto(2)
v2.empinar()

v3 = Moto(7)
v3.empinar()
