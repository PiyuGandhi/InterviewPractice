'''
Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity.

Example :

n = 5
n! = 120 
Number of trailing zeros = 1
So, return 1
'''
class Solution:
    def trailingZeros(self, A):
        cnt = 0
        i = 5
        while A >= i:
            cnt += int(A/i)
            i *= 5
        return cnt

S = Solution()
print(S.trailingZeros(100))