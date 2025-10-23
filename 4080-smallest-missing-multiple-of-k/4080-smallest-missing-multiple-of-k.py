class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        found = {}
        for n in nums:
            index = n//k
            if index == n/k:
                found[index] = True
        
        for index in range(1, len(nums) + 3):
            if not found.get(index, False):
                return k*index
        
        return -1
