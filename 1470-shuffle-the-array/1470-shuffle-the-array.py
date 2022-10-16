class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        l=0
        r=len(nums)//2
        ans=[]
        while l<len(nums)//2 and r<len(nums):
            ans.append(nums[l])
            l+=1
            ans.append(nums[r])
            r+=1
        return ans
       
            
            