""" 
給予兩個字串needle和haystack, 回傳needle出現在haystack的位置, 如果不包含則回傳-1
"""
import time

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            for j in range(len(needle)):
                if i+j > len(haystack)-1:
                    return -1
                if haystack[i+j] == needle[j]:
                    if j == len(needle)-1:
                        return i
                else:
                    break
        return -1
    
    def strStr2(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1

def test_case_run():
    haystack = "sadbutsad"
    needle = "sad"
    result = Solution.strStr(Solution, haystack, needle)
    print(result)
    
    haystack = "leetcode"
    needle = "leeto"
    result = Solution.strStr(Solution, haystack, needle)
    print(result)
    return

start = time.perf_counter()
test_case_run()
end = time.perf_counter()
print("執行時間：%f 豪秒" % ((end - start)*1000))

""" 
思路:
1. 逐一比對字元 O(m*n)
"""