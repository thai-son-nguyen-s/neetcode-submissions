class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = set()
        l = len(nums)
        for n in nums:
            if n in count:
                return True
            else:
                count.add(n)
        
        return False