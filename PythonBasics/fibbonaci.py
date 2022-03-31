print("welcome to the fibonacci series program")
fibo_num = input("enter the number: ")
fibo_i_num = int(fibo_num)

n1 = 0
n2 = 1
n3 = 1

print(f"{n1} {n2}")

for x in range(fibo_i_num):
  print(f"{n3} ")
  n1 = n2
  n2 = n3
  n3 = n1 + n2
  