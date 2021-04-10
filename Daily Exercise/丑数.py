class Solution:

    def isUgly3(self,n:int) -> int:
        sum = [1]

        ugly = 2
        while len(sum) < n:
            if self.isUgly2(ugly):
                sum.append(ugly)
            ugly += 1
        
        if len(sum) == n:
            return sum[len(sum) - 1]


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

    def __init__(self):
       a =  self.isUgly3(350)
       print(a)


if __name__ == "__main__":
    s = Solution()



        
