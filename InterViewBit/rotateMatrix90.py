'''
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

You need to do this in place.

Note that if you end up using an additional array, you will only receive partial score.

Example:

If the array is

[
    [1, 2],
    [3, 4]
]
Then the rotated array becomes:

[
    [3, 1],
    [4, 2]
]
'''
class Solution:
    def rotateMatrix(self, A):
        
        # Transposing matrix
        A = list(map(list, zip(*A)))
        # Reverse columns
        mid_point = int(len(A[0])/2)
        for i in range(0, len(A)):
            j = 0
            k = len(A[0]) - 1
            while j < mid_point and k >= mid_point:
                A[i][j], A[i][k] = A[i][k], A[i][j]
                j += 1
                k -= 1
        return A


S = Solution()
A = [[1,2,3,4], 
     [5,6,7,8], 
     [9,10,11,12], 
     [13,14,15,16]]
B = [[1,2,3],
     [4,5,6],
     [7,8,9]]
print(S.rotateMatrix(A))