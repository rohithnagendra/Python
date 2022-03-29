n=2
while n < 20:
    n += 2
   #print(n)




    
list1 = [1, 2, 3]
list2 = [9, 8, 7]
new_list = list1 + list2
list1 += list2
print(new_list)


all_fruits = ["apple", "banana", "orange"]
for fruit in all_fruits:
    print(fruit)



scores = [34, 67, 99, 105]
for s in scores:
 if s > 100:
    print("Invalid")
    break
 print(s)