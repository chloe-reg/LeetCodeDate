""" 
建構一個表是二元樹的字串, 用不到的括號要去除
例如    
        1(2(4)())(3()())   省略括號後 = 1(2(4))(3)
        1(2()(4))(3()())   省略括號後 = 1(2()(4))(3)
"""
import time

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def tree2str(self, root: TreeNode) -> str:
        if root is None:
            return ""
        
        if root.right is None:
            right_tree = ""
            if root.left is None:
                left_tree = ""
            else:
                left_tree = "(" + self.tree2str(self, root.left) + ")"
        else:
            left_tree = "(" + self.tree2str(self, root.left) + ")"
            right_tree = "(" + self.tree2str(self, root.right) + ")"

        result = str(root.val) + left_tree + right_tree
        
        return result

def test_case_run():
    return

start = time.perf_counter()
test_case_run()
end = time.perf_counter()
print("執行時間：%f 豪秒" % ((end - start)*1000))

"""
Constraints:
The number of nodes in the tree is in the range [1, 10^4].
-1000 <= Node.val <= 1000
"""

""" 
思路:
1. 用遞迴的方式處理左子樹跟右子樹, 再將結果串起來
"""