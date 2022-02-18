class Shape():
    def __init__(self) :
        pass
    def area(self):
        return 0
         
class Square(Shape):    
    def __init__(self,length=0):
        Shape.__init__(self)
        self.lentgh = length
    def area(self):
        return self.lentgh*self.lentgh
print(Square().area())        
