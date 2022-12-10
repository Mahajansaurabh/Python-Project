def letter(word):
   # return ''.join(sorted(args))
    #return ''.join(set('entertaining'))

   my_set = set()

   for letter in word:
       my_set.add(letter)

   my_list = list(my_set)
   my_list.sort()

   return my_list

print(letter('pineapple'))
#args = 'aaabbbbcccdddd'

#letter.sort(reversed=False)

#print(letter(args))


