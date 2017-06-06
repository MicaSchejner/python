class Solution:
    # @param A : integer
    # @return an integer
    def numSetBits(self, A):
        self.num = A
        b = 0
        s = (bin(self.num)[2:])
        print s
        for i in s:
            if (i =='1'):
                b = b + 1
        return b
    def numSetBitss(self,A):
        return bin(A).count('1')

    def numSetBitsss(self, A):
        ret = 0
        while A != 0:
            if A & 1:
                ret += 1
            A = A >> 1
        return ret

num = 5
rtaaa = Solution()
rta = rtaaa.numSetBits(num)
rtaa = rtaaa.numSetBitss(num)
rtaaaa = rtaaa.numSetBitsss(num)
print rta
print rtaa
print rtaaaa