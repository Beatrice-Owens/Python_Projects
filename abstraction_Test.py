
#import from abc to be able to use abstract methods
from abc import ABC, abstractmethod

#create a class
class Animal(ABC):
    def favAnimal(self, val): #regular method
        print("Your favorite animal is the",val)

    @abstractmethod #abstract method unimplemented
    def ownAnimal(self, val):
        pass

#child class where I implement the ownAnimal() from the Animal class
class animalOwnership(Animal):
    def ownAnimal(self, val):
        print("I'm sorry, but you can't own a(n) {}.".format(val))

#create an object
obj = animalOwnership()
obj.favAnimal('Tiger')
obj.ownAnimal('Tiger')
