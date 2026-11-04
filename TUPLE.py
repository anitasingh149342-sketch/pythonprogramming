# ordered
# indexed
# allows duplicates
# diffrent data types
# immutable  ### we dont want those values  to be changed.

tuple_name=(1,2,3,4)
name=("ritika","Sam","Rahul")
mixed_data=("ritika","Sam","Rahul",1,2,4,True,)

print(tuple_name)

days=("monday","Tuesday", "wednesday")

print(days[0])
print(days[1])
print(days[2])
print(days[-1])

# Access tuple items

# toltal values


# tuple sliceing

# tuple[strt:end]

numbers=(1,2,3,4,5,6,7,8,9)
print(numbers[1:4])
print(numbers[:4])
print(numbers[2:])
print(numbers[::-1])

#numbers[0]=200 # it can't work coz tuple is immutable
# print(numbers) it cnst 

# tuple cant provide methos such as append(),insert(),remove(),pop(),clear()

# numbers.append(40)  not work

# tuple has only two built in methods 
# count(),index()
print(numbers.count(10))
fruits=("Apple","banana","mango","Banana")
print(fruits.index("banana"))

print(len(fruits))
# max vales
print(max(numbers))
print(min(numbers))

number=(20,43,17,48,23,4,5,12,3,78,34,32) #sorted retun list , not a tuple
print(sorted(number))
# membership oerator(in )

print("Apple" in fruits)
print("pamxgfdsghjhgdsghjpaya" not in fruits)

# concatenation tuple 
a=(2,3)
b=(30,40)
c=a+b
print(c)

print(a*3)
# single item tuple , needs a comma
res=(12,)

# tuple unpacking 
student=("ritika",20,"python")

name,age,course=student
print(name)
print(age)
print(course)

# nested tuple 

data=(("Amit",20),("Ravi",21))

print(data)
print(data[0][0])
print(data[1][0])

score=(
    ("emglih",20,(20,10)),
    ("maths",20,(1,40,67,(20,40,(4,7)))),
    ("scince",30)
)
print(score[1][2][3][2][0])