'''
Rearrange a given array so that Arr[i] becomes Arr[Arr[i]] with O(1) extra space.

Example:

Input : [1, 0]
Return : [0, 1]
 Lets say N = size of the array. Then, following holds true :
All elements in the array are in the range [0, N-1]
N * N does not overflow for a signed integer
'''
class Solution:
    def rearrange(self, A):

        n = len(A)
        for i in range(n):
            A[i] += ( A[A[i]] % n  ) * n

        for i in range(0,n):
            A[i] = int(A[i]/n)

        return A

S = Solution()
A = [1,0]
print(S.rearrange(A))
        