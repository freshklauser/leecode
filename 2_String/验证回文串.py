# -*- coding: utf-8 -*-
# @Author   : Administrator
# @DateTime : 2020/6/16 22:11
# @FileName : 验证回文串.py
# @SoftWare : PyCharm

"""
125. 验证回文串
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
说明：本题中，我们将空字符串定义为有效的回文串。
示例 1
    输入: "A man, a plan, a canal: Panama"
    输出: true
思路：双指针法 (不知道可不可以直接用 s = s[::-1])
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        s = s.lower()
        i = 0
        j = len(s) - 1
        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1
            if s[i] != s[j]:
                return False
            else:
                i += 1
                j -= 1
        return True
