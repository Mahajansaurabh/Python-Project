class Animal:

    def __init__(self,age,color):
        self.age = age
        self.color = color

    def born(self):
        print('This animal has been born')

    def Talk(self):
        print('This animal makes a sound')

class Bird(Animal):

    def __init__(self,age,color,altitude):
       super().__init__(age,color)
        

    def talk(self):
        print('chirp')

    def fly(self,feet):
        print(f'This bird flies {feet} feet')

tweetie = Bird(3,'yellow',196)

tweetie.fly(328)
my_animal = Animal(5,'black')
