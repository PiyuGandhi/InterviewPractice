'''
Given two integers ‘L’ and ‘R’, write a program that finds the count of numbers having 
prime number of set bits in their binary representation in the range [L, R].

Input:
The first line consists of an integer T i.e number of test cases. The first and only 
line of each test case consists of two integers L and R. 

Output:
Print the required output.

Constraints: 
1<=T<=100
1<=L<=R<=100000

Example:
Input:
2
6 10
10 15 

Output:
4
5
'''

class Solution:

    def __init__(self, L, R):
        self.L = L
        self.R = R
        self.primeNoBitsMax = [2,3,5,7,11,13,17,19,23]
    
    # bin() function is 10^6 times faster than division method
    # def convert_to_bin(self, x):
    #     bin = ''
    #     while x > 0:
    #         if (x % 2 == 0):
    #             bin += '0'
    #         else:
    #             bin += '1'
    #         x = x//2
    #     return bin.count('1')


    def primeNoSetBits(self):
        ans = 0

        for i in range(self.L, self.R+1):
            # print(i, ', ' ,self.convert_to_bin(i))
            if bin(i).count('1') in self.primeNoBitsMax:
                ans += 1
        return ans

t = int(input())

for _ in range(t):
    l, r = map(int, input().split())
    S = Solution(l, r)
    print(S.primeNoSetBits())

            


