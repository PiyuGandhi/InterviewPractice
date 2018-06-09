'''
Given an integer array, find if an integer p exists in the array such that the number of integers greater than p in the array equals to p
If such an integer is found return 1 else return -1.
'''

class Solution:
    def nobleint(self, A):
        n = len(A)
        A.sort()
        for i in range(0,n):
            if i < n-1 and A[i] == A[i+1]: continue
            
            if A[i] == (n-1-i):
                return 1
        if A[n-1] == 0:
            return 1
        return -1

S = Solution()
A = [10, 3, 20, 40, 2]
print("Noble integer exists? ", S.nobleint(A))