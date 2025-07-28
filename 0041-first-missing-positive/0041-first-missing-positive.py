class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0

        m = max(nums)
        m += 1
        for i in range(len(nums)):
            orig = nums[i]
            if orig >= m:
                orig -= m

            if 0 < orig <= len(nums) and nums[orig - 1] < m:
                nums[orig - 1] += m

        for i in range(len(nums)):
            if nums[i] < m:
                return i + 1

        return len(nums) + 1
