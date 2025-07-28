class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        m = 0
        for i in range(n):
            if nums[i] < 0:
                nums[i] = 0
            elif nums[i] > m:
                m = nums[i]

        m += 1
        for i in range(n):
            orig = nums[i]
            if orig >= m:
                orig -= m

            if 0 < orig <= n and nums[orig - 1] < m:
                nums[orig - 1] += m

        for i in range(n):
            if nums[i] < m:
                return i + 1

        return n + 1
