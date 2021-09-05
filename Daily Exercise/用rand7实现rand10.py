import random
from typing import Collection

class Solution:
    def rand10(self) -> int:
        while True:
            row = rand7()
            col = rand7()
            idx = (row -1) * 7 + col
            if idx <= 40:
                return 1 + (idx -1) % 10

    def rand10With2(self) -> int:
        a = rand7()
        b = rand7()
        while a == 7 :
            a = rand7()

        while b > 5:
            b = rand7()
        
        return (0 if a & 1 == 1 else 5) + b


def rand7() -> int:
    return random;