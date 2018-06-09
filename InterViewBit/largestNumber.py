'''
Given a list of non negative integers, arrange them such that they form the largest number.

For example:

Given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an integer.
'''

class Solution:
    def cmp(self, a,b):
        ab = str(a) + str(b)
        ba = str(b) + str(a)
        return (int(ba) - int(ab))
    def large(self, A):
        import functools
        A = sorted(A, key=functools.cmp_to_key(self.cmp))
        return "".join([str(i) for i in A])

S = Solution()
A = [54, 546, 548, 60]
print(S.large(A))