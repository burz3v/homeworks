#question 9

class Shape:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f'It is a {self.name}'

class FourSides(Shape):
    def __init__(self, name, a, b, c, d):
        super().__init__(name)
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def __str__(self):
        return super().__str__() + f' with perimeter {self.getHekef()}'

    def getHekef(self):
        return self.a + self.b + self.c + self.d

s2 = FourSides('square',2,2,2,2)

print(s2)

class Rectangle(FourSides):
    def __init__(self,name,a,b,c,d):
        super().__init__(name,a,b,c,d)

    def __str__(self):
        return super().__str__() + f' and area {self.getArea()}'

    def getArea(self):
        return self.a * self.b

s3 = Rectangle('rect',3,2,3,2)

print(s3)

class Square(Rectangle):
    def __init__(self,name,a,b,c,d):
        super().__init__(name, a, b, c, d)

    def __str__(self):
        return super().__str__()

    def getHekef(self):
        return self.a * 4

    def getArea(self):
        return self.a * self.a

s4 = Square('squaaare',3,3,3,3)

print(s4)
