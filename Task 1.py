# Print simple Hello World
class Intro():
    def intro(self):
        # Take the object and print Hallo World
        print("Hallo world")

object = Intro() # creation of an object variable
object.intro() # Accessing class methods


# Simple addition
class Operator():
    def __init__(self,a,b): # passing the object and arguments
        self.a = a
        self.b = b

    def sum(self):
        print(self.a+self.b) # print the sum of two values

ans = Operator(1,3)  # creation of an object variable
ans.sum()  # Accessing class methods


