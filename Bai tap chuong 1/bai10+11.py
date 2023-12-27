import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
class Ellipse(Point):
    def __init__(self, x_center, y_center, a_axis_length, b_axis_length):
        super().__init__(x_center, y_center)
        self.a = a_axis_length
        self.b = b_axis_length
    def area(self):
        return math.pi * self.a * self.b
class Circle(Ellipse):
    def __init__(self, x_center, y_center, radius):
        super().__init__(x_center,y_center,radius,radius)
# Tạo một đối tượng Elip với các thuộc tính 
elip = Ellipse(0, 0, 5, 3)
# Tính diện tích của elip
elip_area = elip.area()
print("Diện tích của elip là:", elip_area)
# Tạo một đối tượng Circle 
circle = Circle(0, 0, 5)
# Tính diện tích của hình tròn
circle_area = circle.area()
print("Diện tích của hình tròn là:", circle_area)


