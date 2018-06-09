'''
Find the contiguous subarray within an array 
(containing at least one number) which has the largest sum.

For example:

Given the array [-2,1,-3,4,-1,2,1,-5,4],

the contiguous subarray [4,-1,2,1] has the largest sum = 6.

For this problem, return the maximum sum.

'''

class Solution:
    def max_contagious_array(self, A):
        n = len(A)
        if n == 1: return A[0]
        ans = A[0]
        curr = A[0]
        for i in range(1,n):
            curr += A[i]
            if curr < A[i]: curr = A[i]
            if ans < curr: ans = curr
        return ans

S = Solution()
A = [-2,1,-3,4,-1,2,1,-5,4]

print(S.max_contagious_array(A))