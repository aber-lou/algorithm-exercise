class Solution:
    def guessNumber(self,n: int) -> int:
        left, right = 1, n
        while left < right:
            mid = left + (right - left) // 2

            status = guess(mid)
            if status == 0:
                return mid
            elif status == -1:
                right = mid
            elif status == 1:
                left = mid + 1
        
        return left