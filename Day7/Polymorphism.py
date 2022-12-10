class Cow:

    def __init__(self,name):
        self.name = name

    def talk(self):
        print(self.name+' moos')

class Sheep:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(self.name + ' bleats')

cow1 = Cow('Mandy')
sheep1 = Sheep('Cloud')



def animal_talks (animal):
    animal.talk()

animal_talks(sheep1)
