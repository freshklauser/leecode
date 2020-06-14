# -*- coding: utf-8 -*-
# @Author   : Administrator
# @DateTime : 2020/6/14 22:14
# @FileName : complement_tohex.py
# @SoftWare : PyCharm

"""
405. 数字转换为十六进制数
给定一个整数，编写一个算法将这个数转换为十六进制数。对于负整数，我们通常使用 补码运算 方法。
注意:
    十六进制中所有字母(a-f)都必须是小写。
    十六进制字符串中不能包含多余的前导零。如果要转化的数为0，那么以单个字符'0'来表示；对于其他情况，十六进制字符串中的第一个字符将不会是0字符。
    给定的数确保在32位有符号整数范围内。
    不能使用任何由库提供的将数字直接转换或格式化为十六进制的方法。
负数的表示： 补码形式 (num < 0)
    num = num & 0xffffff   ---> num转化为正数
位运算实现正数的16进制转换（遍历，低4位转化，右移4位继续遍历，每次转化后字符串拼接到16进制的相对高位）：
    (1) 二进制的低4位和十六进制： 0b1111 = 0xf
        可以通过 num & 0b1111 得到num二进制的低4位, 根据 十六进制掩码映射将低4位转化位16进制，拼接转化后的字符串
    (2) num 右移4位，继续(1)的进制转化过程
"""


def to_hex_via_bit(self, num):
    if num == 0:
        return '0'
    # 负数的化先以补码形式转化为正数
    if num < 0:
        num &= 0xffffffff
    # 对正数的十六进制转换: 0b1111 = 0xf，低4位转化，相对高位拼接16进制字符串
    hex_mapper = '0123456789abcdef'
    target = ''
    while num:
        mask = num & 0b1111             # 取 num 的低4位
        hexer = hex_mapper[mask]        # 映射二进制的低4位为16进制
        target = hexer + target         # 高位拼接
        num = num >> 4                  # 右移，为下一次遍历取低4位做准备
    return target


if __name__ == '__main__':
    res = to_hex_via_bit(-77)
    print(res, hex(77))
