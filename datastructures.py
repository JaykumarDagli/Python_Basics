# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 16:10:14 2020

@author: Jay
"""

"""
DATA STRUCTURES
"""
    
#LIST is a collection of items i.e. numbers, letters etc
zeros = [0] * 5
letters = ['a','b']
print(zeros + letters)    
    
print(list(range(0,20)))  
    
print(len(zeros)) #to get len of list 

#elements of a list can be accessed and updated 
#using index starting from 0 

#generic -> listName[start:end:step]

names = ['a','b','c','d']
print(names[::-1]) #reverse a list

#unpacking a list using index 

numbers = [1,2,3,4,5,6]
first, second, *others = numbers 
#will unpack the first, second element and put the rest in 'others'

print(first)
print(*others)

first, *others, last = numbers

print(first)
print(*others)
print(last)

#looping over list 

letters = ['a','b','c']
for index, letter in enumerate(letters):
    print(index, letter)

#enumerate returns a tuple with index and the corresponding list element 

#add/remove iterms from list

#add item at end of list
letters.append('d')
print(letters)

#add item at specific position -> insert(position, element)
letters.insert(5,'e')
print(letters)

#remove item from end 
letters.pop()
print(letters)

#remove item in general -> but only first occurence 
letters.remove('b')
print(letters)

#remove many items from the list
del letters[0:2]
print(letters)

#remove all items from the list
letters.clear()
print(letters)

#finding object in a list
letters=['a','b','c']

print(letters.count('d')) #to get number of occurences 
print(letters.index('c')) #to get index of element 
#if element is not present, it will return Value Error and not -1

#sorting a list
numbers=[2,1,44,76,4]

numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)

#generic -> lambda input: output 
#generic -> map(function, iterable) will return a map object, convert it
#           to list and check the values 
#generic -> filter(function, iterable)

#in both map and filter, function can be a lambda function 

#LIST COMPREHENSION

#generic -> [expression/output for item in items if condition]

#ZIP FUNCTION -> return pairs of tuples 

list1 = [1,2,3,4]
list2 = [10,20,30,40]
list3 = 'abc'

z=zip(list1, list2, list3)
print(list(z))



















































