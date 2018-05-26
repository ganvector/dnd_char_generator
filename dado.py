
import random

class Dice:
    def d4(self):
        return random.uniform(1, 4)

    def d6(self):
        return random.uniform(1, 6)

    def d8(self):
        return random.uniform(1, 8)

    def d10(self):
        return random.uniform(1, 10)

    def d12(self):
        return random.uniform(1, 12)

    def d20(self):
        return random.uniform(1, 20)

    def d100(self):
        return random.uniform(1, 100)