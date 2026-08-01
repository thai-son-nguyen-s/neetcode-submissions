class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        hashmap = set()
        for i in range(n):
            if nums[i] in hashmap:
                return True
            else:
                hashmap.add(nums[i])
        return False