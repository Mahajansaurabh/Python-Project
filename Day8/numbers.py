def drug_store():
    my_list = []
    for x in range(1,101):
        my_list.append(x)
    return my_list

def my_generatorp():
    for P in range(1,101):
      yield P

def my_generatorm():
    for M in range(1,101):
      yield M


def my_generatorc():
    for C in range(1,101):
      yield C


print(my_generatorp)
print(my_generatorm)
print(my_generatorc)
