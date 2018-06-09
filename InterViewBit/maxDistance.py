'''
Given an array A of integers, find the maximum of j - i subjected to the constraint of A[i] <= A[j].

If there is no solution possible, return -1.

Example :

A : [3 5 4 2]

Output : 2 
for the pair (3, 4)
'''
class Solution:

    def max_distance(self, A):
        n = len(A)
        Lmin = []
        Rmax = []

        Lmin.append(A[0])
        Rmax.append(A[n-1])

        for i in range(1,n):
            Lmin.append(min(Lmin[i-1], A[i]))

        for i in range(n-2,-1,-1):
            Rmax = [max(Rmax[0], A[i])] + Rmax
        
        maxDistance = 0
        i, j = 0, 0
        while i < n and j < n:
            if Lmin[i] < Rmax[j]:
                maxDistance = max(maxDistance, j-i)
                j += 1
            else:
                i += 1
        return maxDistance
            

