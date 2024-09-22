class Vehicle :
    licenseCode = ""
    serialCode = ""
    face = ""
    def turnOnAirconditioner(self):
        print("Turn On : Air")

class Car(Vehicle) :
    pass
class Pickup(Vehicle) :
    pass
class Van (Vehicle):
    pass
class EstateCar(Vehicle) :
    def Opensunroof(self) :
        print("Open Sunroof")

car1 = Car()
car1.turnOnAirconditioner()
car1.Opensunroof()
pickup1 = Pickup()
pickup1.turnOnAirconditioner()
van1 = Van()
van1.turnOnAirconditioner()
estate1 = EstateCar()
estate1.turnOnAirconditioner()
