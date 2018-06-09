'''
Given a Matrix of size M x N. Your task is to print the matrix K times left 
rotated.

Input:
First line consists of T test cases. First line of every test case consists of 
3 integers, M, N, K. Second line of every test case consists of M*N spaced 
integers.

Output:
Single line output, print the M*N spaced integer rotated K times.

Constraints:
1<=T<=100
1<=M,N,K<=100

Example:
Input:
1
2 2 1
1 2 3 4
Output:
2 1 4 3 
'''

class Solution:
    
    def __init__(self, n, m, k, A):
        self.n = n
        self.m = m
        self.k = k
        self.A = A

    def build_matrix(self):
        matrix = []
        startIdx = 0
        endIdx = self.n
        for i in range(self.m):
            matrix.append(self.A[startIdx : startIdx +self.n])
            startIdx += self.n
        return matrix

    def rotateArray(self, X):
        tmp = [0]*self.n
        for i in range(self.n):
            tmp[(i - self.k)%self.n] = X[i]
        return tmp

    def leftRotateKTimes(self):
        matrix = self.build_matrix()
        newMatrix = []
        for i in matrix:
            newMatrix.extend(self.rotateArray(i))
        return newMatrix

t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split())
    A = list(map(int, input().split()))
    S = Solution(n, m, k, A)
    print(' '.join(map(str,S.leftRotateKTimes())))
