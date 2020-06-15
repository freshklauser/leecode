# -*- coding: utf-8 -*-
# @Author   : Administrator
# @DateTime : 2020/6/15 6:14
# @FileName : reverse_string.py
# @SoftWare : PyCharm


def reverse_word(s):
    alist = s.split(' ')
    res = []
    res = [item.strip() for item in alist[::-1] if item]
    return ' '.join(res)


def reverse_word_cursor(s):
    s = s.strip()
    n = len(s)
    i = j = n - 1
    res = []
    while i >= 0:

        # 这里 i=0时要跳出，防止遍历到s[-1],s[-1]!=0,会继续i-=1
        while s[i] != ' ' and i >= 0:
            i -= 1
        res.append(s[i + 1: j + 1])

        while s[i] == ' ':
            i -= 1
        j = i

    return ' '.join(res)


if __name__ == '__main__':
    s = "  hello world!  "
    res = reverse_word_cursor(s)
    print(res)
