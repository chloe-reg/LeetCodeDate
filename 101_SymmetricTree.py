""" 
給予一個二元樹的root, 判斷這棵樹是否左右對稱
"""
import time

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return False
        return Solution.isMirror(Solution, root.left, root.right)
        
    def isMirror(self, left: TreeNode, right: TreeNode) -> bool:
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        
        return (left.val == right.val) and Solution.isMirror(Solution, left.left,right.right) and Solution.isMirror(Solution, left.right,right.left)

def test_case_run():
    return

start = time.perf_counter()
test_case_run()
end = time.perf_counter()
print("執行時間：%f 豪秒" % ((end - start)*1000))

"""
Constraints:
The number of nodes in the tree is in the range [1, 1000].
-100 <= Node.val <= 100

Follow up: Could you solve it both recursively and iteratively?
"""

""" 
思路:
1. 將樹先由root分為left tree跟right tree
2. left tree由左向右, right tree由右向左
3. 如果左右都是None, 則代表左右相同, 只有一邊是None, 代表非鏡像
"""