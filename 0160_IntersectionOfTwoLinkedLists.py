""" 
給予兩個linked list A和B, 如果A和B有交叉點, 回傳那個交叉點, 否則回傳None

Follow up:  O(m + n) time , O(1) memory
"""
import time

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # time O(m*n)
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        tempB = headB
        while headA or tempB:
            if headA is None:
                return None
            if headA is tempB:
                return headA
            else:
                if tempB.next is None:
                    headA = headA.next
                    tempB = headB
                else:
                    tempB = tempB.next
        return None
    
    # time O(m+n)
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        stackA = []
        stackB = []
        while headA is not None:
            stackA.append(headA)
            headA = headA.next
        while headB is not None:
            stackB.append(headB)
            headB = headB.next
        
        resultNode = None
        while len(stackA) != 0 and len(stackB) != 0:
            nodeA = stackA.pop()
            nodeB = stackB.pop()
            if nodeA is nodeB:
                resultNode = nodeA
            else:
                return resultNode
        return resultNode
    
    # 解答中看到別人做的奇妙方法 
    # (https://leetcode.com/problems/intersection-of-two-linked-lists/solutions/1093186/python-magic-solution-o-n-time-o-1-solution/)
    def changeSign(self, head: ListNode):
        while ( head ):
            head.val *= -1
            head = head.next
    
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # 因為題目限制value值必為大於等於1的正數
        self.changeSign(headA) # 將A list的數值全部反轉變負數, 這時和B共同的node也會全部被反轉
        
        while ( headB ): # 在B list中依序找出哪個node開始變負數代表和A交叉
            if headB.val < 0:break
            headB = headB.next
        
        self.changeSign(headA) # 將A list再反轉回來, 讓A B list的數值回到修改前
        return headB

def test_case_run():
    return

start = time.perf_counter()
test_case_run()
end = time.perf_counter()
print("執行時間：%f 豪秒" % ((end - start)*1000))

"""
Constraints:
The number of nodes of listA is in the m.
The number of nodes of listB is in the n.
1 <= m, n <= 3 * 10^4
1 <= Node.val <= 10^5
0 <= skipA < m
0 <= skipB < n
intersectVal is 0 if listA and listB do not intersect.
intersectVal == listA[skipA] == listB[skipB] if listA and listB intersect.
"""

""" 
思路:
1. 暴力破解, 依序比較, 時間複雜度過高

1. 依序存入stack中, 由尾端比較回來, 如果不同的話代表出現分岔
"""