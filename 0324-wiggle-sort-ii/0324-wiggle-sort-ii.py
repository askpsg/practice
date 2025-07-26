class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # for i in range(len(nums)):
        #     print(nums)
        #     if ((i < len(nums) - 1) and nums[i] == nums[i + 1]) or i == len(nums) - 1:
        #         k = 1
        #         while i + k < len(nums) and nums[i] == nums[i + k]:
        #             k += 1

        #         if i + k < len(nums):
        #             nums[i + 1], nums[i + k] = nums[i + k], nums[i + 1]
        #         else:
        #             for j in range(i):
        #                 if (nums[i-1] < nums[j] if i % 2 else nums[i-1] > nums[j]):
        #                     if j > 0 and (nums[j - 1] < nums[i] > nums[j + 1] if j % 2 else nums[j - 1] > nums[i] < nums[j + 1]):
        #                         nums[i], nums[j] = nums[j], nums[i]
        #                         break
        #                     elif j == 0 and (nums[i] > nums[j + 1] if j % 2 else nums[i] < nums[j + 1]):
        #                         nums[i], nums[j] = nums[j], nums[i]
        #                         break

        #     if i < len(nums) - 1 and (
        #         (i % 2 == 0 and nums[i] >= nums[i + 1]) or \
        #         (i % 2 == 1 and nums[i] <= nums[i + 1])):
        #         nums[i], nums[i + 1] = nums[i + 1], nums[i]

        sorted_nums = sorted(nums)
        sorted_nums.reverse()
        n = len(nums)
        b, a = sorted_nums[:n//2], sorted_nums[n//2:]
        i = 0
        while i < n:
            if not i % 2:
                nums[i] = a[i//2]
            else:
                nums[i] = b[i//2]

            i += 1
