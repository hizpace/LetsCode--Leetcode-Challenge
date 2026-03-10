class Solution:
    def countEven(self, num: int) -> int:
        count = 0
        for num in range(1,num+1):
            dig_sum = 0
            while num>0:
                n = num%10
                dig_sum += n
                num = num//10
            if dig_sum%2==0:
                count+=1
        
        return count
