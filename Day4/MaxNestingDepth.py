class Solution:
    def maxDepth(self, s: str) -> int:
        s.split()
        curr = 0
        max = 0
        for i in s:
            if i=="(":
                curr+=1
                if curr>max:
                    max = curr
            elif i==")":
                curr-=1
                
        return max
        
