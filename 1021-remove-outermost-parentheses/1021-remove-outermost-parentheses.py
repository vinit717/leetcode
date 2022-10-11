class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        index = 0
        res = ''
        cnt = 0
        for i in range(len(s)):
            if s[i] == "(":
                cnt+=1
            elif s[i] == ")":
                cnt-=1
            if cnt == 0:
                res+=s[index+1:i]
                index = i+1
        return res
        
        
        
       