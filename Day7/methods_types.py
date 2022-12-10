class Bird:

    wings = True

    def __init__(self,color,species):
        self.color = color
        self.species = species

    def chirp(self):
        print('tweet')

    def fly(self,feet):
        print(f'The bird flies {feet} feet high')
        self.chirp()

    def paint_black(self):
        self.color = 'black'
        print(f'Now the bird is {self.color}')

    @classmethod
    def lay_eggs(cls,number):
        print(f'It laid {number} eggs')
        cls.wings = False
        print(Bird.wings)

    @staticmethod
    def look():
      print('The bird looks')

Bird.look()
Bird.lay_eggs(3)

tweetie = Bird('yellow', 'canary')

tweetie.chirp()
