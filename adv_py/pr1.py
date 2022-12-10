name = input('Enter your name: ')
marks = input('Enter your marks: ')
phone = input('Enter your phone number: ')

template = 'The name of the students is {}, his marks are {} and phone number is {}'
output = template.format(name,marks,phone)
print(output)