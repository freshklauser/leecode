# -*- coding: utf-8 -*-
# @Author   : Administrator
# @DateTime : 2020/6/16 22:13
# @FileName : 验证回文字符串2.py
# @SoftWare : PyCharm

"""
680. 验证回文字符串 Ⅱ
给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。
示例 1:
    输入: "aba"
    输出: True
思路：
    判断回文串显然是用双指针的，i从前往后遍历，j从后往前遍历。难点就是怎么去判断删除一个元素后的字符串是不是回文串
    s[i] != s[j]时，判断s[i:j] 或者 s[i+1:j+1]是否为回文串即可(切片前闭后开)
"""


class Solution:
    def validPalindrome(self, s):
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return self.is_palind(s[left:right]) \
                       or self.is_palind(s[left+1:right+1])
            else:
                left += 1
                right -= 1
        return True

    def is_palind(self, s):
        return s == s[::-1]


if __name__ == '__main__':
    s = "abdcba"
    res = Solution().validPalindrome(s)
    print(res)
