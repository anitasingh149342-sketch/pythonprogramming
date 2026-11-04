# what is error handling?

# its a technique which is usedbto handle errors

a=10
b=0
# print(a/b)
# ZeroDivisionError: division by zero
# types errors
# 1.Syntax Error
# 2.Runtime Error/Exception
# 3.logic Error 

# 1.Syntax Error
# if 10>5    #SyntaxError: expected ':'
#  print("hello!")

# 2.Runtime Error/Exception
# print(10/0)   #ZeroDivisionError: division by zero

# 3.logic Error 
length=10
width=12
print(length+width)    #wrong for area

# for handling errors we used try and except 

# try:
#     #code that may couse an error
#     # statement
# except:
#     #code to handle error
#     # statement

try:
    a=10
    b=0
    print(a/b)
except:
    print("something went wrong!")  

# handling Specific Exceptions 
# 1.ZeroDevsionError  
# 2.ValueError
# 3.TypeError
# 4.NameError
# 5.IndexError
# 6.KeyError
# 7.FileNotFoundError


# 2.ValueError
# try:
#     age=int(input("Enter Your Age:"))
#     print("Your Age is",age)
# except ValueError:
#         print("pls enter a valid integer!")

# Multiple Exception 

# try:
#     a= int(input("Enter first Number:"))
#     b= int(input("Enter seond Number:"))
#     print(a/b)

# except ValueError:
#     print("pls enter valid numbers!!")
# except ZeroDivisionError: 
#     print("second no can not be zero!") 

#   The else block
# runs when no eception occurs

# try:
#     num=int(input("Enter a Number:"))
# except ValueError:
#     print("Invalid input!") 
# else:
#     print("your number is:",num)

# The Finally Block
# wether an exception occurs or not 

# try:
# except:
# else:
# finally: 


# try:
#     print("program started!")
#     result=10/2
   
# except ZeroDivisionError:
#     print("can not devide by zero!")
# else:
#      print(result)
# finally:
#     print("program finished!!")


# using raise to genrate an exception

# Age=int(input("Enter your Age:"))
# if Age<0:
#     raise ValueError ("Age cant not be negative!")
#     print("Age: ",Age)
# 10,2
# 10,0
# abc,2

try:
     num1= float(input("Enter first Number:"))
     num2= float(input("Enter seond Number:"))
     if num2==0:
        raise ValueError("the second number can not be zero!!")

     result=num1/num2

 
except ValueError as e:
        print("inputr error!!!",e)   
else:
         print("result:",result)  
finally:
         print("calculation completed!")         
