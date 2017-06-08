# Remove Duplicates from Sorted Array
#
# Given a sorted array, remove the duplicates in place such that each element can appear atmost twice and return the new length.
#
# Do not allocate extra space for another array, you must do this in place with constant memory.
#
# Note that even though we want you to return the new length, make sure to change the original array as well in place
#
# For example,
# Given input array A = [1,1,1,2],
#
# Your function should return length = 3, and A is now [1,1,2]
#
# .

class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates2(self, A):
        change = True
        count = 0
        for i in xrange(0, len(A) - 1):
            if A[i] == A[i + 1]:
                if change == True:
                    A[(i + 1) - count] = A[i + 1]
                    change = False
                elif change == False:
                    count += 1
            else:
                A[(i + 1) - count] = A[i + 1]
                change = True
        newLength = len(A) - count
        A = A[:newLength]
        return A

    def removeDuplicates(self, A):
        n = len(A)
        k = 0
        for i in range(2, n):
            if A[i] == A[i - k - 1] and A[i] == A[i - k - 2]:
                if i >= 2 and A[i - 2] == A[i]:
                    k += 1
            elif k > 0:
                A[i - k] = A[i]
        A = A[:n - k]
        return n - k

lista = [1,1,1,2,2,2]
rta = Solution()
print rta.removeDuplicates(lista)

