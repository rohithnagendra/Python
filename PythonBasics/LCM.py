print("--------- WELCOME TO lcm PROOGRAM----------")
my_f_number = input(" ENTER THE FIRST NUMBER: ")
x = int(my_f_number)
my_s_number = input(" ENTER THE SECOND NUMBER: ")
y = int(my_s_number)

smaller = 0
lcm = 0
if x > y:
       greater = x
else:
    greater = y
    
while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1


print(f"the lcm of {x} and {y} is {lcm}")