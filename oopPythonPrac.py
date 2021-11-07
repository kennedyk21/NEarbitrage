"""
#Types of classes run down

a = 3
#here it show that a's class is int
def hello():
    print("hello")
print(type(a))
print(type(hello))
string = hello
"""
# classes 
#class here is dog
#everything inside the class is a method
class Dog:
    # init is esentially a constructor method 
    #if the constructor class takes nothing wrottong pass is sufficient
    # it also seems to have toString attributes as well
    # the self function works like the this function in java
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # in methods you can either return or print the mehtod
    def growl(self):
        return "growl"
    def bark(self):
        print("bark")
    #methods can also take inputs
    def add_one(self, x):
        return x+1
    #this is a get method
    def get_name():
        return self.name
    def get_age(self):
        return self.age
    #modifiers
    def det_age(self, age):
        self.age = age
#this creates an instance dog
d = Dog("bolt", 5)
#this calls the method in the class
d.bark()
#it seems that you can call variables
print(d.name)
print(d.growl())
print(d.add_one(4))