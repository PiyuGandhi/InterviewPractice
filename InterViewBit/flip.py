'''
You are given a binary string(i.e. with characters 0 and 1) S consisting of characters S1, S2, …, SN. In a single operation, you can choose two indices L and R such that 1 ≤ L ≤ R ≤ N and flip the characters SL, SL+1, …, SR. By flipping, we mean change character 0 to 1 and vice-versa.

Your aim is to perform ATMOST one operation such that in final string number of 1s is maximised. If you don’t want to perform the operation, return an empty array. Else, return an array consisting of two elements denoting L and R. If there are multiple solutions, return the lexicographically smallest pair of L and R.

Notes:

Pair (a, b) is lexicographically smaller than pair (c, d) if a < c or, if a == c and b < d.
For example,

S = 010

Pair of [L, R] | Final string
_______________|_____________
[1 1]          | 110
[1 2]          | 100
[1 3]          | 101
[2 2]          | 000
[2 3]          | 001

We see that two pairs [1, 1] and [1, 3] give same number of 1s in final string. So, we return [1, 1].
Another example,

If S = 111

No operation can give us more than three 1s in final string. So, we return empty array [].
'''

class Solution:
    def flip(self, A):
        if A.count('1') == len(A): return []
        gain = [0]*len(A)
        # Kadane's algorithm
        for i in range(0,len(A)):
            if A[i] == '1': gain[i] = -1
            else: gain[i] = 1
        currSum = 0
        maxSum = 0
        l,r = 0,0
        currL = 0
        for i in range(0,len(A)):
            if currSum + gain[i] < 0:
                currSum = 0
                currL = i + 1
            else:
                currSum += gain[i]
            if currSum > maxSum: 
                maxSum = currSum
                l = currL
                r = i
        return [l+1,r+1]


S = Solution()
print("Regular Case:- ",S.flip('101'))
print("Tricky Cases:- ",S.flip('11001100110011'))
print("Corner case", S.flip('0'))