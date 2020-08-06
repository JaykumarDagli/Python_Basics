# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 15:32:50 2020

@author: Jay
"""

#int, str are immutable i.e. if we update the value, it will
#be stored at a new location [id gives the location of a var

age=10
print(id(age))
age='10'
print(id(age))

#list is mutable i.e. the value is updated at the same location 

age1=[10,20,30]
print(id(age1))
age1.append(40)
print(id(age1))

"""
STRINGS
"""

course = 'Python'
print(len(course)) #check the length

#string is indexed from 0 on left and -1 on right
print(course[0])
print(course[-1])

#while slicing first index is included but last is excluded 
print(course[0:3])
print(course[-3:-1])

#formatted strings
first='Jay'
last='Kumar'
full=f"{first} {last}" #can also add valid expressions within {}
print(full)

#string methods: upperm lower, strip etc
course = "python programming"
print(course.upper())

#returns index of search string or -1 if it is not present 
print(course.find('pop'))

#returns t/f based on presence of string 
print('jay' in course)

"""
NUMBERS
"""

x=10
print(x)

x=0b10 #0b for binary
print(x)

x=0x10 #0x for hex
print(x)

#use UPPER case for constants 
PI = 3.14

#round, abs are common functions for numbers
#for other functions use 'math' module 

import math
print(math.sqrt(4))

#type conversion  => use int, str, float, bool as a function 
#to convert the var to required datatype


#"", 0, [], None are all FALSY values 
#meaning all these will return 0, all else will return 1 

bool(False) #will be False
bool('False') #will be True since the string is not empty

"""
CONDITIONAL [if-else] & TERNARY
"""

age=21
msg = 'Good' if age>18 else 'Bad'

"""
LOOPS
"""

for x in 'python':
    print(x)

for x in range(0,12,2):
    print(x)






 



















