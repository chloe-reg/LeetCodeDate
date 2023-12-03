""" 
給予一個嚴格升序的整數陣列nums, 將其轉換成平衡二元樹
"""
import time

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode:
        if len(nums) == 0:
            return None
        
        mid = len(nums) // 2
        
        return TreeNode(
            val=nums[mid], 
            left=Solution.sortedArrayToBST(Solution, nums[:mid]), 
            right=Solution.sortedArrayToBST(Solution, nums[mid+1:])
            )

def test_case_run():
    nums = [-10,-3,0,5,9]
    print(len(nums)//2, nums[len(nums)//2], nums[:len(nums)//2], nums[len(nums)//2+1:])
    return

start = time.perf_counter()
test_case_run()
end = time.perf_counter()
print("執行時間：%f 豪秒" % ((end - start)*1000))

"""
Constraints:
1 <= nums.length <= 10^4
-10^4 <= nums[i] <= 10^4
nums is sorted in a strictly increasing order.
"""

""" 
思路:
1. 將list切成兩半, 取中間值作為當下的Node val, 左半跟右半分別遞迴建立子樹
"""