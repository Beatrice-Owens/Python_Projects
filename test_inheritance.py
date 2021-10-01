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
    weight = 0
    markings = ''
    def __init__(self, name, species, age, weight, markings):
        super().__init__(name, species, age)
        self.weight = weight
        self.markings = markings

animal1 = Cat('Momo', 'cat', 5, 'American Shorthair', 'orange')
animal2 = Dog('Max', 'dog', 13, 45, 'Blue Heeler')

print(animal1.breed)
print(animal2.markings)
