""" 
合併兩個已排序的Linked list
"""
import time

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        if list1 is None and list2 is None:
            return None
        
        result_node = ListNode()
        now_node = None
        
        while list1 is not None or list2 is not None:
            if now_node is None:
                now_node = result_node
            else:
                now_node.next = ListNode()
                now_node = now_node.next
                   
            if list1 is None:
                now_node.val = list2.val
                list2 = list2.next
            elif list2 is None:
                now_node.val = list1.val
                list1 = list1.next
            else:
                if list1.val <= list2.val:
                    now_node.val = list1.val
                    list1 = list1.next
                else:
                    now_node.val = list2.val
                    list2 = list2.next
        return result_node
    
    def mergeTwoLists2(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy_node = ListNode()
        now_node = dummy_node
        
        while list1 and list2:
            if list1.val <= list2.val:
                now_node.next = list1
                list1 = list1.next
            else:
                now_node.next = list2
                list2 = list2.next
            
            now_node = now_node.next
        
        if list1 or list2:
            now_node.next = list1 if list1 else list2
        
        return dummy_node.next

""" 
思路:
1. 已知必為升序排列
2. 如果兩個list都是none, 回傳none
3. 一個一個node取出比較, 比較完前往下一個node, 直到none
4. 只要有其中一個list不是none, 就代表還有下一個值, 創建一個新的node在result後面
5. 將比較完的值存進當下的result node中
6. 最後回傳result node head O(m+n)

1. 如果不一直創立新node, 直接用原先的node重新串接, 只創立一個dummy head
2. 兩個list都有東西時才比較, 不然直接串接剩下的 O(min(m,n))
"""