sum=5+3
print(sum)
num1=2
num2=3
result=num1**num2
print(result)

#explicit
p=int(1.4)
print("value of p:",type(p))
a=int("10")
print("value of a:", type(a))

a=str(10)
b=str(11)
print("value of a:", type(a))
print("value of b:", type(b))

#implicit
x=10
g=10.5
print("value of x:", type(x))
print("value of g:", type(g))

#1.Arithmatic operators
value1=input("Enter the first number")
print("first is number:", value1)
value2=input("Enter the second number")
print("second number is:", value2)
Add=value1+value2
print("Addition of two numbers is:", Add)

#2.Comparision operators
a=10
b=20
print(a==b)#false
print(a!=b)#true
print(a>b)#false
print(a<b)#true
print(a>=b)#false
print(a<=b)#true

#3.Logical operators
x=10
y=20
print(x>y and x<y)#false
print(x!=y or x<y)#True
print(x>y and not x<y)#true


#4. Assignment operators
a=10
b=20

sum=a+b
print("sum of a and b is:", sum)

#membership operators
nums=[1,2,3,4,5]
print(3 in nums)#true
print(6 not in nums)#true
print (10 in nums)#false

#Identity operators
A=[1,2]
B=A
C=[1,2]
print("identity of",A is B)#true
print("identity of",A is C)#false
print("identity of",A is not C)#true3

#BITWISE OPERATORS
#& == and
#| == or
#^ == xor
#<< == left shift
#>> == right shift

a=10
b=4

print(a&b)
print(a|b)
print(a^b)
print(a<<b)
print(a>>b)