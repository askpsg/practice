class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 1:
            return 0

        num_map = {num: True for num in nums}

        max_length = 0
        for num in num_map:
            if num - 1 not in num_map:
                current_length = 1
                current_num = num
                while current_num + 1 in num_map:
                    current_length += 1
                    current_num += 1

                max_length = max(max_length, current_length)
        
        return max_length
