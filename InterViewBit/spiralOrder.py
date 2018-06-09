'''
Given a matrix of m * n elements (m rows, n columns), 
return all elements of the matrix in spiral order.

Example:

Given the following matrix:

[
    [ 1, 2, 3 ],
    [ 4, 5, 6 ],
    [ 7, 8, 9 ]
]
You should return

[1, 2, 3, 6, 9, 8, 7, 4, 5]

'''
class Solution:
    def spiralOrder(self, A):
        n,m  = len(A), len(A[0])
        t,l,b,r = 0, 0, n, m
        d = 0
        ans = []
        while t<b and l<r:
            if d == 0:
                for i in range(l,r):
                    ans.append(A[t][i])
                t += 1
                d = 1
                continue
            elif d == 1:        
                for i in range(t,b):
                    ans.append(A[i][r-1])
                r -= 1
                d = 2
                continue
            elif d == 2:
                for i in reversed(range(l,r)):
                    ans.append(A[b-1][i])
                b -= 1
                d = 3
                continue
            elif d == 3:
                for i in reversed(range(t,b)):
                    ans.append(A[i][l])
                l += 1
                d = 0
        return ans
                
	    
	    
S = Solution()

arr = [[1,2,3], [4,5,6]] 

print(S.spiralOrder(arr))