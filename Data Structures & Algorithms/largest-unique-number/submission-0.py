class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        largest_int = -1


        for i in nums:
            if i <= largest_int or nums.count(i) > 1:
                continue
            largest_int = i
        
        return largest_int
