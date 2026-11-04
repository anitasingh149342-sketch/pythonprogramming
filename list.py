# name1="aman"
# name2="rahil"
# name3="ritika"
# name4="rahul"
name5="Sam"

# list []
# syntax
# list_name =[item,item2,item3,.....]

# example
name=["Aman","rahil","ritika","rahul",name5]
fruits=["Apple", "mango","Banana"]
numbers=[1,3,345,34,4,67,48,23,32,41,56,70]

mixed_list=[10,"python,",True,5.5,[1,3,345,34]]

#orderd
#mutable
#duplicates 
#diffrent data types

#access data of list items
print(name[2])
print(mixed_list[4])
print(numbers)
print(fruits)
print(fruits[-1]) 
print(name[1:4]) #4th index is exclude
print(numbers[:2])
print(numbers[2:])
print(numbers[::2]) #skip 

#slicing
#syntax
# List_name[start:stop:step]

# modifying lists
marks=[70,50,80]
marks[1]=76

# adding items 
# append()
#insert()
# extend()
marks.append(90)
print("append==",marks)
marks.insert(2,"sam")  #specific index
print(marks)

marks.extend([30,50,60])
print(marks)
#delete values
new_list=[1,2,3,3,4,2,1,4,5]
new_list.remove(3) #remove(), removes first matching value
print("remove :",new_list)

new_list.pop()
print("pop :",new_list)
new_list.pop(3)
print("pop :",new_list)

new_list.clear()
print("all  item removes from list :",new_list)




# index(), return index of first mathing value 

List_one=["aman","Riya","aman"]
print(List_one.index("aman"))
#count( ),how many times values occurs
print(List_one.count("aman")) 


New_num=[20,30,40,21,2,4,6]
New_num.sort()
print(New_num)

New_num.sort(reverse=True)
print(New_num)

New_num.reverse()
print(New_num)


# copy  
a=[10,20,30]
b=a.copy()
b.append(40)
print(a)
print(b)

# built-in functions 

numbbers=[10,20,40]
print(len(numbbers))
print(max(numbbers))
print(min(numbbers))
print(sum(numbbers))

# in and not in 

skills=["python","sql","Excel"]
print("python" in skills)
print("java" in skills)
print("java" not in skills)



#nested
score=[[70,30,50],[50,40],[34,60]]
print(score[0][1])
print(score[1][0])
print(score[2][0])

score2=[
    [70,30,50],
    30,
    [
        20,
        30,
        [
            30,
            20,
            40,
            [
                3,
                4,
                6
            ]
        ]
    ]

]

print(score2[2][2][3][1])



# print(score2[1][3][1])