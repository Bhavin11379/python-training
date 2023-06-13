#21)  

"""
---->How to Define a Class in Python? 
Python is an object oriented programming language.

Almost everything in Python is an object, with its 
properties and methods.

A Class is like an object constructor, or a "blueprint" 
for creating objects.


----> What Is Self?

self represents the instance of the class. By using the “self”  we can 
access the attributes and methods of the class in python. 
It binds the attributes with the given arguments

"""
# Give An Example Of A Python Class.
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("nikhil", 36)

print(p1.name)
print(p1.age)