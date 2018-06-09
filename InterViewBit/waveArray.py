'''
Given an array of integers, sort the array into a wave like array and return it, 
In other words, arrange the elements into a sequence such that a1 >= a2 <= a3 >= a4 <= a5.....

Example

Given [1, 2, 3, 4]

One possible answer : [2, 1, 4, 3]
Another possible answer : [4, 1, 3, 2]
'''
class Solution:
    def waveArray(self, A):
        for i in range(0,len(A), 2):
            if i > 0 and A[i] < A[i-1]:
                A[i], A[i-1] = A[i-1],A[i]
            if i < len(A)-1 and A[i] < A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]
        return A

S = Solution()
A = [10, 90, 49, 2, 1, 5, 23]

print(S.waveArray(A))