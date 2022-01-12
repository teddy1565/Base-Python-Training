class Door:
    def __init__(self,name,lock=True):
        self.lock = lock
        self.name = name
    def __str__(self):
        state = self.getState()
        return f"{self.name}:鎖定狀態:{state}"
    def getState(self):
        return self.lock
    def changeState(self):
        self.lock = not self.lock
class Car(Door):
    class CarDoor:
        def __init__(self,Doors=[Door("左前方"),Door("右前方")]):
            self.Door = Doors
        def __str__(self):
            report = ""
            for i in self.Door:
                report = report + f"{i}" + "\n"
            return report

    def __init__(self,color,seat):
        self.color = color
        self.seat = seat
        self.Doors = self.CarDoor()

    def drive(self):
        print("車門狀態:")
        print(self.Doors)
        print(f"車子顏色:{self.color}")
        print(f"車子座位:{self.seat}")

Toyota = Car("Red",4)
Toyota.drive()