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

#ques 9
# number= float(input("enter any number"))
# print(type(number))

  #11. Create a list of five subjects and print the list.
# groceries= ["green chilli", "brinjal", "potato", "tomato"]
# print(groceries)

 #12. Create a tuple containing three coordinates and print it.
# score= (100, 200, 300)
# print(score)

#13. Create a dictionary containing a student name and age, then print the name.
# student= {"name" : "riya" , "age" : 18}
# print(student["name"])

# # #14. Create a set with repeated numbers and display the result.
# nums= {23,24,25,26}
# print(nums)

# # #15. Use type() to display the types of a string, integer, float, and Boolean value.
# name= "ritika"
# age= 15
# marks= 93.4
# is_student= True
# print(type(name))
# print(type(age))
# print(type(marks))
# print(type(is_student))

# # #16. Convert the string "100" to an integer and add 25.
# number= int("100")
# print(number+25)

# # #17. Convert the integer 250 to a string and display its type.
# num= str(250)
# print(type(num))

# # #18. Create variables for employee name, salary, and department and print them.
# employee_name= "Raunak"
# salary= 25,000
# department= "data analyst"
# print(employee_name, salary, department)

# # #19. Take marks in three subjects and print the total and average.
# sub1_marks= float(input("maths:"))
# sub2_marks= float(input("science:"))
# sub3_marks= float(input("social science:"))
# total=sub1_marks + sub2_marks + sub3_marks
# average= total / 3
# print(total)
# print(average)

# # #20. Create a program that takes item name, price, and quantity as input, converts numeric inputs correctly, and prints a simple bill.
# # item_name= str(input("item_name:"))
# # price= float(input("price:"))
# # quantity= int(input("quantity:"))
# # total= price*quantity
# # print("item_name:" , item_name)
# #print("total:" , total)

# for i in range(1,51):
#     print(i)
    
    
# name="sana"
# Students=["Ritika","Roshan","Aman","riya",name,"Ali"]

# print(len(Students))
# print(len(name))

# for stud in range(len(Students)):
#     print("values=",Students[stud],"index=",stud)
    
# for s in range(6):
#     print("*" *6)
    
# for i in range(1,8):
#     print("*",i)
    
    
    
    # 1. Which operator returns the remainder of a division? 
    # A. / B. // C. % D. ** ,ans=A.
   
    # 2. What is the result of 10 // 3?
    # A. 3.33 B. 3 C. 1 D. 0 ,ans=B.
   
    # 3. Which operator checks equality of value? 
    # A. = B. == C. is D. != ,ans=B.

    #   4. What does 'and' return if both sides are True? 
    # A. False B. None C. True D. 0 ,ans=C.
    # 
    # 5. Which operator updates a variable by adding to it?
    # A. =+ B. += C. + D. ++ ,ans=B.
             
        # 6. Which operator performs a bitwise AND? 
        # A. && B. & C. and D. | ,ans=B.
        
        # 7. Which operator checks whether two variables are the same object?
        # A. == B. is C. in D. = ,ans=B.
       
        # 8. Which operator checks membership in a list?
        # A. in B. is C. == D. has ,ans=A.   
        
        #9. Which is evaluated first in 10 + 2 * 3?
        # A. 10 + 2 B. 2 * 3 C. Left to right always D. None,ans=B.
        # 
        # 10. Which keyword starts a conditional block?
        # A. for B. if C. def D. while ,ans=B.
        # 
        # 11. What does elif mean? 
        # A. else if B. an alias for else C. a loop keyword D. a function ,ans=A.
        
        #12. What runs if no condition in if-elif-else is True?
        # A. Nothing B. The if block C. The else block D. An error ,ans=C.
        # 
        # 13. Which loop is best when the number of iterations is known? 
        # A. while B. for C. if D. elif ,ans=B.
        # 
        # 14. What does range(5) start from?
        # A. 1 B. 0 C. 5 D. -1 ,ans=B.
        
        #15. Which statement exits a loop immediately?
        # A. continue B. break C. pass D. return ,ans=B.
        # 
    # 16. Which statement skips to the next iteration?
#          
#         A. break B. continue C. exit D. stop ,ans=B.
       
#       17. What does word[1:4] do on a string? 
#          A. Returns characters at index 1 to 4 inclusive B. Returns characters at index 1, 2, 3 Returns the whole string D. Raises an error
#         #Ans=B.
    
#     18. Which method removes leading and trailing spaces?
#      A. trim() B. strip() C. clean() D. remove() ,ans=B.
    
#      19. Which keyword defines a function?
#      A. func B. def C. function D. lambda ,ans=B.
    
#      20. What does a function return if it has no return statement?
#     #A. 0 B. An error C. None D. An empty string C. ans=C.
    
# 1. Write a program to calculate the area and perimeter of a rectangle using arithmetic operators.
#     length = float(input("Length: "))
#     width =float(input("Width: ")) 
#     print("Area:", length * width) 
#     print("Perimeter:", 2 * (length + width))
    
# 2. Take two numbers as input and print whether the first is greater, smaller, or equal to the second.
#     x = int(input("First number: ")) 
#     y = int(input("Second number: ")) 
#     if  a >=  b:   
#         print("First is greater")
#     elif a <= b:    
#         print("First is smaller")
#     else:   
#         print("Both are equal")
        
# 3. Write a program that checks if a number is both even and greater than 10 using logical operators.
#     num = int(input("Number: ")) 
#     if num % 2 == 0 and num > 10:   
#         print("Even and greater than 10")
#     else:  
#         print("Condition not met")
        
#  4. Write a program using a shorthand assignment operator to add 10 to a running total three times.
#     total = 0
#     total += 10 
#     total += 10 
#     total += 10 
#     print(total)
    
#     #5. Write a program that checks membership of a number in a list of allowed roll numbers.
#     allowed = [101, 102, 103]
#     roll = int(input("Roll number: "))
#     print(roll in allowed)
    
#  6. Write a program to check if a person is eligible to vote (age 18 or above) using an if-else statement.
#     age = int(input("Age: "))
#     if age >= 18:   
#         print("Can  vote")
#     else:   
#         print("Can Not eligible")
        
#   7. Write a program that grades a student's marks using if-elif-else (A, B, C, Fail).
#     marks = int(input("Marks: ")) 
#     if marks >= 95:   
#          print("X")
#     elif marks >= 80:   
#          print("Y")
#     elif marks >= 30:    
#          print("Z")
#     else:    
#              print("Fail")
             
# 8. Write a program with a nested if that checks both age and whether a person has a valid ID.
# age = int(input("Age: ")) 
# has_id = True
# if age >= 18:   
#       if has_id:       
#           print("Entry is allowed")   
#       else:    
#           print("ID is required") 
# else:    
#           print("then Not allowed")
          
# #9. Write a program using the short-hand if to print "Even" or "Odd" for a number.
# numbers = int(input("Number: ")) 
# value = "Even" if num % 2 == 0 else "Odd" 
# print(value)

# 10. Write a program that prints the first 10 natural numbers using a for loop.
# for i in range(1, 11):   
#     print(i)
    
# 11. Write a program that prints the multiplication table of a number using range().
# numbers = int(input("Number: "))
# for i in range(1, 11):    
#     print(num, "y", i, "=", num * i)
    
# 12. Write a program that adds numbers entered by the user until they enter 0, using a while loop.
# total = 0
# while True:   
#     num = int(input("Enter number (0 to stop): "))    
#     if num == 0:        
#       break    
# total += num 
# print("Total:", total)

# #13. Write a program that prints numbers from 1 to 20 but stops as soon as it reaches 15, using break.
# for i in range(1, 30):   
#     if i == 15:       
#         break   
#     print(i)
    
# #14. Write a program that prints numbers from 1 to 10, skipping multiples of 3, using continue.
# for i in range(1, 11):    
#     if i % 3 == 0:      
#         continue   
#     print(i) 
    
# #15. Write a program with nested loops that prints a simple pattern of stars (3 rows).

#     for i in range(3):   
#         for j in range(3):       
#             print("*", end=" ")    
#             print()
            
# #16. Write a program that takes a full name and prints only the first three characters using slicing.


# name = input("Full name: ") 
# print(name[0:3])

# #17. Write a program that counts how many times the letter 'a' appears in a given word.
# Character = input("Word: ") 
# print(Character.count("a"))

# #18. Write a program that takes a sentence and prints it in uppercase and lowercase using string methods.
# sentence = input("Sentence: ")
# print(sentence.upper())
# print(sentence.lower())


# #19. Write a function that takes two numbers and returns their product.
# def multiply(x, y): 
#     return x * y
# print(multiply(4, 5))

# #20. Write a function with a default parameter that greets a user, and a lambda that doubles a number.
# def greet(name="Teacher"):
#     print("Hello", name) 
#     greet() 
#     double = lambda a: a * 2
#     print(double(8))
    
    #List Assignment 
    # Part A - 20 Multiple Choice Questions 
    # 1. Which brackets are used to create a list?
    # A. ()    B. []    C. {}    D. <> =B.[]
    # 
    # 2. What is the index of the first item in a Python list?
    # A. 0    B. 1    C. -1    D. 2 =A.0
    # 
    # 3. Which property means a list can be changed after creation? 
    # A. Ordered    B. Mutable    C. Unique    D. Immutable=D. Immutable
    
    #4. Which method adds one item at the end? 
    # A. add()    B. append()    C. insert()    D. extend() =B.append()
    # 
    # 5. Which method adds several items from an iterable? 
    # A. append()    B. insert()    C. extend()    D. add() =C. extend
    # 
    # 6. What does remove(20) do? 
    # A. Removes index 20   
    # B. Removes first value 20   
    # C. Removes last value   
    # D. Clears the list 
    #=B. remoyes the first value 20
    # 
    # 7. What does pop() remove by default?
    # A. First item    B. Middle item    C. Last item    D. All items=C. Last term
    
    #8. Which method removes all items? 
    # A. delete()    B. clear()    C. empty()    D. remove() B. Clear
    # 
    # 9. What does index('A') return?
    # A. Number of A values    B. First index of A    C. Last index of A    D. True/False 
    # =B. First index of A
    # 
    # 10. Which method counts occurrences? 
    # A. count()    B. index()    C. total()    D. length() =A. count()
    # 
    # 11. Which method sorts a list in place?
    # A. sorted()    B. sort()    C. order()    D. arrange() =B. sort()
    # 
    # 12. Which function returns a new sorted list?
    # A. sort()    B. sorted()    C. order()    D. arrange() = B. sorted()
    # 
    # 13. What does reverse() do?
    # A. Sorts ascending    B. Sorts descending    C. Reverses order    D. Deletes values 
    #=C. Reverse order
    #
    # 14. Which method creates a shallow copy?
    #A. duplicate()    B. clone()    C. copy()    D. new()=C. copy()
    # 
    # 15. What is the result of [10, 20, 30][1]?
    # A. 10    B. 20    C. 30    D. Error =B. 20
    # 
    # 16. What does [1,2,3][0:2] return? 
    # A. [1,2]    B. [1,2,3]    C. [2,3]    D. [1,3] =A. [1,2]
    # 
    # 17. Which operator checks membership?
    # A. is    B. in    C. has    D. contains= b. in
    
    #18. What is the result of len([5, 6, 7])?
    # A. 2    B. 3    C. 4    D. 7 =B. 3
    
    #19. What does b = a do when a is a list?
    # A. Always makes a separate copy    
    # B. Creates another reference to the same list   
    # C. Converts it to tuple   
    # D. Sorts it 
    #=B. Creates another reference to the same list
    
    # 20. Which statement is correct?
    # A. Lists cannot contain duplicates  
    # B. Lists are immutable   
    # C. Lists can contain mixed data types    
    # D. Lists use only strings
    #= C. Lists can contain mixed data types
    
 #Part C - 20 Coding Practice Questions
    
# 1. Create a list of five student names and print it.
students_name=["ritika","roshni","ananya","ruhi","rahul"]
print(students_name)

#2. Create a list of five numbers and print the first and last item.
numbers=[1,2,3,4,5]
print(numbers[0],numbers[4])

#3. Create a list of fruits and print the second item.
fruits=["banana","apple","grapes","orange"]
print(fruits[1])

#4. Create a list of numbers and print the last three items using slicing.
items=["books","pen","pencil","copy","tank"]
print(items[2:5])

#5. Change the third item of a list to a new value.
items1= ["laptop","box","flower pot","paper weight"]
items1[2]="pen stand"
print(items1)

#6. Add a new item to a list using append().
fruits=["apple","banana","grapes"]
fruits.append("orange")
print(fruits)

#7. Insert a value at index 2 using insert().
games=["football","chess","badminton"]
games.insert(2,"cricket")
print(games)

#8. Add three values to a list using extend().
names=["ritika","rahul","ritik"]
names.extend(["riya","shivansh","ronak"])
print(names)

#9. Remove a specific value using remove().
names=["ritika","rahul","ritik"]
names.remove("ritika")
print(names)


#10. Remove the last item using pop().
names=["ritika","rahul","ritik"]
names.pop(2)
print(names)

#11. Remove the item at index 1 using pop(1) and print the removed value.
names=["ritika","rahul","ritik"]
names.pop(1)
print(names)

#12. Empty a list using clear().
names=["ritika","rahul","ritik"]
names.clear()
print(names)

#13. Find the index of a given value.
names=["ritika","rahul","ritik"]
print(names.index("ritik"))

#14. Count how many times a value occurs.
names1=["ritika","rahul","ritik","ruhi","ritik"]
print(names1.count("ritik"))

#15. Sort a list in ascending and descending order.
numbers2=[1,4,6,7,8]
numbers2.sort
print(numbers2)
numbers2.sort(reverse=True)
print(numbers2)

#16. Reverse a list.
numbers4=[1,2,3,4,5,6,7,8]
numbers4.reverse()
print(numbers4)

#17. Create a copy of a list and modify only the copy.
a=["teddy bear","car"]
b = a
b.append("toy house")

c = a.copy()
c.append("toy gun")

print(a)
print(b)
print(c)

#18. Check whether a value exists in a list using in.
listi=["footmat","bouquet","flower","headphones"]
print("flower" in listi)


#19. Create a nested list representing marks of two students and access one mark.
#20. Create a list of numbers and display its length, maximum, minimum and sum.


#data types

#mcqs
#1. Which type represents 3+4j? 
# A. int B. float C. complex D. str (ans=c. complex)

# 2. What does divmod(17, 5) return?
# A. (3, 2) B. (2, 3) C. 3.4 D. 2(ans=a. (3,2))

# 3. Which module provides sqrt() and factorial()?
# A. random B. math C. sys D. os (ans=b. maths)

# 4. What does int(3.9) return? 
# A. 4 B. 3.9 C. Error D. (ans=a. 4)

#5. Which is a valid one-item tuple?
# A. (5) B. [5] C. (5,) D. {5} (ans=a. (5))

# 6. What happens when you run t[0] = 99 on a tuple?
# A. Value changes B. TypeError C. New tuple is made D. Nothing (ans= b. typeError)

# 7. For t = (1, 2, 2, 3), what does t.count(2) return? 
#A. 1 B. 3 C. 0 D. 2 (ans= d. 2)

# 8. What is a, b = (10, 20) called?
# A. Unpacking B. Packing C. Slicing D. Casting (ans = A. unpacking)

# 9. How do you create an empty set? 
# A. {} B. set() C. [] D. () (ans=B. set())

# 10. What is {1, 2, 3} & {2, 3, 4}? 
# A. {2, 3} B. {1, 2, 3, 4} C. {1, 4} D. {1} (ans= {2,3})


#11. Which method adds one item to a set? 
# A. append() B. insert() C. add() D. push() (ans= add())

# 12. Which is the immutable version of a set?
# A. tuple B. list C. dict D. frozenset(ans= d. frozenset)

# 13. Which method returns a default value for a missing key?
# A. pop() B. get() C. keys() D. clear() (ans=b. get)

# 14. Which method returns key-value pairs? 
# A. keys() B. values() C. items() D. get() (ans = c. items)

# 15. Which can be a dictionary key?
#A. tuple B. list C. set D. dict  (ans= d. dict)

# A. Deletes the dictionary B. Sorts the keys C. Replaces the whole dictionary D. Adds or updates key-value pairs # 
# 16. What does d.update({"b": 2}) do?
# (ans=d.)

# 17. Which block always executes?
# A. try B. except C. else D. finally (ans= d. finally )

# 18. Which keyword raises an exception manually?
# A. throw B. raise C. error D. catch(ans= b. raise)

#19. What error does int("abc") raise?
# A. ValueError B. TypeError C. NameError D. (ans= a. value error )

#20. When does the else block of try run? 
# A. When an exception occurs B. When no exception occurs C. Always D. Never (ans= a.)

#code pratice questions 
#1. Take a number and print its square root, ceiling, and floor using the math module.
import math
num=float(input("enter any number:"))
print(math.sqrt(num))
print(math.ceil(num))
print(math.floor(num))

#W 2. Take two integers and print the quotient and remainder using divmod().
x=int(input("first number"))
y=int(input("second number :"))
q,r=divmod(x,y)
print("Quoteint:",q)
print("Remainder:",r)


# 3. Take a decimal number and print it rounded to 2 decimal places.
m = float(input("Number: "))
print(round(m, 2))

# 4. Convert the number 25 to binary, octal, and hexadecimal.
t = 25 
print(bin(t))
print(oct(t)) 
print(hex(t))

#5. Create a tuple of 5 numbers. Print the first item, the last item, and the middle three items
nums1 = (10, 20, 30, 40, 50) 
print(nums1[0]) 
print(nums1[-1]) 
print(nums1[1:4])

#6. Unpack a tuple (name, age, city) into variables and print them.
people = ("ritika", 15, "gorakhpur")
name, age, city = people
print(name, age, city)

#7. Count how many times a value appears in a tuple and find the position of another value.
t = (4, 7, 4,3, 8, 7)
print(t.count(3))
print(t.index(7))

#8. Swap two variables using tuple unpacking. 
a = 2
b = 15
a, b = b,a
print(a, b)

# 9. Remove duplicates from a list of numbers using a set.
data  = [1,1,3,4,4,2,2]
unique= list(set(data))
print(unique)

# 10. Given two sets of student names, print the common names, all names, and names only in the first set. 
r = {"ritika", "Rahul", "Nena"} 
t = {"Rahul", "Nena", "simran"}
print(a & b)
print(a | b) 
print(a - b)
# 11. Take a sentence and print the number of unique words.
sentence = input("Sentence: ") 
words = sentence.lower().split()
print(len(set(words)))

# 12. Add and remove items in a set and print the set after each change. 
n={4,5,6,7,1}
n.add(10)
print(n)
n.remove(4)
print(n)

#13. Create a dictionary with name, age, and course. Print each key and value using a loop. 
Employee={"name":"ritika","age":15,"course":"python"}
for key, value in Employee.items():
    print(key, ":",value)

# 14. Count how many times each character appears in a word using a dictionary.
Word= input("Word: ")
freq={}
for n in Word:
    freq[n]=freq.get(n,0)+1
print(freq)    
    
# 15. Store a product name and price in a dictionary, update the price, and print it. 
product = {"name": "dairy", "price": 35}
product["price"] = 50
print(product)

# 16. Create a nested dictionary of two students with marks and print the name of the topper.
students = {    "s1": {"name": "ritika", "marks": 94},    
            "s2": {"name": "rahul", "marks": 89} 
            }
topper = "" 
best = 3 
for info in students.values():   
    if info["marks"] > best:        
        best = info["marks"]        
topper = info["name"] 
print(topper, best)
# 17. Divide two numbers entered by the user. Handle ZeroDivisionError and ValueError.
try:    
    c= float(input("A: "))    
    d = float(input("B: "))    
    print(a / b) 
except ZeroDivisionError:    
    print("Cannot divide by zero") 
except ValueError:    
    print("Enter valid numbers")
# 18. Keep asking for an integer until the user enters a valid one.
while True:   
    try:       
        n = int(input("Enter any integer: "))        
    except ValueError:       
     print("Invalid, try again") 
     print("You entered", n)

# 19. Raise a ValueError if the entered age is negative, and handle it with try-except. 
try:    
    age = int(input("Age: "))    
    if age < 0:        
        raise ValueError("Age can't be negative")   
    print("Age:", age)
except ValueError as n:  
    print("Error:", n)
# 20. Open a file that may not exist, handle FileNotFoundError, and print a message in finally. 
try:    
    i = open("missing.txt")    
    print(i.read()) 
except FileNotFoundError:   
    print("File not found") 
finally:    
    print("Done")

