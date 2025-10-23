def nmana():
    print("er")
##print (nmana)
nmana ()

def aB (name):
    print (f"hello,{name}")

aB("rohith")
aB("ronith")

def square (x):
    return x * x
result = square (4)
print (result)


def greet (name = "guest"):
    print (f"hello,{name}")


greet()
greet ("hhdhdhh")


def introduce (name,age):
    print(f"Name:{name}")
    print(f"Age:{age}")

introduce(age = 14,name = "Rohith.N")

def add_numbers(*args):
    return sum (args)


result =  add_numbers(1,2,3,4,19876%3235^23423)
print(result)







def describe_person(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")

describe_person(key = "ss" , value = "rr" )




square = lambda x:x*x
result = square (5)
print (result)



