
# Implement pow(x, n), which calculates x raised to the power n (i.e., xn).


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1
        elif n < 0:
            x = 1/x
            temp = self.myPow(x,  -1 * int(n/2))
            if n%2:
                return temp * temp * x
            else:
                return temp * temp
        else:
            temp = self.myPow(x,  int(n/2))
            if n%2:
                return temp * temp * x
            else:
                return temp * temp
