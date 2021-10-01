#
# Python Polymorphism Assignment
#
# Author:   Beatrice Owens

#parent class
class Pet:
    name = ''
    species = ''
    sound = ''

    def intro(self):
        msg = "\nHi. My name is {}, and I'm a {}. {}".format(self.name,self.species,self.sound)
        return msg

#child class
class Cat(Pet):
    name = 'Momo'
    species = 'cat'
    sound = 'Meow'
    adjective = 'sneaky'
    #polymorphism of parent class method
    def intro(self):
        msg = "\nHi. My name is {}, and I'm a {} {}. {}".format(self.name,self.adjective,self.species,self.sound)
        return msg

#another child class
class Bird(Pet):
    name = 'Max'
    species = 'canary'
    sound = 'chirp'
    flying = True

    def intro(self):
        if self.flying:
            msg = "\nHi. I'm a {} named {}, and I can fly! {}".format(self.species,self.name,self.sound)
            return msg
        else:
            msg = "Hi. I'm a {} named {}, and I can't fly. {}".format(self.species,self.name,self.sound)
            return msg
            



if __name__ == "__main__":
    cat = Cat()
    print(cat.intro())

    bird = Bird()
    print(bird.intro())




    
