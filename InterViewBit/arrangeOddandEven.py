'''
Given an array of size n containing equal number of odd and even 
numbers. The problem is to arrange the numbers in such a way that 
all the even numbers get the even index and odd numbers get the 
odd index. Required auxiliary space is O(1).

Examples:

Input : arr[] = {3, 6, 12, 1, 5, 8}
Output : 8 5 12 1 6 3 

Input : arr[] = {10, 9, 7, 18, 13, 19, 4, 20, 21, 14}
Output : 10 9 14 21 20 19 4 13 18 7

'''
class Solution:

    def arrangeOddandEven(self, A):
        i = 0
        j = len(A) - 1

        while True:
            
            while i < len(A) and (A[i] + i)%2 == 0:
                i += 1
            while j >= 0 and (A[j] + j)%2 == 0:
                j -= 1
            if i >= j:
                return A
            A[i], A[j] = A[j], A[i]

if __name__ == "__main__":
    A = [ 3, 6, 12, 1, 5, 8 ]
    S = Solution()
    print(S.arrangeOddandEven(A))