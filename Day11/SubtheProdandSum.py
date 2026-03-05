class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum = 0
        prod = 1
        while n>0:
            num = n%10
            sum += num
            prod *= num
            n = n//10

        return prod - sum
        
