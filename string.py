#  A string is a sequence of a charachters enclosed inside 
#  1. single quotes ('')
#  2. double quotes (" ")
#  3.triple quotes ("""     """)

text="Hitech Mentor 123 !"
text2='Hitech Mentor 123 !'
text3="""Hitech Mentor 123 !"""
# accessing char
print(text[0])
name="Ritika"
print(name[-1])
print(name[-2])
print(name[-6])

# string slicing 
print(text[6:12])
print(text[7:])
print(text[:7])

# important string methods
# important string methods
# important string methods
# important string methods
# important string methods
# important string methods
# important string methods
# important string methods




# Method         Purpose
# upper()          Uppercase
# lower()          Lowercase
# capitalize()          First letter capital
# title()          First letter of each word
# strip()          Remove beginning/end spaces
# replace()          Replace text
# find()          Find position
# count()          Count occurrence
# startswith()          Check beginning
# endswith()          Check ending
# split()          String → List
# join()          List → String
# isalpha()          Check alphabets
# isdigit()          Check digits
# isalnum()
#index()



name2="python"

print(name2.upper())
name3="PYTHON"
res=name3.lower()
print("lower=",res)

text4="python programming"
print("capitalize===",text4.capitalize())

# first latter capital for each word 

print("first letter ===",text4.title())

string="   hi! i am ritika      "
# remove sapce from start and end
print(string)
print(string.strip())

text5="i like java"
print(text5)
result=text5.replace("java","python")
print(result)

# find( )  , returns the position of character or word

text6="hello! i am ritika, i am learning python from Hitech mentor!"
# print(text6.find("ritika"))

print(text6.count(" "))

# startswith( ) ,

print(text6.startswith("py"))
print(text6.startswith("hello"))

print(text6.endswith("tik"))
print(text6.endswith("mentor"))
print(text6.endswith("mentor!"))

# split(), split a string into a list 

text7="python, is easy!"

word=text7.split(",")
print(word)
word2=text7.split()
print(word2)

word2=["pyhton","is","easy","lang"]
print(word2)
res4=" ".join(word2)
print(res4)

# isalpha( ),whether all chaacters are alphabates 
string4="python"
print(string4.isalpha())

#isdigit()
text6="123456"
print(text6.isdigit())

#isalnum()
text7="python123"
print(text7.isalnum())