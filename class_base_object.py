import copy

class Car:
    pass
class Moto:
    pass

toyota = Car()
honda = Car()


print(toyota) #memory address X
print(honda) #memory address Y
print(isinstance(toyota,Car)) #True
print(isinstance(toyota,Moto)) #False
print(toyota.__class__ == honda.__class__)

# 嘗試原型鍊汙染
def hacking(self,color="red",seat=4):
    self.color = color
    self.seat = seat

toyota.__class__.__init__ = hacking
mozda = Car()
print(toyota.__class__ == mozda.__class__) #True

print(mozda) #memory address Z
print(mozda.color) # red
print(mozda.seat) # 4

#print(toyota) #memory address X
#print(toyota.color) # no attribute 'color'
#print(toyota.seat) # no attribute 'seat'