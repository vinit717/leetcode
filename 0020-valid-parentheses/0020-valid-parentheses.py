class Solution:
    def isValid(self, s: str) -> bool:
           # TC = O(n) ; SC = O(n)
        # because we need to iterate over the string once
        # and we are using a check dictionary and stack for space 
        # so space complexity = O(n)
        
        n = len(s)
        if  n < 2:
            return False
        
        # odd length strings wont ever be balanced/valid
        # similarly strings with a single bracket wont be valid
        
        check = {'(':')', '{':'}','[':']'}
        stack1 = []
        for bracket in s:
            # if ith character is opening bracket
            # then add it to stack 
            if bracket in check:
                stack1.append(bracket)
            # otherwise if the stack is empty 
            # or if the closing bracket is not of the same type as the opening one
            # then sequence is not valid
            elif len(stack1) == 0 or check[stack1.pop()] != bracket:
                return False
            
        # if length of the stack is 0 meaning that all opening and closing 
        # brackets matched then ans is Valid
        return len(stack1) == 0
        