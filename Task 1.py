# Print simple Hello World
class Intro:
    def intro(self):
        # Take the object and print Hallo World
        print("Hallo world")


object1 = Intro()  # creation of an object variable
object1.intro()  # Accessing class methods


# Simple addition
class Operator:
    def __init__(self,num1,num2):  # passing the object and arguments
        self.num1 = num1
        self.num2 = num2

    def sum(self):
        print(self.num1+self.num2)  # print the sum of two values


ans = Operator(1,3)  # creation of an object variable
ans.sum()  # Accessing class methods


