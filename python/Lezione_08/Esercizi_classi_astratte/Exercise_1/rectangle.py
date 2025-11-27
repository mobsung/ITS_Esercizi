'''
Creating an Abstract Class with Abstract Methods
Start by defining an abstract base class called Shape. This class should include two abstract methods: one named area, which will be responsible for calculating the area of a shape, and another named perimeter, which will calculate the perimeter. Since Shape is abstract, it will not provide specific implementations for these methods. Instead, it sets a blueprint for all shapes that will inherit from it.

Then, create two concrete subclasses, Circle and Rectangle, that both extend the Shape class. Each of these subclasses must provide their own implementation of the area and perimeter methods, based on the geometric formulas appropriate to their shapes.

Finally, write a simple driver program (test code) that creates instances of Circle and Rectangle, calls their area and perimeter methods, and prints the results. This will help verify that your class hierarchy works as intended.
'''

from shape import Shape


class Rectangle(Shape):

    def __init__(self, base: float, altezza: float):
        self.base = base
        self.altezza = altezza
        
    def area(self) -> float:
        return self.base * self.altezza
    
    def perimetro(self) -> float:
        return self.altezza * 2 + self.base * 2
    

if __name__ == "__main__":

    r1: Rectangle =  Rectangle(10, 4)
    print(r1.perimetro())
    print(r1.area())