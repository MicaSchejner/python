# Given an index k, return the kth row of the Pascal s triangle.
#
# Pascal s triangle : To generate A[C] in row R, sum up A[C] and A[C-1] from previous row R - 1.
#
# Example:
#
# Input : k = 3
#
# Return : [1,3,3,1]
# NOTE : k is 0 based. k = 0, corresponds to the row [1].
# Note:Could you optimize your algorithm to use only O(k) extra space?



class Solution:
    # @param A : integer
    # @return a list of integers
    def getRow(self, A):
        A += 1
        ret = []
        if A == 0:
            return ret
        ret = [[1]]
        for i in range(2,A+1):
            ret.append([0]*i)
            ret[i-1][0] = 1
            ret[i-1][-1] = 1
            for j in range(1,i-1):
                ret[i-1][j] = ret[i-2][j-1]+ret[i-2][j]
        return ret[-1]


rta =Solution()
print rta.getRow(5)