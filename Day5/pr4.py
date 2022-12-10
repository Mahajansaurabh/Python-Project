def pat(args):
 sum = 0
 for i in range(1,num+1):
  sum = sum+i
 return sum
def mySumRecursion(num):
 if num==0:
  return 0
 else:
  return num+mySumRecursion(num-1)
a = int(input('Enter the range: '))
b = mySumRecursion(a)
print('The sum of'+str(a)+'natural no.is'+ str(b))
