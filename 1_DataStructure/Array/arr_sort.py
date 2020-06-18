# -*- coding: utf-8 -*-
# @Author   : Administrator
# @DateTime : 2020/6/14 12:41
# @FileName : arr_sort.py
# @SoftWare : PyCharm

"""
1356. 根据数字二进制下 1 的数目排序
给你一个整数数组 arr 。请你将数组中的元素按照其二进制表示中数字 1 的数目升序排序。
如果存在多个数字二进制中 1 的数目相同，则必须将它们按照数值大小升序排列。
请你返回排序后的数组。
"""

class Solution:
    def sortByBits_simple(self, arr):
        return sorted(arr, key=lambda x: (bin(x).count('1'), x))

    def sortByBits(self, arr):
        # 升序排列arr 原址修改, 计算count, 以count为标准对排序后的arr再进行升序排列
        arr.sort()

        cnt_dict = {}
        for num in arr:
            cnt = 0
            flag = num
            while flag:
                cnt += (flag & 1)
                flag = flag >> 1
            if cnt not in cnt_dict:
                cnt_dict[cnt] = []
            cnt_dict[cnt].append(num)

        output = sorted(cnt_dict.items(), key=lambda x: x[0])
        res = []
        for item in output:
            res.extend(item[1])
        return res


    def sortByBits_1(self, arr):
        # 升序排列arr 原址修改, 计算count, 以count为标准对排序后的arr再进行升序排列
        arr.sort()

        cnt_list = []
        for num in arr:
            cnt = 0
            while num:
                cnt += (num & 1)
                num = num >> 1
            cnt_list.append(cnt)
        zipped = list(sorted(zip(arr, cnt_list), key=lambda x: x[1]))
        res = list(zip(*zipped))
        return res[0]


if __name__ == '__main__':
    arr = [9, 7, 8, 4, 2, 6, 3, 5, 9, 1, 25, 0]
    res = Solution().sortByBits(arr)
    print(res)

    res = Solution().sortByBits_1(arr)
    print(res)

    res = Solution().sortByBits_simple(arr)
    print(res)
