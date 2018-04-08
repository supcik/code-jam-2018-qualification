import sys
import itertools
import math

class Gopher():

    FIELD_SIZE = 1000

    def __init__(self, a):
        self.a = a
        self.w = max(3, int(math.sqrt(a)))         
        self.h = max(3, math.ceil(a / self.w))
        self.field = [[False for y in range(self.h)] for x in range(self.w)]
        # print (self.field, file=sys.stderr)

    def holesAround(self, x, y):
        res = 0
        for i in range (x-1, x+2):
            for j in range (y-1, y+2):
                if self.field[i][j]:
                    res += 1
        return res

    def bestPos(self):
        minH = 10
        bestPos = (1,1)
        for x in range(1, self.w-1):
            for y in range(1, self.h-1):
                h = self.holesAround(x,y)
                if h == 0:
                    return (x,y)
                else:
                    if h < minH:
                        minH = h
                        bestPos = (x,y)
        return bestPos

    def run(self):
        while True:
            guess = self.bestPos()
            print(guess[0]+1, guess[1]+1)
            x, y = [int(s) for s in input().split(" ")]
            # print (x, y, file=sys.stderr)
            if x == 0 and y == 0:
                return # Done
            if x == -1 or y == -1:
                raise Exception("Failed")
            self.field[x-1][y-1] = True

def main():
    t = int(input())
    for _ in range(1, t + 1):
        a = int(input())
        g = Gopher(a)
        try:
            g.run()
        except Exception:
            return

if __name__ == "__main__":
    main()