class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        hashtable = {}
        for i in range(len(nums)):
            val = nums[i]
            hashtable[val] = i
        for i in range(len(nums) + 1):
            if i not in hashtable:
                return i
             