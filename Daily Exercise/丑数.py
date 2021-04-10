class Solution:
    def isUgly(self,n:int) -> bool:

        if n <= 0:
            return False

        if  n == 1 :
            return True

        
        while n % 2 == 0:
            return self.isUgly(n / 2)
        while n % 3 == 0:
            return self.isUgly(n / 3)
        while n % 5 == 0:
            return self.isUgly(n / 5)
        
        return False
        
    def isUgly2(self, n:int) -> bool:
        if n <=0:
            return False
        
        divide = [2,3,5]
        for d in divide:
            while n % d == 0:
                n /= d
        
        return n == 1


        
