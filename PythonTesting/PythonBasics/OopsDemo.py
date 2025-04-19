#classes are user defined blueprint or prototype
#sum, multiplication, addition, constant
#methods, class variables, instance variables, constructors, etc
# self keyword is mandatory for calling variable banes into method
#instance and class variables have whole different purpose
#constructor name should be __init__
#new keyword is not required when you create object in python

class Calculator:
    num = 100 #class variable

    def __init__(self, a, b): #default constructor, variables created within constructors are instance variables
        self.firstNumber= a
        self.secondNumber= b
        print("I am called automatically when object is created")

    def getData(self):
        print("I am now executing as method in class")

    def Summation(self):
        return self.firstNumber + self.secondNumber + self.num

obj = Calculator(2, 3) #syntax to create objects in python
obj.getData()
print(obj.Summation())


obj1 = Calculator(4,5) #syntax to create objects in python
obj1.getData()
print(obj1.Summation())