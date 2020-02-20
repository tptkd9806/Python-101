
# Python Variables

# string
# int
# float
# list
# dict
# boolean : true false

int1 = 1 
string1= "Hi" 
list1 = [1,2,3]
dict1= {1: "hi", 2: "hello"}
bool1 = True # or false


# Python Containers

# ---Lists----
# Creating a list
list1 = [1,2,3]

# Accessing a List
print(list1[2])

# Python Operators
# Python Conditional
# Python Loops

# Adding to a list
list1.append(4)

# Modifying a List
list1[0]=10
print(list1)

# command + s 

# Removing from a List
list1.remove(10)
print(list1)

# Getting the length of a list
print(len(list1))

# ---- Dictionaries ----

# Creating a Dictionary
myDict = { "stupid": "USC",
          "smart": "UCLA",
          "safety":"UCI" }

# Accessing a Dictionary
print("printing the safety school", myDict["safety"])
print("printing the stupid school", myDict["stupid"])

# Modifying a Dictionary
myDict["stupid"]= "Berkeley"
print(myDict["stupid"])

#  Python Operators
# -- Arithmetic operators
# +,-,* 
# Division: Division & Floor Division
x= 10.0
print("Float division")
print(x/3)
print("Floor division")
print(x//3)
# Modulo : returns the remainder after division
print(10%4)

# -- Comparison Operatos
# == , != , > , <, >=, <=
x=1
y=1
z=2
print(x==y)
print(x>y)
print(z>y)

# -- Logical Operatos
# and or not

# and : returns true only if BOTH statements are true
print(True and True)
print(True and False)
print(False and False)
# or: returns true if EITHER statement is true
print(True or True)
print(True or False)
print(False or False)
# not: returns the negated value of the statement
print(not True)
print(not False)

# Python Conditionals ========

#HOMEWORK
# Question 1
for i in range(6):
    print(str(i)*i)

#Question 2


# QUESTION 3
num = int(11)
if num > 1 :
    for i in range(2, num):
        if(num % i) == 0:
            print ("is not a prime number")
            break
        else:
            print("is a prime number")
    else:
        print("is not a prime number")