#Multiples Program
print("---- Welcome to the Multiples Program --------------")

my_num = input("Enter the number to generate the Multiples: ")

my_i_num  = int(my_num)

n = 1
print(f"multiples of {my_num} as follows:")

while n <= 10:
    prod = my_i_num * n
    print(f"{my_i_num} * {n} = {prod}")
    n += 1
    
