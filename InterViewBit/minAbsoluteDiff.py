'''
Given an array of n distinct integers. 
The problem is to find the sum of minimum absolute difference 
of each array element. 
For an element x present at index i in the array 
its minimum absolute difference is calculated as:
Min absolute difference (x) = min(abs(x – arr[j])),
 where 1 <= j <= n and j != i and abs is the absolute value.
Input Constraint: 2 <= n Examples:

Input : arr = {4, 1, 5}
Output : 5
Sum of absolute differences is |4-5| + |1-4| + |5-4|

Input : arr = {5, 10, 1, 4, 8, 7}
Output : 9

Input : {12, 10, 15, 22, 21, 20, 1, 8, 9}
Output : 18


'''

class Solution:

    def minAbsoluteDiff(self, A):
        n = len(A)
        min_diff = abs(A[n-1] - A[0])
        for i in range(1,n):
            diff = abs(A[i] - A[i-1])
            if diff < min_diff: 
                min_diff = diff
        return min_diff

S = Solution()
A = [10, 12, 13, 15, 10]
print(S.minAbsoluteDiff(A))