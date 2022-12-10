def return_distincts(num1,num2,num3):

    a_sum = num1+num2+num3
    a_list = [num1,num2,num3]

    if a_sum > 15:
      return max(a_list)
    elif a_sum < 10:
        return min(a_list)
    else:
        a_list.sort()
        return a_list[1]

print(return_distincts(3,2,7))

####
#if(num1>num2):
 #       if(num1>num3):
  #          return num1
     ###
# else:
    #        return num3
    #else:
     #   if(num2>num3):
      #      return num2
       # else:
        #    return num3

        #sum = 0

       # for n in sum:
        #    sum = sum + n

       # print('Sum:', sum)

#return_distincts(3, 5, 2)
#return_distincts(4, 5, 6, 7)
#return_distincts(1, 2, 3, 4, 5, 6)

#m= max(3,5,234)
#print('the value of the maximum is' + str(m))
###




#elif sum(args)<10:
 #  return lowest_number

#else sum(args)>10 and sum(args)<15:
 #  return args



#print(return_distincts(5,6,2))