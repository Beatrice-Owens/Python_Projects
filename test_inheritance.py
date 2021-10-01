#
# Python Inheritance Assignment
#
# Author:   Beatrice Owens

class Pet:
    #defining attributes
    name = 'No name provided'
    species = ''
    age = 0

    #initialization
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

#creating child classes
class Cat(Pet):
    breed = ''
    color = ''
    def __init__(self, name, species, age, breed, color):
        super().__init__(name, species, age)
        self.breed = breed
        self.color = color

class Dog(Pet):
    breed = ''
    color = ''
    def __init__(self, name, species, age, breed, color):
        super().__init__(name, species, age)
        self.breed = breed
        self.color = color

animal1 = Cat('Momo', 'cat', 5, 'American Shorthair', 'orange')
animal2 = Dog('Max', 'dog', 13, 'Australian Cattle Dog', 'blue heeler')

print(animal1.breed)
