# ======text file=======
# text
# csv
# json
# .py

# ======Binory file====
# image(.jpg,.png)
# audio(.mp3)
# video(.mp4)
# pdf or others binary file

# open("filename","mode")


# =====mode=====
# r  read
# w   write
# a   append
# x   create
# r+   read+write 
# w+  write+read
# a+  append+read

# file=open("student.txt","x")
# file=open("student.txt","r")
# file=open("student.txt","w")
# file.write("hello students!\n")
# file.write("welcome to python class!\n")
# file.write("learn programmimmg!\n")
# =====reading data====
# file=open("student.txt","r")
# data=file.read()
# print(data)
# file.close()

# file=open("student.txt","r")
# data=file.read(7)
# print(data)
# file.close()

# reading one line 
# file=open("student.txt","r")
# data=file.readline()
# print(data)
# data=file.readline()
# print(data)


# reading all lines  ...output will be a list
# file=open("student.txt","r")
# data=file.readlines()
# print(data)

# file.close()

file=open("student.txt","w")
file.write("\npython file handling")
file.close()
# append
file=open("student.txt","a")
file.write("\nwelcome to python \n welcome to hitech mentor \n python handling \n")
file.close()

# best practice 

with open("student.txt","r") as file:
    data=file.read()
    print(data)
file.close()


with open("student.txt","w") as file:
   file.write("Hello Python!!")
file.close()


with open("student.txt","a") as file:
   file.write("\n learning File Handling!!")
file.close()

with open("student.txt","r") as file:
    for line in file:
         print(line.strip())  #strip removes white space newline characters 


# csv file start 
# csv file start 
# csv file start 
# Roll no    Name    Age       Marks
# 101       Rahul    15        85
# 102       Ritika   14        90
# 103       Priya    16        92

# csv format 
# Roll no,Name,Age,Marks
# 101,Rahul,15,85
# 102,Rtita,15,90
# 103,Priya,16,92

import csv
#  syntax 
# with open("filename.csv","w",newline="") as file:
#      writer=csv.writer(file)
#      writer.writerow(["value1","Value2"])

# example 
# with open("student.csv","w",newline="") as file:
#      writer=csv.writer(file)
#      writer.writerow(["Roll NO","Name","Age"])
#      writer.writerow(["1","Ritika","15"])
#      writer.writerow(["2","Rahul","16"])

# multiples lines 

students=[
   ["Roll NO","Name","Age"],
   ["1","Ritika","15"],
   ["2","Rahul","16"],
   ["3","Priya","14"],
   ["4","Rakesh","12"]

]

# with open("student.csv","w",newline="") as file:
#    writer=csv.writer(file)
#    writer.writerows(students)

# with open("student.csv","r") as file:
#    reader=csv.reader(file)
#    for row in reader:
#       print(row)

# reading CSV Data using a List 
# with open("student.csv","r") as file:
#    reader=csv.reader(file)
#    data=list(reader)
#    print(data)
#    print(data[1])
#    print(data[1][1])

# appwendind data into csv 
# with open("student.csv","a",newline="") as file:
#    writer=csv.writer(file)
#    writer.writerows([105,"sahil",88])

student2=[
   ["106","xyz","15"],
   ["107","abx","16"],
   ["108","klm","14"],
   ["109","trs","12"]
  ]

with open("student.csv","a",newline="") as file:
        writer=csv.writer(file)
        writer.writerows(student2)

with open("student.csv","r") as file:
   reader=csv.reader(file)
   data=list(reader)
   print(data)        


student3=[
  {"Rollno":110,"Name":"SAM","Marks":98},
  {"Rollno":112,"Name":"SAM2","Marks":94},
  {"Rollno":113,"Name":"SAM3","Marks":76},
  {"Rollno":114,"Name":"SAM4","Marks":89}
  ]  

with open("student.csv","w",newline="") as file:
    fieldnames=["Rollno","Name","Marks"]
    writer=csv.DictWriter(file,
      fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(student3)