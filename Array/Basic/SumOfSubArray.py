'''
Given an unsorted array A of size N that contains only positive integers, find a continuous sub-array that adds to a given number S and
return the left and right index(1-based indexing) of that subarray.
'''


class Solution:
    def subArraySum(self, arr, n, s):
        res = []
        for i in range(n - 1):
            tot = 0
            for j in range(i, n):
                tot += arr[j]
                res.append(j + 1)
                if tot == s:
                    # return res
                    return [res[0], res[-1]]
            res.clear()
        return -1


def main():
    T = int(input())

    while T > 0:
        NS = input().strip().split()
        N = int(NS[0])
        S = int(NS[1])
        A = list(map(int, input().split()))
        sol = Solution()
        ans = sol.subArraySum(A, N, S)
        for i in ans:
            print(i, end=' ')
        print()
        T -= 1


if __name__ == '__main__':
    main()
