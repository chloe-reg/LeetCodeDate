""" 

"""
import time

class Solution:
    def reverseString(self, s: list[str]) -> None:
        left = 0
        right = len(s)-1
        while left < right:
            temp = s[left]
            s[left] = s[right]
            s[right] = temp
            left += 1
            right -= 1
        return
    
    def reverseString2(self, s: list[str]) -> None:
        s[:] = s[::-1]
        return

def test_case_run():
    s = ["h","e","l","l","o"]
    Solution.reverseString(Solution, s)
    print(s)
    s = ["H","a","n","n","a","h"]
    Solution.reverseString(Solution, s)
    print(s)
    return

start = time.perf_counter()
test_case_run()
end = time.perf_counter()
print("執行時間：%f 豪秒" % ((end - start)*1000))

"""
Constraints:
1 <= s.length <= 10^5
s[i] is a printable ascii character.
"""

""" 
思路:
1. 交換位置
"""