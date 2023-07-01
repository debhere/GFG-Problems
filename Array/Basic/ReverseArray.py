'''
Given an array arr[] of positive integers of size N. Reverse every sub-array group of size K.
'''


class Solution:
    def reverseInGroups(self, arr, N, K):
        return arr[K-1:: -1] + arr[N-1:K-1:-1]


sol = Solution()
print(sol.reverseInGroups([1, 2, 3, 4, 5], 5, 3))
print(sol.reverseInGroups([5, 6, 8, 9], 4, 3))
