"""
Given an array of integers, find a combination of four elements in the array whose sum is equal to a given value X.

Input:
First line consists of T test cases. First line of every test case consists of an integer N, 
denoting the number of elements in an array. 
Second line consists of N spaced array elements. Third line of every test case X.

Output:
Single line output, print 1 if combination is found else 0.

Constraints:
1<=T<=100
1<=N<=100

Example:
Input:
1
6
1 5 1 0 6 0
7
Output:
1
"""

class Solution:

    def __init__(self, n ,A, X):
        self.n = n
        self.A = A
        self.X = X

    def fourElements(self):
        sumMap = {}
        pairs = []
        countEle = {}

        for i in range(self.n):
            if self.A[i] in countEle: countEle[self.A[i]]+= 1
            else: countEle[self.A[i]] = 1
            for j in range(i+1,self.n):
                pairs.append((self.A[i], self.A[j]))
                if (self.A[i] + self.A[j]) in sumMap:
                    sumMap[(self.A[i] + self.A[j])].append( (self.A[i], self.A[j]) )
                else:
                    sumMap[(self.A[i] + self.A[j])] = [(self.A[i], self.A[j])]
        
        for i in sumMap:
            if (self.X - i) in sumMap:
                if (self.X-i)*2 == self.X :
                    if len(sumMap[i]) > 1:
                        pair1 = list(sumMap[i][0])
                        pair2 = list(sumMap[i][1])
                        if (pair1[0] in pair2):
                            if pair1.count(pair1[0]) + pair2.count(pair1[0]) > countEle[pair1[0]]:
                                continue
                            elif pair1[1] in pair2:
                                if pair1.count(pair1[1]) + pair2.count(pair1[1]) > countEle[pair1[1]]:
                                    continue
                        if pair1[1] in pair2:
                            if pair1.count(pair1[1]) + pair2.count(pair1[1]) > countEle[pair1[1]]:
                                continue
                                
                        return 1
                else:
                    pair1 = list(sumMap[i][0])
                    pair2 = list(sumMap[X-i][0])
                    if (pair1[0] in pair2):
                        if pair1.count(pair1[0]) + pair2.count(pair1[0]) > countEle[pair1[0]]:
                            continue
                        elif pair1[1] in pair2:
                            if pair1.count(pair1[1]) + pair2.count(pair1[1]) > countEle[pair1[1]]:
                                continue
                    if pair1[1] in pair2:
                        if pair1.count(pair1[1]) + pair2.count(pair1[1]) > countEle[pair1[1]]:
                            continue
                    return 1
        return 0

t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    X = int(input())
    S = Solution(n, A, X)
    print(S.fourElements())
                
                


