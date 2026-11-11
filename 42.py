class Rectangle:
        def __init__ (self,length,breath) :
              self.length=length
              self.breath=breath
        def area(self):
              return self.length*self.breath      
        def perimeter(self) :
              return 2*(self.length + self.breath)

r1=Rectangle(10,5)
r2=Rectangle(8,6)
print("rectangle 1")
print("area :", r1.area())
print("perimeter:", r1.perimeter())
print("rectangle 2")
print("area :", r2.area())
print("perimeter:", r2.perimeter())

if r1.area() > r2.area() :
   print("\nRectangle 1 has greater area")
elif r1.area() < r2.area():
   print("\nRectangle 2 has greater area")
else:
   print("\nBoth Rectangle has equal area")


