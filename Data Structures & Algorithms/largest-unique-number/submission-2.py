class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        largest_int = -1
        for num in nums:
            if num <= largest_int or nums.count(num) > 1:
                continue
            largest_int = num

        
        
        return largest_int
