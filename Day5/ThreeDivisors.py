import math
class Solution:
    def isThree(self, n: int) -> bool:
        n = math.sqrt(n)
        is_prime = True
        
        if n>1 and n==int(n):
            for i in range(2,int(n)):
                if n%i==0:
                    is_prime= False
        
            if is_prime:
                return True
            else:
                return False
        else:
            return False



        
