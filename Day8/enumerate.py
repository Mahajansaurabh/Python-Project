list1 = [3,53,2,True,6.2,'sam']

index = 0
for item in list1:
    print(item,index)
    index += 1


for index,item in enumerate(list1):
    print(item,index)
