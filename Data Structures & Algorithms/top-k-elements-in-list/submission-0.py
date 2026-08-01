class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        ans = []
        for i in range(len(nums)):
            if nums[i] in hashmap:
                hashmap[nums[i]] += 1
            else:
                hashmap[nums[i]] = 0

        sorted_dict = dict(sorted(hashmap.items(), key=lambda item: item[1], reverse=True))

        for i in range(k):
            n = list(sorted_dict)[i]
            ans.append(n)

        return ans
