# # 1. Which function is used to display output in Python?
# #  A. input() B. print() C. output() D. display() = B. print()

# #  2. Which symbol starts a single-line comment?
# #  A. // B. # C. /* D. - = B. #
 
# # 3. What type does input() return by default? 
# # A. int B. float C. str D. bool = C. str

# # 4. Which is a valid variable name?
# # A. 2marks B. student name C. student_name D. class = C. student_nmae

# # 5. What is the type of 25?
# # A. str B. float C. int D. bool = C. int

# # 6. What is the type of 10.5?
# # A. int B. float C. str D. complex = B. float

# # 7. Which type stores key-value pairs? 
# # A. list B. tuple C. dict D. set = C. dict

# # 8. Which type stores unique values? 
# # A. set B. list C. str D. dict = A. set

# # 9. What does type(25) return? 
# #A. 25 B. int C. <class 'int'> D. number = B. int

# # 10. Which expression converts "10" to an integer? 
# # A. str("10") B. float("10") C. int("10") D. bool("10") = int("10")

# # 11. What does bool(0) return?
# # A. True B. False C. 0 D. None = B. False 

# # 12. What is the output of print("Hi", "There")? 
# # A. HiThere B. Hi There C. "Hi" "There" D. Error = B. Hi There

# # 13. Which type is immutable?
# # A. list B. dict C. set D. tuple = D. tuple

# # 14. What does range(5) contain when converted to a list?
# # A. 1,2,3,4,5 B. 0,1,2,3,4 C. 0,1,2,3,4,5 D. 5 only = B. 0,1,2,3,4

# # 15. Which is the correct Boolean literal? 
# # A. true B. TRUE C. True D. bool = A. true

# # 6. Which function converts a value to a string? 
# # A. string() B. str() C. text() D. toString() = str()

# # 17. Which value represents no value in Python?
# # A. null B. nil C. None D. empty = C. None

# # 18. What is the result of int("25.5")? 
# # A. 25 B. 25.5 C. ValueError D. True = C. ValueError

# # 19. Which type uses square brackets? 
# # A. tuple B. list C. dict D. set = B. list

# # 20. Which statement is correct? 
# # A. Python ignores case B. Python is case-sensitive C. Variables must be uppercase D. Strings need no quotes 
# # = B. Python is case-sewnsitive


# # Practise Questions 

# # 1. Write programm to print hello world.
# print("hello world")

# #2. Print your name, city, and course on separate lines.
# name= "ritika"
# city= "Gorakhpur"
# course= "python"

# print("name is:", name)
# print("city is:", city)
# print("course is:", course)

# #3. Create variables for name, age, and city and print them.
# name= "ritika"
# age= 15
# city= "gorakhpur"
# print(name, age, city)

# #4. Take a user name as input and print a welcome message.
# name = input("name")
# print("welcome:", name)

# #5. Take two integers as input and print their sum.
# x= int(input("any number"))
# y= int(input("any number"))
# sum= x+y
# print(sum)

# #6. Take the length and width of a rectangle and print its area.
# length= 34
# breadth= 56
# area= length*breadth
# print("area of rectangle:", area)

# #7. Take a temperature in Celsius and print a simple Fahrenheit conversion using the formula F = C * 9/5 + 32.
# C= float(input("Celcius:"))
# F= C * 9/5 + 32.
# print(F)

# #8. Take a student name and marks as input and print a formatted message.
# student_name= input("student_nmae:")
# marks= int(input("marks:"))
# print(name, "marks scored:", marks)


# #9. Take the price and quantity of an item and calculate the total bill.
# price= int(input("price:"))
# quantity= int(input("quantity:"))
# print(price * quantity)

# #10. Take a decimal number as input and print its type before and after converting it with float().
# number= float(input("enter any number"))
# print(type(number))

# #11. Create a list of five subjects and print the list.
# groceries= ["green chilli", "brinjal", "potato", "tomato"]
# print(groceries)

# #12. Create a tuple containing three coordinates and print it.
# score= (100, 200, 300)
# print(score)

# #13. Create a dictionary containing a student name and age, then print the name.
# student= {"name" : "riya" , "age" : 18}
# print(student["name"])

# #14. Create a set with repeated numbers and display the result.
# nums= {23,24,25,26}
# print(nums)

# #15. Use type() to display the types of a string, integer, float, and Boolean value.
# name= "ritika"
# age= 15
# marks= 93.4
# is_student= True
# print(type(name))
# print(type(age))
# print(type(marks))
# print(type(is_student))

# #16. Convert the string "100" to an integer and add 25.
# number= int("100")
# print(number+25)

# #17. Convert the integer 250 to a string and display its type.
# num= str(250)
# print(type(num))

# #18. Create variables for employee name, salary, and department and print them.
# employee_name= "Raunak"
# salary= 25,000
# department= "data analyst"
# print(employee_name, salary, department)

# #19. Take marks in three subjects and print the total and average.
# sub1_marks= float(input("maths:"))
# sub2_marks= float(input("science:"))
# sub3_marks= float(input("social science:"))
# total=sub1_marks + sub2_marks + sub3_marks
# average= total / 3
# print(total)
# print(average)

# #20. Create a program that takes item name, price, and quantity as input, converts numeric inputs correctly, and prints a simple bill.
# item_name= str(input("item_name:"))
# price= float(input("price:"))
# quantity= int(input("quantity:"))
# total= price*quantity
# print("item_name:" , item_name)
#print("total:" , total)

for i in range(1,51):
    print(i)
    
    
name="sana"
Students=["Ritika","Roshan","Aman","riya",name,"Ali"]

print(len(Students))
print(len(name))

for stud in range(len(Students)):
    print("values=",Students[stud],"index=",stud)
    
for s in range(6):
    print("*" *6)
    
for i in range(1,8):
    print("*",i)
    
    

            
             