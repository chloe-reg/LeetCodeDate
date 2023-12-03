""" 
給予一個二元樹的根root, 回傳inorder traversal的遍歷值
"""
import time

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode) -> list[int]:
        return self.inorderTraversal(Solution, root.left) + [root.val] + self.inorderTraversal(Solution, root.right) if root else []

def test_case_run():
    return

start = time.perf_counter()
test_case_run()
end = time.perf_counter()
print("執行時間：%f 豪秒" % ((end - start)*1000))

"""
Constraints:

"""

""" 
思路:
1. inorder traversal是中序遍歷法, 相當於由二元樹的最左邊遍歷到最右邊
2. 用遞迴的方式, 根據 left leaf + root + right leaf 來排序
"""