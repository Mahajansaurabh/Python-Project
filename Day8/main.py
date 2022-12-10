from numbers import drug_store


def area():
    print('Choose area: ')

Perfume =input("Please press  first option:\n")
Medicine =input("Please press  second option:\n")
Cosmetics =input("Please press third option:\n")

v1 =str(Perfume)
v2 =str(Medicine)
v3 = str(Cosmetics)

numbers = count(int(numbers))

choice =input("Enter 1 for Perfume.\nEnter 2 for Medicine.\nEnter 3 for Cosmetics:\n")
choice =int(choice)
if choice ==1:
 print(f'You entered {v1} \n Please proceed to Perfume section ')
 print(f'P - int{} ')
elif choice ==2:
 print(f'You entered {v2} \n Please proceed to Medicine section')
 print('M - int{}')
elif choice == 3:
 print(f'You entered {v3} \n Please proceed to Cosmetics section ')
 print('C - int{}')