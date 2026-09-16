class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = {}
        for i in range(len(nums)):
            val = nums[i]
            hashtable[val] = i
        for j in range(len(nums)):
            need = target - nums[j]
            
            if need in hashtable and j != hashtable[need]:
                return [j, hashtable[need]]
            else:
                continue