class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x>=0:
            num = x
            rev = 0
            while x>0:
                n = x%10
                rev = rev*10 + n
                x = x//10
            if rev==num:
                return True
            else:
                return False
        else:
            return False
            

            
        
        
