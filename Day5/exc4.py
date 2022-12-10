def count_primes(num):
  prime_numbers=[2]
  iteration = 3

  if num<2:
    return 0

  while iteration <= num:
    for i in range(3,iteration,2):
        if (iteration % i)==0:
         iteration +=2
         break
    else:
        prime_numbers.append(iteration)
        iteration += 2
  print(prime_numbers)
  return len(prime_numbers)


print(count_primes(50))

