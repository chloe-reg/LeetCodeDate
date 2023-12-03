""" 
取得一個Linked list的頭head
用pos來表示Linked list尾端連接的索引位置, 如果 pos 是 -1, 則在該Linked list中沒有環
注意這個pos值並沒有輸入到函式中
判斷這個linked list內部有沒有環, 並回傳布林值

Follow up: 用O(1)的空間複雜度解題(固定大小)?
"""
import time

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        fast = head
        while fast and fast.next:
            head = head.next
            fast = fast.next.next
            if head is fast:
                return True
        return False

def test_case_run():
    return

start = time.perf_counter()
test_case_run()
end = time.perf_counter()
print("執行時間：%f 豪秒" % ((end - start)*1000))

"""
Constraints:
The number of the nodes in the list is in the range [0, 10^4].
-10^5 <= Node.val <= 10^5
pos is -1 or a valid index in the linked-list.
"""

""" 
思路:
1. 參考解題
2. 設定兩個指標, 一個跑得慢(一倍速)一個跑得快(兩倍速)
3. 如果沒有環結構的話, 永遠不會撞在一起
4. 如果有環結構的話, 他們的距離會兩格兩格拉開, 進入環之後又一格一格速拉近直到會合
5. 有會合則代表有環結構
"""