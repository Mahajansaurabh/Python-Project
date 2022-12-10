user_name = input("Enter user name: ")
print(
    'Well ' + user_name + ', I\'ve thought of a number between 1 and 100 and you have only eight tries to guess it. What number do you think it is?')

# ✅ Take multiple string inputs using for loop
number = []

for _ in range(8):
    number.append(input('Choose a number: '))
    print(number)

if number < 1 or number > 100:
    print(' Number is out of play')
elif number < random(secret_number):
    print('Answer is wrong,chosen a lower number than the secret number')
    elif number > random(secret_number):
    print("The chosen number is greater")
    else number == random(secret_number):
        print('You have won')


