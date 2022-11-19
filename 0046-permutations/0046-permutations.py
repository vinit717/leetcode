class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
         
        res = []
        def dfs(path, num): # record the path and remaining numbers
            if not num:
                res.append(path)    # When finished iterating, append path to result
                return
            for i in range(len(num)):
                dfs(path + [num[i]], num[:i] + num[i + 1:]) 
                # append the current number to path and iterate with the unused numbers
        
        dfs([], nums)
        return res  # return results
        