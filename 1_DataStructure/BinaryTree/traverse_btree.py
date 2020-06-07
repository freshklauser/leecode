# -*- coding: utf-8 -*-
# @Author   : Administrator
# @DateTime : 2020/5/5 13:17
# @FileName : traverse_btree.py
# @SoftWare : PyCharm

"""
节点递归相当于嵌套循环遍历
"""

import random
from binarytree import bst
from binarytree import tree

random.seed(4)
# print(help(bst))
my_tree = bst(4)

# print(len(my_tree))
# print(my_tree)
# print(my_tree.left)
# print(my_tree.left.left)
#
# # values: 子数的所有value
# print(my_tree.right.values)
# # value: 当前节点的value
# print(my_tree.right.value)
# print(my_tree.leaves)


res_pre = []
res_mid = []
res_post = []


# 前序遍历
def traverse_pre(root):
    if root:
        res_pre.append(root.value)
        traverse_pre(root.left)
        traverse_pre(root.right)
    return


# 中序遍历
def inorder_traverse(root):
    if root:
        inorder_traverse(root.left)
        res_mid.append(root.value)
        inorder_traverse(root.right)
    return


# 后序遍历
def traverse_post(root):
    if root:
        traverse_post(root.left)
        traverse_post(root.right)
        res_post.append(root.value)
    return


print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
print(my_tree)
traverse_pre(my_tree)
inorder_traverse(my_tree)
traverse_post(my_tree)
print('pre :', res_pre)
print('mid :', res_mid)
print('post:', res_post)

"""
    __8_______________
   /                  \
  5                ____18_________
 / \              /               \
1   6        ____16            ____25___
            /      \          /         \
          _13       17      _21         _28
         /   \             /   \       /   \
        10    14          19    22    26    30

pre : [8, 5, 1, 6, 18, 16, 13, 10, 14, 17, 25, 21, 19, 22, 28, 26, 30]
mid : [1, 5, 6, 8, 10, 13, 14, 16, 17, 18, 19, 21, 22, 25, 26, 28, 30]
post: [1, 6, 5, 10, 14, 13, 17, 16, 19, 22, 21, 26, 30, 28, 25, 18, 8]
"""