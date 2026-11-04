# print("Hitech Mentor , is Pvt ltd ")
# print("hello world") 
# variables
# x=10
# y=15

# Name="Ritika"
# Age=15
# isStudent=True
# print("Name:", Name, "Age:",Age,"Is Student:",isStudent)
# print(f"{name} will be {age + 1} next year")


# num1=2
# num2=4
# sum=num1+num2
# print(sum)

# name=int(input("type your name :"))
# print(type(name))
# 1.implicit 
# 2. explicit




#data type
#data type
#data type
#data type
#data type


# text===> str
#numeric vlaues===> int,float,complex
#sequnece Type==> list[],tuple(),range()
#mapping==>dict{"key":"value"}
#set===>set={1,3,4},frozenset([2,3,4])
#boolean==> bool==True/false
#binary types==> bytes b"hello",byteArray([1,3,5]),memmoryview(b"hello")
#none type== none

#typecasting
# val=2.5 #float
# sum=2+val
# print(type(sum))

# s=int(2.8)
# print("value of s:",type(s))
# R=int("3")
# print("Type of R:",type(R))

# type conversion==type casting
# 1. implicit==aoutomatic
# 2.Explicit==user

# number=float(2)
# number1=float(2.8)
# number2=int("456")
# number3=float("34.5")

# print("Type of number:",type(number1),type(number2),type(number3),type(number))

# a=str(12)
# b=str(93.0)
# print("Type of a:",type(a),"Type of b:",type(b))

# value1=float(input("Enter First number"))
# print("FIrst value is :",value1)
# value2=float(input("Enter 2nd number"))
# print("2nd value is :",value2)
# Add=value1+value2
# print("Addition of  value1 and value 2 :",Add)



#operators
#operators
#operators
#operators
#operators
# are symbols or keywords , used to perform operations on variables and values.
# types
# 1.Arithmatic == (
#     +   => Addition
#     -   => Subtraction
#     *   =>Mulitiplication
#     /   => Division
#     //  => Floor Division
#     %   => Modulus(Remainder)
#     **  => Exponent

# sum=5+3
# print(sum)
# num1=2
# num2=3
# res=num1**num2
# print(res)

#comparison (relational)(==,!=,<,>,<=,>=<)

# used to compare two values. retrun True / false 
a=10
b=5
# print(a==b) #false
# print(a!=b) #True
# print(a>b) #True
# print(a<b) #False
# print(a>=b) #True
# print(a<=b) #false

# 3. assignment operator(=)
# x=10
# m+=5 # m=m+5
# m-=2 # m=m-2
# m*=3 # m=m*3
# m/=3 # m=m/3

# 4. logical opr(and,or,not)
# 4. logical opr(and,or,not)
# 4. logical opr(and,or,not)
# 4. logical opr(and,or,not)
# 4. logical opr(and,or,not)

# exp1 and exp2 ==both should be true , then it return True
x=10
# print(x>5 and x<20) # True
# print(x<5 and x<20) # False

# exp1 or exp2 == atleast one statment should be true , then it return True
y=10
print(y<5 or y<20) # True
print(y<5 or y>20) # False
print(y>5 or y<20) # True
# not
print(not(y>20)) # reverse the result 

#membership Operators == check wether a value exists in a sequence 
nums=[1,2,3]
print("membership=",2 in nums) # true
print("membership=",6 not in nums) # true

## identity opr (is )==> check whether two variables refer to the same object
A=[1,2]
B=A
c=[1,2]

print("identity",A is B) # true
print("identity",A is c) # False
print("identity",A is not c) # True
print("identity",B is  c) # False 

## Bitwise (
# & == AND
# | == OR
# ^ ==XOR
# - == NOT
# << ==  Left shift
# >> == Right Shift     1010010

# 5= 101
# 3= 011
# 5&3    == 101
#           011
#           001==1 ANd
#            111 ==7 or
print("ANd ",5&3)
print("OR ",5|3)

