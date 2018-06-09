'''
Given a non-negative number represented as an array of digits,
add 1 to the number ( increment the number represented by the digits ). The digits are stored 
such that the most significant digit is first element of array.

Examples :

Input : [1, 2, 4]
Output : [1, 2, 5]

Input : [9, 9, 9]
Output : [1, 0, 0, 0]

'''
class Solution:
    def add_one(self,A):
        n = ''.join([str(x) for x in A])
        n = int(n)
        ans = n+1
        ans = str(ans)
        return list(ans)
        
            
S = Solution()
A = [1,2,3]
print(S.add_one(A))
            