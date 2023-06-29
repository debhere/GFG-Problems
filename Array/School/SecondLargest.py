'''
Given an array Arr of size N, print second largest distinct element from an array.
'''


class Solution:
    def print2largest(self, arr, n):
        l = list(set(arr))
        l.sort(reverse=True)
        if len(l) > 1:
            return l[1]
        else:
            return l[0]


sol = Solution()
print(sol.print2largest([12, 35, 1, 10, 34, 1], 6))
