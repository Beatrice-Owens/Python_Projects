#
# Python Polymorphism Assignment
#
# Author:   Beatrice Owens

#parent class
class Pet:
    name = 'Max'
    species = 'canary'
    sound = 'chirp'

    def intro(self):
        msg = "\nHi. My name is {}, and I'm a {}. {}".format(self.name,self.species,self.sound)
        return msg

#child class
class Cat(Pet):
    weight = '1'
    adjective = 'plump'
    #polymorphism of parent class method
    def intro(self):
        msg = "\nHi. My name is {}, and I'm a {} {}lb(s) {}. {}".format(self.name,self.adjective,self.weight,self.species,self.sound)
        return msg

#another child class
class Bird(Pet):
    color = 'yellow'
    flying = True

    def intro(self):
        if self.flying:
            msg = "\nHi. I'm a(n) {} {} named {}, and I can fly!".format(self.color,self.species,self.name)
            return msg
        else:
            msg = "Hi. I'm a(n) {} {} named {}, and I can't fly.".format(self.color,self.species,self.name)
            return msg
            



if __name__ == "__main__":
    cat = Cat()
    print(cat.intro())

    bird = Bird()
    print(bird.intro())




    
