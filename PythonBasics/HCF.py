print("--------- WELCOME TO HCF PROOGRAM----------")
my_f_number = input(" ENTER THE FIRST NUMBER: ")
x = int(my_f_number)
my_s_number = input(" ENTER THE SECOND NUMBER: ")
y = int(my_s_number)

smaller = 0
hcf = 0

if x > y:
  smaller = y
else:
  smaller = x

for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i 
 
print(f"The HCF of {x} and {y} is {hcf}")