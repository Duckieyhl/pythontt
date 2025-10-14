import math

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def distance(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def area(self):
        a = self.p1.distance(self.p2)
        b = self.p2.distance(self.p3)
        c = self.p3.distance(self.p1)

        if a + b <= c or a + c <= b or b + c <= a:
            return "INVALID"

        s = (a + b + c) / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        return f"{area:.2f}"



t = int(input())
for i in range(t):
    x1, y1, x2, y2, x3, y3 = map(float, input().split())
    p1 = Point(x1, y1)
    p2 = Point(x2, y2)
    p3 = Point(x3, y3)

    tg = Triangle(p1, p2, p3)
    result = tg.area()
    if result == "INVALID":
       print("INVALID")
    else:
        print(result)
