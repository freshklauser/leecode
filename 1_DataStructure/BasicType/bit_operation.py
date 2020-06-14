# -*- coding: utf-8 -*-
# @Author   : Administrator
# @DateTime : 2020/6/14 8:15
# @FileName : bit_operation.py
# @SoftWare : PyCharm


def to_hex_via_bit(num):
    """
    405. 数字转换为十六进制数
    给定一个整数，编写一个算法将这个数转换为十六进制数。对于负整数，我们通常使用 补码运算 方法。
    注意:
        十六进制中所有字母(a-f)都必须是小写。
        十六进制字符串中不能包含多余的前导零。如果要转化的数为0，那么以单个字符'0'来表示；对于其他情况，十六进制字符串中的第一个字符将不会是0字符。
        给定的数确保在32位有符号整数范围内。
        不能使用任何由库提供的将数字直接转换或格式化为十六进制的方法。
    负数的表示： 补码形式 (num < 0)
        num = num & 0xffffffff   ---> num转化为正数再按正数方法实现转化  (32位：0xffffffff, 16位：0xffff)
    位运算实现正数的16进制转换（遍历，低4位转化，右移4位继续遍历，每次转化后字符串拼接到16进制的相对高位）：
        (1) 二进制的低4位和十六进制： 0b1111 = 0xf, 取二进制低四位： num & 0b1111
            可以通过 num & 0b1111 得到num二进制的低4位, 根据 十六进制掩码映射将低4位转化位16进制，拼接转化后的字符串
        (2) num 右移4位，继续(1)的进制转化过程
    """
    if num == 0:
        return '0'
    if num < 0:
        num &= 0xffffffff
    hex_mapper = '0123456789abcdef'
    target = ''
    while num:
        mask = num & 0b1111             # 取 num 的低4位
        hexer = hex_mapper[mask]        # 映射二进制的低4位为16进制
        target = hexer + target         # 高位拼接
        num = num >> 4                  # 右移，为下一次遍历取低4位做准备
    return target


def bin_count_one(n):
    """
    191. 位1的个数
    题目：无符号整数，返回其二进制表达式中数字位数为 ‘1’ 的个数
          即 hamming weight
    """
    cnt = 0
    while n:
        cnt += n & 1
        n = n >> 1
    return cnt


def hamming_distance(x, y):
    """
    461. 汉明距离：两个整数之间的汉明距离是则两个数对应二进制不同的位置的数目
    示例：
        输入：x = 1, y = 4
        输出：2
    """
    cnt = 0
    tmp = x ^ y
    while tmp:
        cnt += tmp & 1
        tmp = tmp >> 1
    return cnt


def single_number(nums_arr):
    """
    136. 只出现一次的数字
        给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。
        找出那个只出现了一次的元素。
    思路：
        一个数与其自身异或结果位0，与1异或结果为这个数
    """
    res = 0
    for num in nums_arr:
        res ^= num
    return res


def reverse_bits(bit_n):
    """
    190. 题目：颠倒给定的 32 位无符号整数的二进制位。
    输入: 00000010100101000001111010011100
    输出: 00111001011110000010100101000000
    解释: 输入的二进制串 00000010100101000001111010011100 表示无符号整数 43261596，
          因此返回 964176192，其二进制表示形式为 00111001011110000010100101000000。
    注意：
        1）索引从0开始，32位则索引最大值power为31；
        2）运算符优先级：<< ,+=, & (高-->低)
    思路： 索引i,颠倒后的索引为 power-i   (索引从0开始)
    """
    power = 31
    res = 0
    while bit_n:
        res += (bit_n & 1) << power
        bit_n = bit_n >> 1
        power -= 1
    return res


def alternate_bins(num):
    """
    693. 交替位二进制数。判断num是否为交替位二进制数
    特点：
                     10101
        n>>1         01010
        XOR          11111
        xor+1       100000
        XOR & XOR+1 000000
    """
    tmp = num ^ (num >> 1)
    return tmp & (tmp + 1) == 0


def is_four_power(num):
    """
    342. 4的幂
    给定一个整数 (32 位有符号整数)，请编写一个函数来判断它是否是 4 的幂次方。
    示例 1:
        输入: 16
        输出: True
    思路：
        （1）判断是否为2的幂
        （2）若为2的幂，遍历num（每次右移2位），若 num >> 2 & 1 == 1，则说明是4的幂
        （3）负数和1（4**0）单独讨论
    TIPS(推荐该优化方法):
        步骤(2)也可以根据 `一个数的N次方-1总能除尽比这个数小1的数` 来判断
        if is_power:
            return (num - 1) % 3 == 0
    """
    if num < 0:
        return False
    if num == 1:
        return True
    is_power = num & (num - 1) == 0
    is_four = False
    if is_power:
        while num and not is_four:
            is_four = bool(num >> 2 & 1)
            if not is_four:
                num = num >> 2
    return is_four


def bin_watch(n):
    """
    401. 二进制手表
    """
    res = []
    for h in range(12):
        for m in range(60):
            if bin(h).count('1') + bin(m).count('1') == n:
                # if m < 10:
                #     m = '0' + str(m)
                strings = '{}:{:0>2d}'.format(h, m)
                res.append(strings)
    return res


def count_prime_set_bits(low, high):
    """
    762. 二进制表示中质数个计算置位
    给定两个整数 L 和 R ，找到闭区间 [L, R] 范围内，
    计算置位位数为质数的整数个数。
    """
    res = 0
    for num in range(low, high + 1, 1):
        cnt = 0
        while num:
            cnt += num & 1
            num = num >> 1
        if is_primes(cnt):
            res += 1
    return res


def is_primes(num):
    """
    判断一个数是不是素数（质数）：True(是)， False(否)
    """
    if num <= 1:
        return False
    if num == 2:
        return True
    tag = 2
    prime = True
    while tag < num and prime:
        if num % tag == 0:
            prime = False
        tag += 1
    return prime


if __name__ == '__main__':
    res = hamming_distance(2, 4)
    print('hamming_distance: ', res)

    n = 52
    res = bin_count_one(n)
    print('bin_count_one: ', res, bin(n))

    n = 0b00000010100101000001111010011100
    res = reverse_bits(n)
    print('reverse_bits: ', res, bin(res), '|| n: ', n, bin(n))

    res = bin_watch(3)
    print('bin_watch: ', res)

    res = count_prime_set_bits(842, 888)
    print('count_prime_set_bits: ', res)

    res = single_number([4, 1, 2, 1, 2])
    print('single_number: ', res)

    res = is_four_power(16)
    print('is_four_power: ', res)      # True

    res = to_hex_via_bit(-75)
    print('to_hex_via_bit: ', res)      # ffffffb5
