# -*- coding: utf-8 -*-
# @Author   : Administrator
# @DateTime : 2020/6/13 22:37
# @FileName : bin_add.py
# @SoftWare : PyCharm


"""
不使用 +, -, 实现整数 a+b
理解：
二进制加法：从以下可以看出，二进制加法不含进位部分就是异或^
    0 + 0 = 0
    0 + 1 = 1
    1 + 0 = 1
    1 + 1 = 0（进位 1）
a ^ b 得到了一个无进位加法结果
a & b 得到进位信息，但需左移1位才在高位

步骤：
    a + b 的问题拆分为 (a 和 b 的无进位结果) + (a 和 b 的进位结果)
    无进位加法使用异或运算计算得出
    进位结果使用与运算和移位运算计算得出
    循环此过程，直到进位为 0

"""


def sum_by_bin(a, b):
    a &= 0xFFFFFFFF
    b &= 0xFFFFFFFF
    while b:
        carry = a & b
        a = a ^ b
        b = carry << 1 & 0xFFFFFFFF
        print(a, b)
    return a if a < 0x80000000 else ~(a ^ 0xFFFFFFFF)


res = sum_by_bin(10, -2)
print(res)


