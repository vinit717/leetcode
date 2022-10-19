class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        
        """
        curr_max = arr[-1]
        arr[-1] = -1
        for i in range(len(arr)-2,-1,-1):
            curr = arr[i]
            arr[i] = curr_max
            if curr>curr_max:
                curr_max = curr
        return arr
    
        