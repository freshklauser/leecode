# -*- coding: utf-8 -*-
# @Author   : Administrator
# @DateTime : 2020/5/7 23:21
# @FileName : 572-另一个树的子树.py
# @SoftWare : PyCharm

"""572. 另一个树的子树 Subtree of Another Tree
Given two non-empty binary trees s and t, check whether tree t has
exactly the same structure and node values with a subtree of s.
A subtree of s is a tree consists of a node in s and all of this node's
descendants. The tree s could also be considered as a subtree of itself.

思路：
    错误思路：s, t 先转化为列表，在判断 t 是否是 s 的子列表， 也可以转化为集合，直接用集合的方法来判断
    正确思路：递归
            三种条件： s == t, s.left == t, s.right == t
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def isSubtree(self, s: TreeNode, t: TreeNode):

        return self.is_same_tree(s, t) \
            or self.isSubtree(s.left, t) \
            or self.isSubtree(s.right, t)

    def is_same_tree(self, s, t):
        # 两个均为空
        if not (s or t):
            return False

        # 一个为空
        if not (s and t):
            return False

        # 两个非空, 先判断根节点值是否相同，不同直接返回False
        if s.val != t.val:
            return False

        return self.is_same_tree(s.left, t.left) \
            and self.is_same_tree(s.right, t.right)
