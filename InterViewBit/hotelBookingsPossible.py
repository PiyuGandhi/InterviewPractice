'''
A hotel manager has to process N advance bookings of rooms for the next season. His hotel has K rooms. Bookings contain an arrival date and a departure date. He wants to find out whether there are enough rooms in the hotel to satisfy the demand. Write a program that solves this problem in time O(N log N) .

Input:


First list for arrival time of booking.
Second list for departure time of booking.
Third is K which denotes count of rooms.

Output:

A boolean which tells whether its possible to make a booking. 
Return 0/1 for C programs.
O -> No there are not enough rooms for N booking.
1 -> Yes there are enough rooms for N booking.
Example :

Input : 
        Arrivals :   [1 3 5]
        Departures : [2 6 8]
        K : 1

Return : False / 0 

At day = 5, there are 2 guests in the hotel. But I have only one room. 
'''

class Solution:
    def hotel(self, A, D, k):
        A.sort()
        D.sort()
        tmp = D[0]
        d = 0
        cnt = 1
        for i in range(1,len(A)):
            if A[i] < tmp:
                cnt += 1
                if cnt > k : return False
            else:
                cnt += 1
                while tmp <= A[i] and d < len(D)-1 :
                    d += 1
                    tmp = D[d]
                    cnt -= 1
        return cnt <= k

S = Solution()
A = [1, 3, 5]
D = [2, 6, 8]
k = 1
print(S.hotel(A,D,k))