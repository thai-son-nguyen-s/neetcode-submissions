class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashtable = {}
        ans = []
        for i in range(len(nums2)):
            val = nums2[i]
            hashtable[val] = i
        for i in range(len(nums1)):
            n = hashtable[nums1[i]]
            ans.append(n)
        return ans
        