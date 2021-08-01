from typing import List
import heapq

class Solution:
    def kWeakeatRows(self, mat:List[List[int]], k: int) -> List[int]:
        m, n = len(mat), len(mat[0])
        power = list()
        for i in range(m):
            l, r , pos = 0, n - 1, -1
            while l <= r:
                mid = (r - l)//2 + l
                if mat[i][mid] == 0:
                    r = mid - 1
                else:
                    pos = mid
                    l = mid + 1
            power.append((pos + 1, i))

        heapq.heapify(power)
        ans = list()
        for i in range(k):
            ans.append(heapq.heappop(power)[1])
        return ans

    def __init__(self) -> None:
        mat = [
            [1,1,1,1,0,0],
            [1,1,1,0,0,0],
            [1,1,1,1,1,0],
            [1,1,0,0,0,0],
            [1,0,0,0,0,0],
            [1,1,1,1,1,1],

        ]
        a =  self.kWeakeatRows(mat,5)
        print(a)


if __name__ == "__main__":
    s = Solution()
    

