class Solution:
    def partition(self,s:str) -> list[list[str]]:
        self.res = []
        self.path = []
        self.dfs_backtrace(s)
        return self.res

    def dfs_backtrace(self, s:str) -> None:
        n = len(s)
        if n == 0:
            self.res.append(self.path[:])
        for j in range(n):
            if self.isPalindrome(s[ :j+1]) == True:
                self.path.append(s[ :j+1])
                self.dfs_backtrace(s[j+1: ])
                self.path.pop(-1)


    def isPalindrome(self, s: str) -> bool:
        return s == s[::-1]