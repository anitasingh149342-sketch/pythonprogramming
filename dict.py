# syntax
# dictionary_name={
#     "key":value,
#     "key":value,
#     "key":value,
#     "key":value,
# }


# create a dictionary 
student={
    "name":"Ritika",
    "age":14,
    "course":"python",
    "city":"gorakhpur"
}

print(student)

# data access 

print(student["name"])
print(student["course"])

# using get( ), it returns none if key is not there 

print(student.get("name")) 


# how to add data 

student["gender"]="female"
print(student)

# how to update data

student["age"]=15
print(student)

# update( ),add & update multiple key-value pairs

student.update({
    "age":16,
    "city":"delhi",
    "class":"9th"
})
print(student)

# how to access all keys
print(student.keys())
# how to access all values 
print(student.values())

# how to return all key-value pairs
print(student.items())

# in operator
print("name" in student)
print("AGE" in student)
print("attendence" not in student)

# how to remove key 
# pop(), it removes specified key and return its value 
#popitem(), it removes last inserted key-value pair
student.pop("age")
print(student)

student.popitem()
print(student)


# how to delete specific key- value pair

del student["gender"]
print(student)

# how to remove all items 
student.clear()
print(student)

# how to copy dictionary
student={
    "name":"ritika",
    "age":14,
    "course":"python"
}
new_student=student.copy()
print(new_student)

# how to count key valu pairs
print(len(student))

# how to create nested  dictionary 
students={
    "student1":{
        "name":"ritika",
        "age":14,
        "score":{
            "maths":79,
            "science":79,
            "english":79,
        }
    },
     "student2":{
        "name":"sam",
        "age":16
    },
     "student3":{
        "name":"ravi",
        "age":14
    },
}

print(students["student1"]["score"]["science"])

# Dictionary loop
data={
    "name":"ritika",
    "age":14,
    "course":"python",
    "gender":"f"
}
for key in data:
    print(key)

#  value 

for value in student.values():
    print(value)
#  key+value
for key,val in student.items():
    print(key ,":",val)