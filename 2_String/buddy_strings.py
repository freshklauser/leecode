# -*- coding: utf-8 -*-
# @Author   : Administrator
# @DateTime : 2020/6/18 21:18
# @FileName : buddy_strings.py
# @SoftWare : PyCharm

"""
859. 亲密字符串
给定两个由小写字母构成的字符串 A 和 B ，只要我们可以通过交换 A 中的两个字母得到
与 B 相等的结果，就返回 true ；否则返回 false 。
    输入： A = "aaaaaaabc", B = "aaaaaaacb"
    输出： true

思路：只有两种情况返回True
    1. A 和 B 长度不同，返回 False
    2. A == B, 且字符串中存在重复字符 True, else False
    3. A != B, A与B只有两个字符不同，且存在A[i]==B[j] and A[j]==B[i] True, else False

"""

from collections import Counter


def buddy_strings(s1, s2):
    sim = False
    if len(s1) != len(s2):
        return False

    if s1 == s2:
        count = Counter(s1)
        for k, v in count.items():
            if v > 1:
                sim = True
    else:
        ds1 = []
        ds2 = []
        cnt = 0
        for i, j in zip(s1, s2):
            if i != j:
                ds1.append(i)
                ds2.append(j)
                cnt += 1
        if cnt == 2 and ds1[0] == ds2[1] and ds1[1] == ds2[0]:
            sim = True

    return sim



