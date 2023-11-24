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

'''
模擬加法：
    這是最直觀的解法，模擬手工加法的過程，從兩個連結列表的頭部開始相加，同時考慮進位。
    這種方法的時間複雜度為 O(max(m, n))，其中 m 和 n 分別是兩個連結列表的長度。
鏈表反轉： 
    將兩個連結列表反轉，然後執行單鏈表的加法操作，最後再將結果反轉。
    這樣可以減少在進位處理上的代碼量。這種方法的時間複雜度同樣為 O(max(m, n))。
使用遞迴： 
    利用遞迴從最低位開始相加，同時處理進位。這種方法同樣具有簡潔的代碼結構。
    時間複雜度也是 O(max(m, n))。
使用數組存儲中間結果： 
    將兩個連結列表的數字提取出來，轉換成數組，然後執行數組的加法操作，最後將結果轉換回連結列表。
    這種方法同樣具有清晰的邏輯結構。時間複雜度為 O(max(m, n))。
'''