"""
Given an array of distinct integers, print all the pairs having positive value and negative value 
of a number that exists in the array.

NOTE: If there is no such pair in the array , print "0".

Input:
The first line consists of an integer T i.e number of test cases. The first line of each 
test case consists of an integer n.The next line of each test case consists of n spaced integers.

Output:
Print all the required pairs in the increasing order of their absolute numbers.

Constraints: 
1<=T<=100
1<=n<=1000
-1000<=a[i]<=1000

Example:
Input:
2
6
1 -3 2 3 6 -1
8
4 8 9 -4 1 -1 -8 -9

Output:
-1 1 -3 3 
-1 1 -4 4 -8 8 -9 9 
"""


class Solution:

    def __init__(self, n, A):
        self.n = n
        self.A = A
    
    def findPairs(self):
        ans = []
        self.A.sort()
        startIdx = 0
        endIdx = n-1
        while startIdx < endIdx:
            if self.A[startIdx]*-1 == self.A[endIdx]:
                ans.append([self.A[startIdx], self.A[endIdx]])
                startIdx += 1
                endIdx -= 1
                continue
            if self.A[startIdx]*-1 < self.A[endIdx]:
                endIdx -= 1
                continue
            if self.A[startIdx]*-1 > self.A[endIdx]:
                startIdx += 1
                continue
        if len(ans) == 0:
            print(0, end=' ')
            return

        for i in ans[::-1]:
            print(i[0], i[1], sep=' ', end= ' ')



for _ in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))
    S = Solution(n, A)
    S.findPairs()
    print('')
