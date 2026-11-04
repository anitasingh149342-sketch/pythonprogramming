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
