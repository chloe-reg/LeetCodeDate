""" 
給予兩個字串s和t, 判斷t是否為s的字謎
Follow up: What if the inputs contain Unicode characters?
"""
import time

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        while len(s) != 0:
            char = s[0]
            s = s.replace(char,"")
            t = t.replace(char,"")
            if len(s) != len(t):
                return False
        return True

def test_case_run():
    s = "anagram"
    t = "nagaram"
    result = Solution.isAnagram(Solution, s, t)
    print(result)
    s = "rat"
    t = "car"
    result = Solution.isAnagram(Solution, s, t)
    print(result)
    return

start = time.perf_counter()
test_case_run()
end = time.perf_counter()
print("執行時間：%f 豪秒" % ((end - start)*1000))

"""
Constraints:
1 <= s.length, t.length <= 5 * 10^4
s and t consist of lowercase English letters.
"""

""" 
思路:
1. 字母在s和t中出現的次數要相同
2. 分別把s和t中某一個字母替換成空字串"", 剩下的字串長度要相同, 否則False
"""