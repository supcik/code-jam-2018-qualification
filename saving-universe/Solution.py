import sys

class SwapException(Exception):
    pass

class RobotHack():

    def __init__(self, d, p):
        self.maxDamage = d
        self.program = [c for c in p]

    def damage(self):
        result = 0
        strength = 1
        for command in self.program:
            if command == 'S': # Shoot
                result += strength
            elif command == 'C': # Charge
                strength *= 2
            else:
                raise Exception("Invalid command : {}".format(command))
        return result

    def bestSwap(self):
        p = self.program
        i = len(p) - 2
        while i >= 0 and (p[i] == p[i+1] or p[i] == 'S'):
            i -= 1
        if i < 0:
            raise SwapException()
        else:
            p[i], p[i+1] = p[i+1], p[i]

    def solve(self):
        swapCount = 0
        while self.damage() > self.maxDamage:
            try:
                self.bestSwap()
                swapCount += 1
            except SwapException:
                return "IMPOSSIBLE"
        return swapCount


def main():
    t = int(input())
    for i in range(1, t + 1):
        line = input().split(" ")
        d, p = int(line[0]), [c for c in line[1]]
        rh = RobotHack(d,p)
        print("Case #{}: {}".format(i, rh.solve()))

if __name__ == "__main__":
    main()