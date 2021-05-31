class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        
        return (n & (n - 1)) == 0 and (n & 0xaaaaaaaa) == 0


    def __init__(self) -> None:
        print(self.isPowerOfFour(4))


if __name__ == "__main__":
    solution = Solution()