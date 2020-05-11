# -*- coding: utf-8 -*-
# @Author   : Administrator
# @DateTime : 2020/5/8 0:53
# @FileName : 100-相同的树.py
# @SoftWare : PyCharm

"""相同的树
Given two binary trees, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical and
the nodes have the same value.
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # 两个都空
        if not (p or q):
            return True
        # 只有一个空
        if not (p and q):
            return False
        # 两个非空，先判断是否根节点值相等，不相等直接返回False
        if p.val != q.val:
            return False
        return self.isSameTree(
            p.left, q.left) and self.isSameTree(
            p.right, q.right)
