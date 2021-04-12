from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums:[int]) -> str:
        def compare(x, y): return int(y+x) - int(x+y)
        nums = sorted(map(str, nums), key=cmp_to_key(compare))
        return "0" if nums[0]=="0" else "".join(nums)



    def __init__(self):
        a = self.largestNumber([40,8,9,48,30])
        print(a)
    

if __name__ == "__main__":
    solution = Solution()
    