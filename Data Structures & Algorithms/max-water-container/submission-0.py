class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        ans = 0
        while left < right:
            if heights[left] > heights[right]:
                width = min(heights[left], heights[right]) 
                length = right - left
                v = width * length
                ans = max(ans, v)
                right -= 1
            else:
                width = min(heights[left], heights[right]) 
                length = right - left
                v = width * length
                ans = max(ans, v)
                left += 1



        return ans  
        #gonna fix this tonight  
        