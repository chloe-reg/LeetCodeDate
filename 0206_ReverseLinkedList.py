""" 

"""
import time

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        reverse = None
        now_node = head

        while now_node is not None:
            next_node = now_node.next
            now_node.next = reverse
            reverse = now_node
            now_node = next_node
        
        return reverse

def test_case_run():
    return

start = time.perf_counter()
test_case_run()
end = time.perf_counter()
print("執行時間：%f 豪秒" % ((end - start)*1000))

"""
Constraints:
The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
"""

""" 
思路:
1. 從head node頭反過來串到尾端, 回傳最後的node, 即為反向過後的head
"""