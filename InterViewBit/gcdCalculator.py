'''
Given 2 non negative integers m and n, find gcd(m, n)

GCD of 2 integers m and n is defined as the greatest integer g such that g is a divisor of both m and n.
Both m and n fit in a 32 bit signed integer.

Example

m : 6
n : 9

GCD(m, n) : 3 
 NOTE : DO NOT USE LIBRARY FUNCTIONS 
'''
class Solution:
    def gcd_cal(self, A, B):
        a,b = max(A,B), min(A,B)
        
        if b == 0:
            return a
        if a == b:
            return a

        return self.gcd_cal(a-b, b)

S = Solution()
print(S.gcd_cal(98,56))