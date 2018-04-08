import math
import sys

class Point2D:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def rotate(self, angle):
        if angle != 0:
            r = math.sqrt(self.x * self.x + self.y * self.y)
            a = math.atan2(self.y, self.x)
            a += angle
            self.x = r * math.cos(a)
            self.y = r * math.sin(a)

    def __repr__(self):
        return "[{}, {}]".format(self.x, self.y)


class Point3D:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def rotateX(self, alpha):
        p = Point2D(self.z, self.y)
        p.rotate(alpha)
        self.z = p.x
        self.y = p.y

    def rotateZ(self, alpha):
        p = Point2D(self.x, self.y)
        p.rotate(alpha)
        self.x = p.x
        self.y = p.y

    def asList(self):
        return (self.x, self.y, self.z)

    def __repr__(self):
        return "[{}, {}, {}]".format(self.x, self.y, self.z)

class Ufo:

    def __init__(self, x=0, z=0):
        self.x = x
        self.z = z

    def rotate(self, x, z=0):
        self.x = x
        self.z = z

    def pt(self, x, y, z):
        p = Point3D(x, y, z)
        p.rotateX(self.x)
        p.rotateZ(self.z)
        return p

    def solve(self, a):
        if a > 1.0 and a <= math.sqrt(2):
            x = math.pi/4 - math.acos(a / math.sqrt(2))
            self.rotate(0, x)
        elif a > math.sqrt(2):
            # https://www.wolframalpha.com/input/?i=sqrt(2)*cos(x)+%2B+sin(x)
            # https://www.wolframalpha.com/input/?i=solve+sqrt(2)*cos(x)+%2B+sin(x)+%3D+a
            # https://www.wolframalpha.com/input/?i=2+(tan%5E(-1)((1+-+sqrt(3+-+a*a))%2F(sqrt(2)+%2B+a)))
            # https://www.wolframalpha.com/input/?i=2+tan%5E(-1)(1%2F(sqrt(2)+%2B+sqrt(3))
            try:
                x = 2 * math.atan((1 - math.sqrt(3 - a*a)) / (a + math.sqrt(2)))
            except:
                x = 2 * math.atan(1 / (math.sqrt(2) + math.sqrt(3)))

            self.rotate(math.pi/4, x)

        print (*self.pt(0.5,0,0).asList())
        print (*self.pt(0,0.5,0).asList())
        print (*self.pt(0,0,0.5).asList())


def main():
    t = int(input())
    for i in range(1, t + 1):
        a = float(input())
        u = Ufo()
        print("Case #{}:".format(i))
        u.solve(a)

if __name__ == "__main__":
    main()
