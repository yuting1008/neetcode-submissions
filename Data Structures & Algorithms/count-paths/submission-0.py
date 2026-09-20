class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def factorial_loop(n):
            res = 1
            for i in range(1, n + 1):
                res *= i
            return res

        a = factorial_loop(m + n - 2)
        b = factorial_loop(m - 1) * factorial_loop(n - 1)
        
        return int(a/b)