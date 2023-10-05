class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small
        self.b = 0
        self.m = 0
        self.s = 0

    def addCar(self, carType):
        if carType == 1 and self.b < self.big:
            self.b += 1
            return True
        elif carType == 2 and self.m < self.medium:
            self.m += 1
            return True
        elif carType == 3 and self.s < self.small:
            self.s += 1
            return True
        else:
            return False

# tests
obj = ParkingSystem(1,1,0)
print(obj.addCar(1))
print(obj.addCar(2))
print(obj.addCar(3))
print(obj.addCar(1))
