class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        for i in range(1,round(sqrt(num))+1):
            if i*i==num:
                return True
        return False
        
