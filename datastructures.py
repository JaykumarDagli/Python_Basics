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

#STACKS - LIFO eg: Browser History, list can be used as a stack 
#use append and pop to add/remove items 
#and latest element can be checked using index -1 

#QUEUE - FIFO eg: queues, list can be used as a queue
#but all the items have to be shifted since we have to remove 
#the element from the first position, thus, we use deque object

from collections import deque
queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
print('Queue is:', queue)
queue.popleft() #this is not for list, only for deque object
print('Queue is:', queue)

#TUPLES: just that this is not mutable/changeable
#tuples are denoted by () but they can also be denoted by ,
#i.e. a=(1,2) or a=1,2

point1 = (1,2,3)
print("Class point1:" , type(point1))
point2 = 1,2,3
print("Class point2:" , type(point2))

#ARRAY: faster than lists if there are many numbers 

from array import array
a1=array("i", [1,2,3])

#append, pop, insert, remove are same as lists just that all the
#items should be of the same type which is mentioned 
#as the typecode 

#generic -> array(typecode, [list of items])

#SETS: UNordered collection with no duplicates 

numbers = [1,1,2,3,4,5,4]
first = set(numbers)
print('First values: ', first)

#they are denoted by {}, add/remove methods can be used 
#but the main usage point is in Maths!

second = {4,5,8}
print(first | second) #union of 2 sets
print(first & second) #intersection 
print(first - second) #difference 
print(first ^ second) #either present in first or second but not both

#cannot be accessed by index since they are not ordered
#but we can check if the item is present in set or not

if 1 in first:
    print('Exists')

#DICTIONARIES: data is stored as key-value pair
#and can be accessed only with keys eg: key value pair

d1 = {'k1':'v1', 'k2':'v2'}
print("Value of K1 is: ",d1['k1'])
print("Other method to get value is: ", d1.get('k1'))

#this will return the keys
for i in d1: 
    print(i)

#to get values from the dict, use this:
for i in d1.items():
    print(i)

#DICT COMPREHENSIONS: same as list comprehensions just that we
#replace [] by {}

#UNPACKING operator:
numbers = [1,2,3]
print(numbers) #normal print
print(*numbers) #unpacking each item 

#EXERCISE
s1="This is a common interview question"
#Write program to find most repeated character 

freq= {}

for i in s1:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

Keymax = max(freq, key=freq.get) 
print(Keymax)