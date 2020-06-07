# -*- coding: utf-8 -*-
# @Author   : Administrator
# @DateTime : 2020/5/11 23:17
# @FileName : 50-power_x_n.py
# @SoftWare : PyCharm

"""
Implement pow(x, n), which calculates x raised to the power n (xn).
Example 1:
Input: 2.00000, 10
Output: 1024.00000

example 2:
input: 2.10000, 3
output: 9.26100

example 3:
Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
思路：分治法 时间复杂度 log(n)
    如果n为偶数，则pow(x,n) = pow(x^2, n/2)；
    如果n为奇数，则pow(x,n) = x*pow(x, n-1)。
"""

import time


class Solution:
    def myPow(self, x, n):
        """
        x[-100.0, 100.0]   n[-2**31, 2**31-1]
        method to calculate x**n
        """
        if n == 0:
            return 1.0
        if n < 0:
            return 1 / self.helper(x, -n)
        return self.helper(x, n)

    def helper(self, x, n):
        if n == 1:
            return x
        # 奇数
        if n % 2 == 1:
            # n - 1 则为偶数，递归调用偶数的分治方法
            return self.helper(x, n - 1) * x
        return self.helper(x * x, n // 2)


if __name__ == '__main__':
    # x = 3
    # n = 3
    x = 0.8
    n = 21
    inst = Solution()
    t1 = time.clock()
    res = inst.myPow(x, n)
    print('Time Consumed: ', time.clock() - t1)
    print(res)

# Time Consumed:  6.8153639
