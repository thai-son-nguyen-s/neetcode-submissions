class Solution:
    def climbStairs(self, n: int) -> int:
        def solving(n, memo={}):
            if n <=2:
                return n
            if n in memo:
                return memo[n]
            memo[n] = solving(n-1) + solving(n-2)
            return memo[n]
        return solving(n)