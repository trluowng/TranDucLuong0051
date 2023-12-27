import math
class Polygon:
    def __init__(self, num_sides):
        self.num_sides = num_sides
        self.sides = []
    def input_sides(self):
        for i in range(self.num_sides):
            side = float(input(f"Enter length of side {i+1}: "))
            self.sides.append(side)
    def perimeter(self):
        return sum(self.sides)
class Parallelogram(Polygon):
    def __init__(self):
        super().__init__(4) 
    def area(self):
        base = self.sides[0]
        height = float(input("Enter height: "))
        return base * height
class Rectangle(Parallelogram):
    def __init__(self):
        super().__init__()
class Square(Rectangle): 
    def __init__(self): 
      super().__init__() 
square = Square()
square.input_sides()

perimeter_square = square.perimeter()
area_square = square.area()

print(f"Perimeter of the square: {perimeter_square}")
print(f"Area of the square: {area_square}")