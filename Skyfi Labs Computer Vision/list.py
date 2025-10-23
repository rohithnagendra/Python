number = [1,2,3,4,5]
mix_list = [1,"myself",3.14,True]
nested_list = [1,2,[3,4]]


value = [13,15,34,55,77,99,32,234,]
mix_value = [1233,"yourself",4.13,True]
nested_value = [13,14,[23,54]]

print(value)
print(mix_value)
print(nested_value)

print(value[0])
print(mix_list[1])

print(nested_value)
value[1]=89
print(value)


mix_list.append(784)
print(mix_list)

nested_list.insert(2,5423)
print(nested_list)

mix_value.remove(4.13)
print(mix_value)

del value[3]
print(value)
valu_list = [1,2,3,4,5,5,66,7,47,57]
sub_list = valu_list[1:9]
print(sub_list)


print(valu_list[-3:-1])
print(valu_list[::2])

list_val = [1,2,3,4,5,6,7,8,9,10]
print(len(list_val))

listl =[1,2,3,45,567]
friut = ['orange','apple','banana','guava']
for fruits in friut:
    print(friut)
for l in listl:
    print(listl)
