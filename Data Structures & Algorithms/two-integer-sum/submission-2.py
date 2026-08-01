class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        n = 0
       
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hashmap:
                n = hashmap[diff]
                if n > i:
                    return [i, n]
                if n == i:
                    continue
                else:
                    return [n, i]

