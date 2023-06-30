'''
Given an array Arr of N positive integers. Your task is to find the elements whose value
is equal to that of its index value ( Consider 1-based indexing ).

Note: There can be more than one element in the array which have the same value as its index.
You need to include every such element's index. Follows 1-based indexing of the array.
'''


class Solution:
    def valueEqualToIndex(self, arr, n):
        vals = []
        for idx in range(1, n + 1):
            if arr[idx - 1] == idx:
                vals.append(idx)
        return vals


sol = Solution()
print(sol.valueEqualToIndex([15, 2, 45, 12, 7], 5))
print(sol.valueEqualToIndex([1], 1))
