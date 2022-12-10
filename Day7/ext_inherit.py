class Father:
  def talk(self):
      print('Hello')


class Mother:
    def laugh(self):
        print(' ha ha')

    def talk(self):
        print('How are you?')



class Child(Mother,Father):
    pass

class Grandchild(Child):
    pass


my_grandchild = Grandchild()

my_grandchild.laugh()
my_grandchild.talk()

print(Grandchild.__mro__)