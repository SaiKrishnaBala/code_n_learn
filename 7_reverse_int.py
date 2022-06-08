# Reverse Integer
# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).


class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return x
        if x > 0:
            sign = 1
        else:
            sign = -1
            x = -1 * x
        y = 0
        while x > 0:
            rem = x%10
            y = y*10 + rem
            x = int(x/10)
        y = sign * y
        if y > pow(2, 31)-1 or y < pow(-2, 31):
            return 0
        return y
