class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        sum = 0
        if num>1:
            for i in range(1,round(sqrt(num))+1):
                if num%i==0:
                    if (num/i)==num or num/i==i:
                        sum+=i
                    else:
                        sum+=i+num/i
            return sum==num
        else:
            return False
            
        
