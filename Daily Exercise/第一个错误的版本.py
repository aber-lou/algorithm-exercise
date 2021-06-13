class Solution:
    def firstBadVersion(self, n:int):
        left, right = 1, n
        while left < right :
            mid = left + (right - left) // 2

            if(self.isBadVersion(mid)):
                right = mid
            else:
                left = mid + 1
        
        return int(left)


    def isBadVersion(self, n: int) -> bool:
        if(n > 3):
            return True
        return False


    def __init__(self):
       version =  self.firstBadVersion(7)
       print(version)


if __name__ == "__main__":
    s = Solution()
