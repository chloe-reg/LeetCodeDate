""" 
輸入一個字串陣列, 回傳最長的共通前綴字, 沒有則回傳""
"""
import time

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        result = ""
        
        min_len = min(len(s) for s in strs)
        for i in range(min_len):
            char = strs[0][i]
            for s in strs:
                if s[i] != char:
                    return result
            result += char
        return result

def test_case_run():
    strs = ["flower","flow","flight"]
    result = Solution.longestCommonPrefix(Solution, strs)
    print(result)
    
    strs = ["dog","racecar","car"]
    result = Solution.longestCommonPrefix(Solution, strs)
    print(result)
    return

start = time.perf_counter()
test_case_run()
end = time.perf_counter()
print("執行時間：%f 豪秒" % ((end - start)*1000))

""" 
思路:
1. 逐一比較字元是否相同, O(n*m)
"""