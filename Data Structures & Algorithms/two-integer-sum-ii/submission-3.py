class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0 
        r = len(numbers) - 1
        sums = 0
        while l < r:
            sums = numbers[l] + numbers[r]
            if sums == target:
                return [l + 1, r + 1]
            if sums < target:
                l += 1
            if sums > target:
                r -= 1