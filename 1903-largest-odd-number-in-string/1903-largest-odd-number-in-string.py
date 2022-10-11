class Solution:
    def largestOddNumber(self, num: str) -> str:
        # We have to just find the last index of an odd number, then slice the number upto that index,  becuase an odd number always ends with a number which is not divisible by 2 :)
        
        # Lets take the last index of an odd number as -1
        last_ind = -1
        
        # Iterate through all the numbers for finding a odd number that appears on the last.
        for i , j in enumerate(num[::-1]):
            if(int(j) % 2 != 0):
                last_ind = len(num) - i
                break
        
        # If there is no odd number, return empty string.
        if(last_ind == -1): return ""
                
        # Or return the string upto that index.
        return(num[:last_ind])