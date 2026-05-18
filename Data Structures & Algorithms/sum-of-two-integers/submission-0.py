class Solution:
    def getSum(self, a: int, b: int) -> int:
        # convert both to binary, then go through each digit, seeing if you can + carry over (have a var for a carry over digit)
        #
        # we can actually do this by first realizing that to get the initial digit of each place, we can just XOR the entire
        # number
        # then, to get the carries, we just & the entire thing and << by 1 to create the "carried" over number
        # We then loop through this until our carry is 0, meaning we can stop now.
        # since in python we deal with unlimited size integers, we must mask it to clamp it to 32 bits
        # additionally, we must calculate at the end whether or not it is a negative number to convert it correctly
        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF
        # let's let b = our carry, and a = our non-carry sums
        while b != 0:
            temp = (a & b) << 1
            a = (a ^ b) & mask
            b = temp & mask
        return a if a <= max_int else ~(a ^ mask)
