from typing import List


class Solution:
    def sortBollnoon(self, arr:List[int]) -> List[int]:
        l = len(arr)
        print(l)
        s = 0
        e = l - 1

        i = 0
        while(i < e and i < l):
            if i == s and arr[i] == 0:
                s += 1
                i += 1
                continue

            if arr[i] == 0 and i > s:
                tem = arr[i] 
                arr[i] = arr[s]
                arr[s] = tem
                s += 1
            
            if arr[i] == 2 and e > i:
                tem = arr[i]
                arr[i] = arr[e]
                arr[e] = tem
                e -= 1

            if arr[i] == 1:
                i += 1
            print(arr,i)
        return arr


    def bubbleSort(self,arr:List[int]) -> List[int]:
        l = len(arr) - 1

        for i in range(l):
            for j in range(0,l-i):
                if arr[j] > arr[j+1]:
                    tem = arr[j]
                    arr[j] = arr[j+1]
                    arr[j+1] = tem
        return arr

    def __init__(self) -> None:
        bollNoonArr = self.sortBollnoon([0,1,2,1,0,0,0,0,2,0,1,0,2,2,1,0,1,2,0])

        sortArr = [9,6,5,4,0,12]
        a = self.bubbleSort(sortArr)
        print(a)  

if __name__ == "__main__":
    s = Solution()