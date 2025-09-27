'''
Confronti vasche di reazione: contano resa (area) e bordo (perimetro). Scrivi `Rectangle(w, h)` con `area()`, `perimeter()` e `__eq__` basato sull'**area**. Mantieni la firma data e fai superare tutti i test automatici.
'''


class Rectangle:
    
    def __init__(self, w: int, h:int) -> None:
        self.w = w
        self.h = h

    def area(self) -> int:
        return self.w * self.h
    
    def perimeter(self) -> int:
        return self.w * 2 + self.h * 2
    
    def __eq__(self, value):
        
        if self.area() == value.area():
            return True
        else:
            return False