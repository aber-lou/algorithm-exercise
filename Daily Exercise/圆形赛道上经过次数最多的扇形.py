class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        s, d = rounds[0], rounds[-1]
        if s <= d:
            return list(range(s, d+1))
        else:
            return list(range(1,d+1)) + list(range(s,n+1))
        
