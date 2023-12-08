""" 
判斷linked list是否為回文型態

Follow up: O(n) time and O(1) space?
"""
import time

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        reverse = None
        now_node = head
        fast_node = head.next
        
        # reverse half list
        while fast_node is not None:
            next_node = now_node.next
            now_node.next = reverse
            reverse = now_node
            now_node = next_node
            
            if fast_node is not None:
                if fast_node.next is None: # The number of nodes in the list is even 
                    break
                else:
                    fast_node = fast_node.next.next
                    if fast_node is None: # The number of nodes in the list is odd 
                        now_node = now_node.next
            else:
                reverse = reverse.next
                break
        
        # compare
        while reverse is not None:
            print(reverse.val, now_node.val)
            if reverse.val != now_node.val:
                return False
            reverse = reverse.next
            now_node = now_node.next
        
        return True

def test_case_run():
    print(Solution.isPalindrome(Solution, ListNode(1, ListNode(0, ListNode(1)))))
    return

start = time.perf_counter()
test_case_run()
end = time.perf_counter()
print("執行時間：%f 豪秒" % ((end - start)*1000))

"""
Constraints:
The number of nodes in the list is in the range [1, 10^5].
0 <= Node.val <= 9
"""

""" 
思路:
1. 用fast和normal speed node來找出list的中間
2. 在找中間的過程中順便把前半段list反轉
3. 找到中間後, 比較反轉後的前半段跟後半段數值是否相同
"""