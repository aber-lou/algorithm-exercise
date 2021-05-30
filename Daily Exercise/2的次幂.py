class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n-1)) == 0

    def __init__(self) -> None:
       print( self.isPowerOfTwo(16))


if __name__ == "__main__":
    s = Solution()
