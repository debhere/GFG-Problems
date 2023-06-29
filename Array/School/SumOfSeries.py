'''
Write a program to find the sum of the given series 1+2+3+ . . . . . .(N terms)
'''


class Solution:
    def seriesSum(self, n):
        return n * (n+1)//2


sol = Solution()
print(sol.seriesSum(5))
