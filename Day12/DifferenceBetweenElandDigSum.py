class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        el_sum = 0
        dig_sum = 0
        for num in nums:
            el_sum += num
            while num>0:
                n = num%10
                dig_sum += n
                num = num//10

        return abs(el_sum-dig_sum)    
    
        
