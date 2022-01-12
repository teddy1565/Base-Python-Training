class Car:
    # constructor
    def __init__(self,color,seat):
        self.color = color
        self.seat = seat
    # Method
    def drive(self):
        # print(f'str') f表示格式化輸出
        print(f"My car is {self.color} and has {self.seat} seats.")

toyota = Car("Red",16)
toyota.drive()