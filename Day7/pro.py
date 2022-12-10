class Person:
    def __int__(self,First_name,Last_name):
        self.First_name = First_name
        self.Last_name = Last_name

class Customer(Person):
    def __int__(self, First_name,Last_name,account_no,balance=0):
        super().__int__(First_name,Last_name)
        self.account_no = account_no
        self.balance = balance

    def __str__(self):
        return f'Customer: {self.First_name} {self.Last_name}\nAccount Balance {self.account_no}: ${self.balance} '


    def deposit(self,amount_deposit):
        self.balance += amount_deposit
        print ('Deposit Accepted')

    def withdraw(self,amount_withdraw):
       if self.balance >= amount_withdraw:
          self.balance -= amount_withdraw
          print('Withdraw done')
       else:
            print('Insufficient funds')




def create_cutomer():
    first_name_ct = input('Enter your name: ')
    last_name_ct = input('Your last name: ')
    account_number = input('Enter your account number: ')
    customer1 = Customer(first_name_ct,last_name_ct,account_number)

    return customer1


def start():
    my_client = create_cutomer()
    print(my_client)
    option = 0

    while option != 'E':
        print('Choose: Deposit (D), Withdraw(W), or Exit(E)')
        option = input()

      if option == 'D':
          dep_amount = int(input('Deposit Amount: '))
        my_client.deposit(dep_amount)
      elif option == 'W':
         with_amount = int(input('Withdraw Amount: '))
         my_client.withdraw(with_amount)

      print(my_client)


deposit = input(float('Submit the amount'))
print('account' = 'balance' + 'deposit')

withdraw = input(float('Withdraw the amount'))
account = balance - deposit
withdraw < account


exit()





def start():

