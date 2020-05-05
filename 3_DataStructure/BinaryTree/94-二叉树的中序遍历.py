# -*- coding: utf-8 -*-
# @Author   : Administrator
# @DateTime : 2020/5/5 14:29
# @FileName : 94-二叉树的中序遍历.py
# @SoftWare : PyCharm

"""
Given a binary tree, return the inorder traversal of its nodes' values.
Example:二叉树的中序遍历
    Input: [1,null,2,3]
       1
        \
         2
        /
       3

    Output: [1,3,2]
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.res = []
        self.stack = []

    def inorder_traversal(self, root):
        if not root:
            return []
        self.inorderTraversal(root.left)
        self.res.append(root.val)
        self.inorderTraversal(root.right)
        return self.res

    def inorder_traveral_iter(self, root):
        """ 迭代法实现中序遍历 """
        if not root:
            return []

        cursor = root
        while cursor or self.stack:
            while cursor:
                # node 入栈
                self.stack.append(cursor)
                cursor = cursor.left

            # node 出栈
            node = self.stack.pop()
            self.res.append(node.val)
            cursor = node.right

        return self.res


