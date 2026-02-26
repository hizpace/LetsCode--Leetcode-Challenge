class Solution:
    def averageValue(self, nums: List[int]) -> int:
        try:
            lst = []
            for i in nums:
                if i%2==0 and i%3==0:
                    lst.append(i)
            avg = int(sum(lst)/len(lst))
            return avg
        except ZeroDivisionError:
            return 0
