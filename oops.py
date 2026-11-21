# class Student:
#     name="ritika"
#     def study(self):
#         print("studying python at hitech mentor!!!")

# s1=Student()
# print(s1.name)  
# s1.study()  

# constructor==>  __init__() 
# syntax 
# class ClassName:
#     def __init__(self,parameters):
#         self.attrubutes=parameters

# class Student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def   display(self):
#         print(self.name )
#         print(self.age)

# s1=Student("rahul",15)       
# s2=Student("ritika",14) 
# s1.display()      
# s2.display()      


class Mobile:
    brand="apple"
    def call(self):
        print("calling.....")
    def camera(self):
        print("taking photo.....!") 

m1=Mobile()
print(m1.brand)
m1.call()
m1.camera()

class faculty:
    def putdata(self):
        self.id=int(input("enter faculty id "))
        self.name=input("enter name ")
        self.salary= float(input("enter salary " ))
    def display(self):
        print("faculty id =",self.id)    
        print("faculty name =",self.name)    
        print("faculty salary =",self.salary)    

a=faculty()
a.putdata()
a.display()  
b.faculty()   

# 3.Encapsulation
# 4.Inheritance
# 5.Polymorphism
# 6.Abstraction