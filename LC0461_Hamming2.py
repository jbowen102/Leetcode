"""
The Hamming distance between two integers is the number of positions at which
the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 2^31.

Example:
    Input: x = 1, y = 4
    Output: 2

    Explanation:
    1   (0 0 0 1)
    4   (0 1 0 0)
           ↑   ↑
   The above arrows point to positions where the corresponding bits are different.

"""

class Solution:
    # def hammingDistance(self, x: int, y: int) -> int:
    def hammingDistance(self, x, y):
        x_bits = self.dec_to_binary(x)
        y_bits = self.dec_to_binary(y)

        print(x_bits)
        print(y_bits)
        count = 0

        for i in range(8):
            dif = abs(int(x_bits[i]) - int(y_bits[i]))
            count += dif

        return count

    def dec_to_binary(self, dec_num, output="00000000"):
        if dec_num >= 128:
            new_output = "1" + output[1:]
            return self.dec_to_binary(dec_num-128, new_output)
        elif dec_num >= 64:
            new_output = output[0] + "1" + output[2:]
            return self.dec_to_binary(dec_num-64, new_output)
        elif dec_num >= 32:
            new_output = output[:2] + "1" + output[3:]
            return self.dec_to_binary(dec_num-32, new_output)
        elif dec_num >= 16:
            new_output = output[:3] + "1" + output[4:]
            return self.dec_to_binary(dec_num-16, new_output)
        elif dec_num >= 8:
            new_output = output[:4] + "1" + output[5:]
            return self.dec_to_binary(dec_num-8, new_output)
        elif dec_num >= 4:
            new_output = output[:5] + "1" + output[6:]
            return self.dec_to_binary(dec_num-4, new_output)
        elif dec_num >= 2:
            new_output = output[:6] + "1" + output[7:]
            return self.dec_to_binary(dec_num-2, new_output)
        elif dec_num >= 1:
            new_output = output[:7] + "1"
            return self.dec_to_binary(dec_num-1, new_output)
        else:
            return output

# test
mysol = Solution()
print(mysol.hammingDistance(1, 4))
print(mysol.hammingDistance(1, 1))
print(mysol.hammingDistance(1, 0))
print(mysol.hammingDistance(1, 10))
print(mysol.hammingDistance(1, 231))



# print(mysol.dec_to_binary(255))
# print(mysol.dec_to_binary(129))
# print(mysol.dec_to_binary(128))
# print(mysol.dec_to_binary(64))
# print(mysol.dec_to_binary(33))
# print(mysol.dec_to_binary(32))
# print(mysol.dec_to_binary(16))
# print(mysol.dec_to_binary(9))
# print(mysol.dec_to_binary(4))
# print(mysol.dec_to_binary(1))
# print(mysol.dec_to_binary(0))



# Failed on inputs:
# x = 1577962638
# y = 1727613287
