
#22) Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle.

def init(self, length, width):
    self.length = length
    self.width = width 
def area(self): 
    return self.length * self.width
    l=float(input("Please Enter Length of Rectangle : ")) 
    w=float(input("Please Enter width of Rectangle : ")) 
    r = Rectangle(l, w) 
    print("Area of Rectangle is :{} ".format(r.area()))
