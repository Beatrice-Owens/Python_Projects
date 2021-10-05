
#creating class Car
class Car:
    def __init__(self, color, speed):
        self._color = color #single "_" still functions normally
        self.__speed = speed #double "_" is more restrictive 

    def get_Speed(self): #creating a method to obtain and give the value of __speed
        print('Getting value...') #added print line to see that the code was being executed
        return self.__speed
        
    def set_Speed(self, value): #creating a method to set the value of __speed
        print('Setting Value...') #added print line to see that the code was being executed
        self.__speed = value

        

honda = Car('black', 300) #instatiating the object

print(honda.get_Speed())

honda.set_Speed(400)

print(honda.get_Speed())

print(honda._color) #color is not double "_", so it doesn't need a get/set method
