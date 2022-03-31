print("------------------ welcome to prime  number program-------------------------")
my_prime = input("enter any number")
my_1_prime = int(my_prime)
c = 0
for n in range(1,my_1_prime+1):
  if my_1_prime % n == 0:
      c += 1

if c == 2:
  print(f"{my_prime} is a prime number")
else:
  print(f"{my_prime} is a not prime number")