class Animal():
    def makeSound(self):
        print('Some generic animal sound')

class Dog(Animal):
    def makeSound(self):
        print('Bark')

class Cat(Animal):
    def makeSound(self):
        print('Meow')

class Horse(Animal):
    def makeSound(self):
        print('Neigh')

Animals = [Dog(), Cat(), Horse()]

for animal in Animals:
    animal.makeSound()