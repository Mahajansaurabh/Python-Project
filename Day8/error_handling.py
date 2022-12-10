def ask_number():

    while True:

        try:
            number = int(input('Enter a number: '))

        except:

            print('That is not a number')

        else:
            print(f'You have enter number {number}')
            break

    print('Thank You')

ask_number()