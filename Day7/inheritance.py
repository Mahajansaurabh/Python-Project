class Animal:
    pass

    def __init__(self,age,color):
     self.age = age
     self.color = color

    def born(self):
     print('This animal has been born')

class Bird(Animal):
    pass


tweetie = Bird(2, 'yellow')

print(tweetie.color)

