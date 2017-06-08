
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
#
# P.......A........H.......N
# ..A..P....L....S....I...I....G
# ....Y.........I........R
# And then read line by line: PAHNAPLSIIGYIR
# Write the code that will take a string and make this conversion given a number of rows:
#
# string convert(string text, int nRows);
# convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR"
# **Example 2 : **
# ABCD, 2 can be written as
#
# A....C
# ...B....D
# and hence the answer would be ACBD.


class Solution:
    # @param A : string
    # @param B : integer
    # @return a strings
    def convert(self, A, B):
        n = len(A)
        if n == 0:
            return ""
        if n <= B:
            return A
        if B <= 1:
            return A
        ret = ""
        for i in range(B):
            j = i
            if i == 0 or i == B - 1:
                step = 2*(B-1)
                while j < n:
                    ret += A[j]
                    j += step
            else:
                step1 = 2*(B-i-1)
                step2 = 2*i
                while j < n:
                    ret += A[j]
                    j += step1
                    if j < n:
                        ret += A[j]
                        j += step2
                    else:
                        break
        return ret