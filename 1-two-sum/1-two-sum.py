class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for i,el in enumerate(nums):
            if target - el in m:
                return[m[target-el],i]
            m[el]=i    
        