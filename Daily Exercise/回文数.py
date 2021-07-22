class Solution:
        def isPalindrome(self, x:int) -> bool:
            return True if x > 0 and x == int(str(x)[::-1]) else False