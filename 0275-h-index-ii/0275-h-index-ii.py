class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        s, e = 0, n - 1
        ans = 0
        while s <= e:
            m = (s+e)//2
            r = n - m
            if citations[m] == r:
                ans = r
                break
            elif citations[m] < r:
                s = m + 1
            else:
                e = m - 1
                ans = r
        
        return ans
