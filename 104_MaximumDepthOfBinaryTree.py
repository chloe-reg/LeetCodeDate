""" 
給予一個二元樹的root, 回傳這棵樹的最大深度
"""
import time

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return max(Solution.maxDepth(Solution, root.left),Solution.maxDepth(Solution, root.right))+1

def test_case_run():
    return

start = time.perf_counter()
test_case_run()
end = time.perf_counter()
print("執行時間：%f 豪秒" % ((end - start)*1000))

"""
Constraints:
The number of nodes in the tree is in the range [0, 10^4]
-100 <= Node.val <= 100
"""

""" 
思路:
1. 遍歷所有節點, 找出最大深度, return (max(左邊深, 右邊深) + 1)
"""