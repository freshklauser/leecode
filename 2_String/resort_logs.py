# -*- coding: utf-8 -*-
# @Author   : Administrator
# @DateTime : 2020/6/18 22:47
# @FileName : resort_logs.py
# @SoftWare : PyCharm


class Solution:
    def reorderLogFiles(self, logs):
        num_log = []
        str_log = []
        for log in logs:
            if log[-1].isdigit():
                num_log.append(log)
            if log[-1].isalpha():
                str_log.append(log.split(' ', 1))
        str_log_list = list(sorted(str_log, key=lambda x: (x[1], x[0])))
        str_log_sorted = [' '.join(item) for item in str_log_list]
        # return sort_str_log + num_log
        print(str_log_sorted)
        output = str_log_sorted + num_log
        return output


if __name__ == '__main__':
    s = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
    res = Solution().reorderLogFiles(s)
    print(res)
