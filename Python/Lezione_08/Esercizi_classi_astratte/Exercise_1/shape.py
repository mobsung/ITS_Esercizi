'''
Creating an Abstract Class with Abstract Methods
Start by defining an abstract base class called Shape. This class should include two abstract methods: one named area, which will be responsible for calculating the area of a shape, and another named perimeter, which will calculate the perimeter. Since Shape is abstract, it will not provide specific implementations for these methods. Instead, it sets a blueprint for all shapes that will inherit from it.

Then, create two concrete subclasses, Circle and Rectangle, that both extend the Shape class. Each of these subclasses must provide their own implementation of the area and perimeter methods, based on the geometric formulas appropriate to their shapes.

Finally, write a simple driver program (test code) that creates instances of Circle and Rectangle, calls their area and perimeter methods, and prints the results. This will help verify that your class hierarchy works as intended.
'''


from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def area(self) -> None:
        pass

    @abstractmethod
    def perimetro(self) -> None:
        pass

    def setShape(self, shape: str) -> None:
        if shape:
            self.shape = shape
        else:
            self.shape = ""
            print('La shape non puo essere una stringa vuota')

    def getShape(self) -> str:
        return self.shape