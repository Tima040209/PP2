#Define a class named Rectangle which inherits from Shape class from task 2. Class instance can be constructed by
# a length and width. The Rectangle class has a method which can compute the area
class Shape():
    def __init__(self) :
        pass
    def area(self):
        return 0
         
class Rectangle(Shape):    
    def __init__(self,length,width):
        Shape.__init__(self)
        self.lentgh = length
        self.width = width
    def area(self):
        return self.lentgh*self.width
req = Rectangle(int(input()),int(input()))
print(req.area()) 
