class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        n = len(nums)
        for i in range(n):
            hashmap[nums[i]] = i

        for i in range(n):
            diff = target - nums[i]
            for i in range(n):
                diff = target - nums[i]
                if diff in hashmap:
                    n = hashmap[diff]
                    if n > i:
                        return [i, n]
                    if n == i:
                        continue
                    else:
                        return [n, i]







