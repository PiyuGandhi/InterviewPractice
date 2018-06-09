'''
Given an unsorted array of size n. 
Array elements are in range from 1 to n. 
One number from set {1, 2, …n} is missing and 
one number occurs twice in array. Find these two numbers.

Examples:

  arr[] = {3, 1, 3}
  Output: 2, 3   // 2 is missing and 3 occurs twice 

  arr[] = {4, 3, 6, 2, 1, 1}
  Output: 1, 5  // 5 is missing and 1 occurs twice 

'''
class Solution:
    def missAndRepeat(self, A):
        n = len(A)
        req = set([i for i in range(1,n+1)])
        miss = list(req - set(A))[0]
        m = {}
        for i in range(0,n):
            if A[i] in m:
                multiple = A[i]
                break
            else:
                m[A[i]] = 1
        return [miss, multiple]

S = Solution()
A = [1,2,3,4,5,6,8,8,9]
print(S.missAndRepeat(A))