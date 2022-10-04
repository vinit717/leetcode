class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        N=len(nums)
        sumM=0
        for i in (nums):
            sumM=sumM+i
        x=N*(N+1)//2
        return x-sumM
        