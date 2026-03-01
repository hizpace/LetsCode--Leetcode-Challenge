class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums = sorted(nums)
        lst = []
        for i in range(len(nums)):
            if i%2==0:
                lst.append(nums[i+1])
            else:
                lst.append(nums[i-1])

        return lst
