import sys
import itertools

class TroubleSort():

    def __init__(self, v):
        self.v = v

    def doSort(self):
        l = self.v
        done = False
        while (not done):
            done = True
            for i in range(len(l)-2):
                if l[i] > l[i+2]:
                    done = False
                    l[i], l[i+2] = l[i+2], l[i]

    def doQuickSort(self):
        l1 = sorted(self.v[0::2])
        l2 = sorted(self.v[1::2])
        self.v = [j for i in itertools.zip_longest(l1,l2) for j in i if j is not None]

    def solve(self):
        self.doQuickSort()
        l = self.v
        for i in range(len(l)-1):
            if l[i] > l[i+1]:
                return i
        return "OK"


def main():
    t = int(input())
    for i in range(1, t + 1):
        _ = int(input())
        v = [int(s) for s in input().split(" ")]
        t = TroubleSort(v)
        print("Case #{}: {}".format(i, t.solve()))

if __name__ == "__main__":
    main()