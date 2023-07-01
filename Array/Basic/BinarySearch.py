'''
Given a sorted array of size N and an integer K,
find the position(0-based indexing) at which K is present in the array using binary search.
'''


class Solution:
    def binarySearch(self, arr, n, k):
        start = 0
        end = n - 1
        mid = 0

        while start <= end:
            mid = (start + end) // 2

            if arr[mid] > k:
                end = mid - 1
            elif arr[mid] < k:
                start = mid + 1
            else:
                return mid
        return -1


sol = Solution()
print(sol.binarySearch([2, 3, 5, 8, 10], 5, 5))
