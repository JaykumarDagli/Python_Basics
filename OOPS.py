# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 11:11:52 2020

@author: Jay
"""

""" CLASS & OBJECT """

# Class: Blueprint to create new object, everything is an object in Python eg: Animal
# Obj: Instance of a class eg: Cat, they have attributes and methods

class Point:
    def draw(self):
        print('Draw')
        
point = Point()
point.draw()

print(isinstance(point, Point)) #helps to know if obj is from the specified class

# CONSTRUCTOR: method called when creating new object

# 'self' is a reference to current object

class Point:
    
    default_color = 'red' #class attribute
    
    def __init__(self,x,y): #special magic method i.e. constructor 
        self.x = x
        self.y = y
    
    @classmethod #decorator to let ppl know that this is a class method
    def zero(cls): #just like 'self' this is a convention 
        #return Point(0,0) 
        return cls(0,0) 
    
    #Point(0,0) and cls(0,0) are the same as they both return object with 
    #initialized values 
    
    def draw(self):
        print('X is: ', self.x)
        print('Y is: ', self.y)
        
    #magic method
    def __str__(self): 
        return f"(self.x),(self.y)"
            
p1=Point(1,2)
p1.draw()

#calling class method 
p2=Point.zero()
p2.draw()

""" CLASS v/s INSTANCE ATTRIBUES """

# class attributes are shared among all instances i.e. objects :
# but objects can have their specific attributes which
# may not be present in the class i.e. objects are dynamic 

""" CLASS v/s INSTANCE METHODS """

# just like attributes, classes and objects also have methods that
# can be on various levels, a class method will be inherited by
# every object but not the other way round 

# the main use of this functionality is that if we wanted to 
# initialize a object with the same values, we would have to write
# code again and again, so we create this method and call it

""" MAGIC METHODS """

#called automatically by python interpretor having __ eg: __init__

p1=Point(1,2)
p1=Point(1,2)

#returns False as addresses are compared by default and not the data
print('Comparison is: ', p1==p2)

#there are magic methods to solve this eg: __eq__
#and there are methods for arithmetic operators as well

""" INHERITANCE """

# mechanism to allow common functions in one class and inherit them in
# other classes

class Animal:
    
    #can inherit variables/attributes
    def __init__(self):
        print('Animal Constructor')
        self.age = 1
    
    #can inherit functions 
    def eat(self):
        print('Eat')

#'Animal' is parent and 'mammal' is child class

#suppose if we have constructor in the child, it'll override 
#the one in the base class and thus, we have to write 'super' 
#in doing so, first the constructor of the parent class is called 
#and then of child class. If this is not done, we get 'AttributeError'


class Mammal(Animal):
    
    def __init__(self):
        super().__init__() 
        print('Mammal Constructor')
        self.wt = 1
    
    def walk(self):
        print('Walk')
        
m1=Mammal()
print(m1.age)

""" ABSTRACT CLASS """

# Sometimes the parent class is only needed to provide inheritance 
# eg: we can have a base class a human, and the child classes as 
# male and female but 'human' will never be needed for the code i.e.
# we'll create objects only from the child classes and in this case
# the parent class should be made 'abstract' 

# 'abc' stands for Abstract Base Class

from abc import ABC, abstractmethod

class Human(ABC):
    
    @abstractmethod    
    def smile(self):
        print('Smile')

class Male(Human):
    
    def taska(self):
        pass
    
class Female(Human):
    
    def taskb(self):
        pass
    
# once this is done, we cannot create objects from the 'human' class
# and it becomes abstract
    
""" POLYMORPHISM """

























    
