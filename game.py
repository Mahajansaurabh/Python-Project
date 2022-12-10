#snake water gun
import random
def game(comp,you):
    if comp == you:
        return None
    elif comp == 's':
        if you=='w':
            return  False
        elif you=='g':
            return True
        elif comp == 'w':
            if you== 'g':
                return False
        elif you=='s':
                return True
        elif comp == 'g':
            if you== 's':
                return False
        elif you=='w':
                return True


comp = input("Comp Turn : Snake(s) Water(w) or Gun(g)?")
randomNo = random.randint(1,3)
print(randomNo)
if randomNo == 1:
    comp = 's'
elif randomNo == 2:
    comp = 'w'
elif randomNo == 3:
    comp = 'g'

you = input("Your Turn : Snake(s) Water(w) or Gun(g)?")

game(comp,you)
print(f'Computer chose {comp}')
print(f'You chose {you}')
if comp == None:
    print("The game is a tie!")
elif comp :
    print('You Win!')
else:
    print('You Lose!')