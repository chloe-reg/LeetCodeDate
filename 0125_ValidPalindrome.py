""" 
判斷輸入字串是否為回文, 並無視空格,標點,大小寫
"""
import time

class Solution:
    def isPalindrome(self, s: str) -> bool:        
        left = 0
        right = len(s)-1
        
        s = s.lower()
        while left <= right:
            if not s[left].isnumeric() and not s[left].isalpha():
                left += 1
                continue
            if not s[right].isnumeric() and not s[right].isalpha():
                right -= 1
                continue
            
            if s[left] != s[right]:
                return False
            
            left += 1
            right -= 1
        return True

def test_case_run():
    s = "A man, a plan, a canal: Panama"
    result = Solution.isPalindrome(Solution, s)
    print(result)
    s = "race a car"
    result = Solution.isPalindrome(Solution, s)
    print(result)
    s = " "
    result = Solution.isPalindrome(Solution, s)
    print(result)
    s = "0P"
    result = Solution.isPalindrome(Solution, s)
    print(result)
    return

start = time.perf_counter()
test_case_run()
end = time.perf_counter()
print("執行時間：%f 豪秒" % ((end - start)*1000))

"""
Constraints:
1 <= s.length <= 2 * 10^5
s consists only of printable ASCII characters.
"""

""" 
思路:
1. 用兩側逼近法判斷字串是否回文
"""