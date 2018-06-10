"""
Given an unsorted array. The task is to find all the star and super star elements in the array. Star are those elements which are strictly greater than all the elements on its right side. Super star are those elements which are strictly greater than all the elements on its left and right side.

Note: Assume first element (A[0]) is greater than all the elements on its left side, And last element (A[n-1]) is greater than all the elements on its right side.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case consists of two lines. First line of each test case contains an Integer N denoting size of array and the second line contains N space separated elements.

Output:
For each test case, print the space separated star elements and then in new line print super star elements. If no super star element present in array then print "-1".

Constraints:
1<=T<=200
1<=N<=106
1<=A[i]<=106

Example:
Input:
2
6
4 2 5 7 2 1
3
8 6 5

Output:
7 2 1
7
8 6 5
8
"""

class Solution:

    def __init__(self, n, A):
        self.n = n
        self.A = A

    def findStarElements(self):
        superStar = -1
        starElements = []
        maxCurrent = -1e6

        for i in self.A[::-1]:
            if i == superStar:
                superStar = -1            
            
            
            if i == maxCurrent:
                continue
            
            
            if i  > maxCurrent:
                starElements.append(i)
                maxCurrent = i
                superStar = i
                continue

            
            
        starElements.sort(reverse=True)
        return starElements, superStar

t = int(input())

for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    S = Solution(n ,A)
    starElements, superStar  = S.findStarElements()
    print(' '.join(map(str, starElements)))
    print(superStar)
