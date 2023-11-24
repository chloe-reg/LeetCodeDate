'''
給定兩個非空的連結列表，表示兩個非負整數。數字以相反的順序存儲，每個節點包含一個數字。
將這兩數相加並返回一個新的連結列表。
你可以假設這兩個數字不包含任何前導零，除了數字 0 本身。
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result_node_head = ListNode(0)
        result_node = result_node_head
        carry = 0
        node1 = l1
        node2 = l2
        
        while node1 != None or node2 != None or carry != 0:
            node_sum = carry
            if node1 == None:
                node_sum += 0
            else:
                node_sum += node1.val
            if node2 == None:
                node_sum += 0
            else:
                node_sum += node2.val
                
            carry = node_sum // 10
            node_sum = node_sum % 10
            
            result_node.next = ListNode(node_sum)
            result_node = result_node.next
            
            if node1 != None:
                node1 = node1.next
            if node2 != None:
                node2 = node2.next
        
        result_node_head = result_node_head.next
            
        return result_node_head

'''
思路
1. LinkedList的尾巴為next=None那個Node, 為數字的高位數
2. 兩數字相加由低位加到高位, 由LinkedList頭Node操作到尾Node, 其中會產生Carry位
3. 如果兩邊的Node都為None, 代表數字加總結束, 若Carry位有值要多一個Node
'''
