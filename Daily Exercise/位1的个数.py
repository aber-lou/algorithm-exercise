class Solution:
    def hammingWeight(self, n: int) -> int:
        ret = sum(1 for i in range(32) if n & (1 << i))
        return ret

    def hammingWeight2(self, n: int) -> int:
        ret = 0
        while n:
            n = n & (n - 1)
            ret += 1

        return ret

    def __init__(self):
        print(self.hammingWeight(0o00110101010101010101010101))

if __name__ == "__main__":
    s = Solution()
