class Solution(object):
    def canBeIncreasing(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                count += 1
                if i>1 and nums[i] <= nums[i-2]:
                    nums[i] = nums[i-1]
        return count <= 1