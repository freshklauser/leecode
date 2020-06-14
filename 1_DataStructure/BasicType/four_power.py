# -*- coding: utf-8 -*-
# @Author   : Administrator
# @DateTime : 2020/6/14 20:33
# @FileName : four_power.py
# @SoftWare : PyCharm


class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num < 0:
            return 'false'
        is_power = num & (num - 1) == 0
        if not is_power:
            return 'false'
        else:
            stop = False
            while num and not stop:
                is_four = num >> 2 & 1
                if is_four:
                    stop = True
                num = num >> 2

            return stop


if __name__ == '__main__':
    num = 5
    res = Solution().isPowerOfFour(num)
    print(res)
