class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        m1, m2 = 1, 1
        
        for i in range(len(nums) - 1):
            m1 *= nums[i]
            res[i + 1] *= m1
            
            m2 *= nums[-1 - i]
            res[-1 - (i + 1)] *= m2
        
        return res
#         res = []
#         product = 1
#         for i in range(len(nums)):
#             product *= nums[i]
        
#         for j in range(len(nums)):
#             res.append(int(product/nums[j]))
#         return res
# #         res = []
#         for i in range(len(nums)):
#             product = 1
#             for j in range(len(nums)):
#                 if j == i:
#                     continue
#                 product *= nums[j]
#             res.append(product)
#         return res

# #Approach 2: 

# #Points to note about this approach
# # Works only if the input array does not contain any zeros
# # Won't be accepted since we can't use a division operator

# # Time complexity: O(n)
# # Space complexity: O(n)

# def productExceptSelf1(nums):
        