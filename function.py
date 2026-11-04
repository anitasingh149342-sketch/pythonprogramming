# print("my name is Ritika")
# print("my name is Ritika")
# print("my name is Ritika")


# function is a block of reusable code that perform a specific task 

#define
# def greet():
#     print("my name is ritika ")
#     print("what about u?")

#     #calling function
# greet()
# greet()
# greet()
# greet()
# greet()

# num1=12
# num2=13
# sum=num1+num2
# print(sum)

# num3=12
# num4=16
# sum2=num3+num4
# print(sum2)

#define function
def sum():
    num3=1
    num4=2
    sum2=num3+num4
    print(sum2)

#calling function
# sum()
# sum()


# def addition(a,b):
#     c=a+b
#     print(c)

# addition(2,3)
# addition(22,33)
# addition(12,3)

# def AreaOfSquare(x):
#     print("Area of sqaure is : ",x*x)

# # height=12
# # lenght=15
# side=float(input("enter side :"))

# AreaOfSquare(side)


# def findvolume(x,y,z):
#    c =x*y*z
#    print("voume is:",c)

# L=float(input("enter length :"))
# H=float(input("enter Height :"))
# W=float(input("enter width :"))

# findvolume(L,H,W)
# findvolume(2,4,W)

def mul(a,b):
     c=a*b
     return c


res=mul(3,4)

print(mul(5,4))

print(res)

# mutiple arguments   *args, **kwargs

# position Arguments 
def New_Sum(val1,val2,val3):
   res=val1+val2+val3
   print("New_sum is:",res) 

New_Sum(2,4,5) 

# Defualt parameter
def GREEEt(name="ritika"):
    print(name)

GREEEt() 
GREEEt("SAm")  
GREEEt("RAhul")  

#keyword arguments

def student(name,age):
    print(name,age)

student(20,"rahul")
student("rahul",20) #position Arguments
student(age=20,name="rahul") #keyword arguments


# *args 

def ADD(*numbers):
      total=0
      for n in numbers:
        total=total+n
      return total 

print(ADD(2,4,5,6,87,9,0,10,34)  )  
print(ADD(2,4)  )  

# **kwargs ==> allow to pass multiple keyword arguments

def STUdent(**details):
    print(details)


STUdent(name="Ritika",age=20,city="delhi")    


# local and global variables 

# local variables ==>created inside a function is generally local to that function

y=10  #a variable created outside a function is global
def demo():
  x=10
  res=x+y
  
  print(res)  
demo()


# lambda , recursive 

#create a fun tofind odd number  till 
def find_odd_numbers(n):
    odd_numbers = []
    for i in range(1, n+1):
        if i % 2 != 0:
            odd_numbers.append(i)
    return odd_numbers

print(find_odd_numbers(10))



# def check_odd(n):
#      return  n%2!=0

# print(check_odd(6))



# def check_odd(n):
#      if  n%2!=0:
#       return True
#      else: 
#        return False
# print(check_odd(6))


# def check_odd(n):
#      if  n%2!=0:
#         print("number is odd") 
#      else: 
#         print("number is even") 

# check_odd(6)


# # !5=5*4*3*2*1
# !n=n* (n-1) * (n-2) * (n-3) * (n-4) * (n-5)

def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)   # 5*factorial(4) *4*factorial(3) *3*factorial(2) * 2*factorial(1)  *1*1
                               
                         
                               
print(factorial(5))



#lmbda function ==> anonymous function , a function without name
# syntax ==> lambda arguments : expression

def square(x):
    return x*x
print(square(5))
print(square(6))

square=lambda  x: return x*x
print(square(5))

add=lambda a,b:a+b
print(add(2,4))


###map 