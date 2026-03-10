class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        digsum = 0
        temp = x
        while x>0:
            n = x%10
            digsum += n
            x = x//10

        if temp%digsum==0:
            return digsum
        else:
            return -1
