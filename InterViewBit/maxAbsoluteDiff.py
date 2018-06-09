'''
You are given an array of N integers, A1, A2 ,…, AN. Return maximum value of f(i, j) for all 1 ≤ i, j ≤ N.
f(i, j) is defined as |A[i] - A[j]| + |i - j|, where |x| denotes absolute value of x.

For example,

A=[1, 3, -1]

f(1, 1) = f(2, 2) = f(3, 3) = 0
f(1, 2) = f(2, 1) = |1 - 3| + |1 - 2| = 3
f(1, 3) = f(3, 1) = |1 - (-1)| + |1 - 3| = 4
f(2, 3) = f(3, 2) = |3 - (-1)| + |2 - 3| = 5

So, we return 5.

'''
class Solution:
    def maxAbsoluteDiff(self, A):
        first_arr = [A[i] + i for i in range(0,len(A))]
        second_arr = [A[i] - i for i in range(0,len(A))]
        min1, max1 = min(first_arr), max(first_arr)
        min2, max2 = min(second_arr), max(second_arr)

        return max(max1 - min1, max2- min2)

S = Solution()
A = [ -70, -64, -6, -56, 64, 61, -57, 16, 48, -98 ]
print(S.maxAbsoluteDiff(A))
 