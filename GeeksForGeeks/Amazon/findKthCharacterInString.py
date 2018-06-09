'''
Given a decimal number m. Convert it in binary string and apply n iterations, 
in each iteration 0 becomes 01 and 1 becomes 10. Find kth character in the 
string after nth iteration.

Input:
The first line consists of an integer T i.e number of test cases. The first and
only line of each test case consists of three integers m,k,n. 

Output:
Print the required output.

Constraints: 
1<=T<=100
1<=m<=50
1<=n<=10
0<=k<|Length of final string|

Example:
Input:
2
5 5 3
11 6 4

Output:
1
1
'''

class Solution:

    def __init__(self, m, n, k):
        self.m = m
        self.n = n
        self.k = k

    def kthCharacter(self):
        s = bin(self.m)[2:]
        oldS = s
        for j in range(self.n):
            newS = ''
            for i in oldS:
                if i == '1': newS += '10'
                else: newS += '01'
            oldS = newS
        return newS[self.k]

t = int(input())

for _ in range(t):
    m, k, n = map(int, input().split())
    S = Solution(m,n,k)
    print(S.kthCharacter())